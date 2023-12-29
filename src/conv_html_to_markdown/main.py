import logging
from concurrent.futures import ThreadPoolExecutor
from converter import HTMLToMarkdownConverter
from formatter import DatasetFormatter
from utils import load_json_files, save_output_in_chunks, chunk_dataset

def process_dataset_chunk(chunk):
    """
    Processes a single chunk of the dataset.
    """
    try:
        formatter = DatasetFormatter(HTMLToMarkdownConverter())
        return formatter.format_dataset(chunk)
    except Exception as e:
        logging.error("Error processing dataset chunk: %s", e)
        return ""

def main():
    """
    Main function to load, process, and save the dataset.
    """
    logging.basicConfig(level=logging.INFO)
    pattern = "output*.json"  # Pattern to match JSON files
    chunk_size = 512  # Adjust chunk size as needed
    max_threads = 15  # Adjust the maximum number of threads as needed
    output_file_name = "gpt-crawler-curated_markdown.md"

    try:
        original_data = load_json_files(pattern)
        chunks = list(chunk_dataset(original_data, chunk_size))
        formatted_contents = process_and_collect_data(chunks, max_threads)
        save_output_in_chunks(output_file_name, formatted_contents)
        logging.info("Conversion process successful. Exiting program.")
    except Exception as e:
        logging.error("An error occurred in the main function: %s", e)

def process_and_collect_data(chunks, max_threads):
    """
    Processes the data chunks in parallel and collects the results.
    """
    logging.info("Processing and saving dataset in chunks.")
    with ThreadPoolExecutor(max_workers=max_threads) as executor:
        return [result for result in executor.map(process_dataset_chunk, chunks)]

if __name__ == "__main__":
    main()
