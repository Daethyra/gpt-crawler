import unittest
import glob
import json
import logging
from ..utils import load_json_files, save_output_in_chunks, chunk_dataset, process_chunk

class TestLoadJsonFiles(unittest.TestCase):
    def test_load_json_files(self):
        pattern = "test_data/*.json"
        aggregated_data = load_json_files(pattern)
        self.assertIsNotNone(aggregated_data)
        self.assertGreater(len(aggregated_data), 0)

class TestSaveOutputInChunks(unittest.TestCase):
    def test_save_output_in_chunks(self):
        file_path = "test_data/output.txt"
        contents = ["This is a test", "This is another test"]
        save_output_in_chunks(file_path, contents)
        with open(file_path, "r") as f:
            output = f.read()
        self.assertEqual(output, "This is a testThis is another test")

class TestChunkDataset(unittest.TestCase):
    def test_chunk_dataset(self):
        data = [1, 2, 3, 4, 5]
        chunk_size = 2
        chunks = list(chunk_dataset(data, chunk_size))
        self.assertEqual(len(chunks), 3)
        self.assertEqual(chunks[0], [1, 2])
        self.assertEqual(chunks[1], [3, 4])
        self.assertEqual(chunks[2], [5])

class TestProcessChunk(unittest.TestCase):
    def test_process_chunk(self):
        chunk = ["This is a test", "This is another test"]
        result = process_chunk(chunk)
        self.assertEqual(result, "This is a test\nThis is another test\n")

if __name__ == '__main__':
    unittest.main()