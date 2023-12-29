import unittest
from ..converter import HTMLToMarkdownConverter
from ..formatter import DatasetFormatter

class TestDatasetFormatter(unittest.TestCase):
    def setUp(self):
        self.converter = HTMLToMarkdownConverter()
        self.formatter = DatasetFormatter(self.converter)

    def test_format_entry(self):
        entry = {
            "title": "Test Title",
            "url": "https://example.com/test-title",
            "html": "<p>This is a test.</p>"
        }
        expected_markdown = "## Test Title\n\n[Read More](https://example.com/test-title)\n\nThis is a test."
        self.assertEqual(self.formatter.format_entry(entry), expected_markdown)

    def test_structure_markdown(self):
        title = "Test Title"
        url = "https://example.com/test-title"
        content = "This is a test."
        expected_markdown = "## Test Title\n\n[Read More](https://example.com/test-title)\n\nThis is a test."
        self.assertEqual(self.formatter.structure_markdown(title, url, content), expected_markdown)

    def test_format_dataset(self):
        data = [
            {
                "title": "Test Title 1",
                "url": "https://example.com/test-title-1",
                "html": "<p>This is a test 1.</p>"
            },
            {
                "title": "Test Title 2",
                "url": "https://example.com/test-title-2",
                "html": "<p>This is a test 2.</p>"
            }
        ]
        expected_markdown = "## Test Title 1\n\n[Read More](https://example.com/test-title-1)\n\nThis is a test 1.\n\n## Test Title 2\n\n[Read More](https://example.com/test-title-2)\n\nThis is a test 2."
        self.assertEqual(self.formatter.format_dataset(data), expected_markdown)

if __name__ == '__main__':
    unittest.main()