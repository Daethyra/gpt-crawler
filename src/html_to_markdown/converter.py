from bs4 import BeautifulSoup
from markdownify import markdownify as md
from transformers import AutoTokenizer, AutoModel
import torch
import logging

class HTMLToMarkdownConverter:
    """
    A converter class that transforms HTML content to Markdown
    format and processes text embeddings.
    """

    def __init__(self, strip_tags=None, convert_links=True):
        """
        Initialize the converter with configuration options and
        Jina embeddings model.
        """
        self.strip_tags = strip_tags or ["script", "style", "meta"]
        self.convert_links = convert_links
        self.tokenizer, self.model = self._initialize_embedding_model()

    def _initialize_embedding_model(self):
        """
        Initialize the tokenizer and model for embeddings.
        """
        tokenizer = AutoTokenizer.from_pretrained(
            "jinaai/jina-embeddings-v2-small-en", trust_remote_code=True
        )
        model = AutoModel.from_pretrained("jinaai/jina-embeddings-v2-small-en")
        return tokenizer, model

    def mean_pooling(self, model_output, attention_mask):
        """Applies mean pooling to the token embeddings to
        create sentence embeddings."""
        token_embeddings = model_output[0]
        input_mask_expanded = (
            attention_mask.unsqueeze(-1).expand(token_embeddings.size()).float()
        )
        sum_embeddings = torch.sum(token_embeddings * input_mask_expanded, 1)
        sum_mask = torch.clamp(input_mask_expanded.sum(1), min=1e-9)
        return sum_embeddings / sum_mask

    def _process_embeddings(self, lines, batch_size=32):
        """Processes the embeddings for the given lines in batches."""
        batched_embeddings = []
        for i in range(0, len(lines), batch_size):
            batch = lines[i : i + batch_size]
            encoded_input = self.tokenizer(
                batch, padding=True, truncation=True, return_tensors="pt"
            )
            with torch.no_grad():
                model_output = self.model(**encoded_input)
            batch_embeddings = self.mean_pooling(
                model_output, encoded_input["attention_mask"]
            )
            batched_embeddings.extend(batch_embeddings)

        return torch.nn.functional.normalize(
            torch.stack(batched_embeddings), p=2, dim=1
        )

    def _remove_redundant_data(self, embeddings, lines):
        """Removes redundant lines based on semantic similarity
        using embeddings."""
        cleaned_lines = [lines[0]]  # Always include the first line
        for i in range(1, len(lines)):
            similarity = torch.cosine_similarity(
                embeddings[i].unsqueeze(0), embeddings[i - 1].unsqueeze(0)
            )
            if similarity.item() < 0.86899:  # Threshold for redundancy
                cleaned_lines.append(lines[i])
        return "\n".join(cleaned_lines)

    def convert(self, html_content):
        """
        Converts HTML content to Markdown format.
        """
        try:
            curated_html = self._curate_content(html_content)
            markdown_content = md(
                curated_html,
                strip_tags=self.strip_tags,
                convert_links=self.convert_links,
            ).strip()
            lines = markdown_content.split("\n")
            embeddings = self._process_embeddings(lines)
            return self._remove_redundant_data(embeddings, lines)
        except Exception as e:
            logging.error("Error during conversion: %s", e)
            raise

    def _curate_content(self, html):
        """
        Curates the HTML content by removing specified elements and tags.
        """
        try:
            soup = BeautifulSoup(html, "html.parser")
            self._remove_selectors(soup)
            self._strip_tags(soup)
            return str(soup)
        except Exception as e:
            logging.error("Error in curating HTML content: %s", e)
            return html

    def _remove_selectors(self, soup):
        """
        Removes specific selectors from the BeautifulSoup object.
        """
        selectors = [
            "header", "footer", "nav", ".navbar", ".menu", ".footer-links",
            "#sidebar", "#ad-container", 'div[class*="cookie"], div[class*="banner"]',
            "aside", ".pagination", "form"
        ]
        for selector in selectors:
            for element in soup.select(selector):
                element.decompose()

    def _strip_tags(self, soup):
        """
        Strips specified tags from the BeautifulSoup object.
        """
        for tag in self.strip_tags:
            for s in soup(tag):
                s.decompose()

