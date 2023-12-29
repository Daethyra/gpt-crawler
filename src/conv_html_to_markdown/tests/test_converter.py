import unittest
from bs4 import BeautifulSoup
from markdownify import markdownify as md
from transformers import AutoTokenizer, AutoModel
import torch
import logging

class HTMLToMarkdownConverterTest(unittest.TestCase):
    def setUp(self):
        self.converter = HTMLToMarkdownConverter()

    def test_initialize_embedding_model(self):
        tokenizer, model = self.converter._initialize_embedding_model()
        self.assertIsInstance(tokenizer, AutoTokenizer)
        self.assertIsInstance(model, AutoModel)

    def test_curate_content(self):
        html = '<html><head></head><body><div class="cookie">Cookie</div></body></html>'
        expected_html = '<html><head></head><body></body></html>'
        curated_html = self.converter._curate_content(html)
        self.assertEqual(curated_html, expected_html)

    def test_remove_selectors(self):
        html = '<html><head></head><body><header>Header</header></body></html>'
        expected_html = '<html><head></head><body></body></html>'
        soup = BeautifulSoup(html, "html.parser")
        self.converter._remove_selectors(soup)
        self.assertEqual(str(soup), expected_html)

    def test_strip_tags(self):
        html = '<html><head></head><body><script>Script</script></body></html>'
        expected_html = '<html><head></head><body></body></html>'
        soup = BeautifulSoup(html, "html.parser")
        self.converter._strip_tags(soup)
        self.assertEqual(str(soup), expected_html)

    def test_convert(self):
        html = '<html><head></head><body><p>Hello World!</p></body></html>'
        expected_markdown = 'Hello World!'
        markdown_content = self.converter.convert(html)
        self.assertEqual(markdown_content, expected_markdown)

if __name__ == '__main__':
    unittest.main()