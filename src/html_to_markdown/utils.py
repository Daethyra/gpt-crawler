import glob
import json
import logging

def load_json_files(pattern):
    """
    Load data from multiple JSON files matching a pattern.
    """
    try:
        aggregated_data = []
        for file_path in glob.glob(pattern):
            with open(file_path, "r", encoding="utf-8") as file:
                aggregated_data.extend(json.load(file))
        return aggregated_data
    except Exception as e:
        logging.error("Error loading JSON files: %s", e)
        return []

def save_output_in_chunks(file_path, contents, chunk_size=1024):
    """
    Save the given content into a file in chunks.
    """
    try:
        with open(file_path, "w", encoding="utf-8") as file:
            for content in contents:
                file.write(content)
                if len(content) > chunk_size:
                    file.flush()
    except Exception as e:
        logging.error("Error saving output in chunks: %s", e)

def chunk_dataset(data, chunk_size):
    """
    Yields chunks of the dataset for processing.
    """
    try:
        for i in range(0, len(data), chunk_size):
            yield data[i : i + chunk_size]
    except Exception as e:
        logging.error("Error chunking dataset: %s", e)
        return []

def process_chunk(chunk):
    """
    Processes a single chunk of the dataset.
    """
    try:
        formatter = DatasetFormatter(HTMLToMarkdownConverter())
        return formatter.format_dataset(chunk)
    except Exception as e:
        logging.error("Error processing chunk: %s", e)
        return ""