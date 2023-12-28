from converter import HTMLToMarkdownConverter
import logging

class DatasetFormatter:
    """
    A class to format a dataset of HTML entries into structured Markdown.

    Attributes:
        converter (HTMLToMarkdownConverter): An instance of \
            HTMLToMarkdownConverter for HTML to Markdown conversion.

    Methods:
        format_entry(entry): Formats a single dataset entry into Markdown.
        structure_markdown(title, url, content): Structures \
            Markdown content with headers and links.
        format_dataset(data): Formats an entire dataset \
            of entries into Markdown.
    """

    def __init__(self, converter):
        self.converter = converter

    def format_entry(self, entry):
        """Format a single entry from the dataset."""
        try:
            title = entry.get("title", "Untitled")
            url = entry.get("url", "")
            html_content = entry.get("html", "")
            logging.info("Formatted entry: %s", title)
            markdown_content = self.converter.convert(html_content)
            return self.structure_markdown(title, url, markdown_content)
        except Exception as e:
            logging.error("Error formatting entry: %s", e)
            return ""

    def structure_markdown(self, title, url, content):
        """Structure the Markdown content with headers, lists, etc."""
        structured_content = f"## {title}\n\n"
        if url:
            structured_content += f"[Read More]({url})\n\n"
        structured_content += (
            content.strip()
        )  # Remove leading and trailing whitespace/newlines
        return structured_content

    def format_dataset(self, data):
        """
        Formats the entire dataset.
        Formats each entry in the dataset and joins them with newlines.
        """
        return "\n\n".join(self.format_entry(entry) for entry in data)