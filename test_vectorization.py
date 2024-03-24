import unittest
import numpy as np
from pdf_vector_search import vectorize_text, create_vector_index, search_vectors

class TestVectorization(unittest.TestCase):
    def test_vectorize_text(self):
        # Test cases for text vectorization
        text = "This is a sample text for vectorization."
        vector = vectorize_text(text)
        self.assertEqual(len(vector), 384)  # Assuming the length of the vector is 384

    def test_create_vector_index(self):
        # Test cases for vector indexing
        vectors = [np.random.rand(384) for _ in range(10)]
        index = create_vector_index(vectors)
        self.assertEqual(index.ntotal, 10)  # Assuming 10 vectors were indexed

    def test_search_vectors(self):
        # Test cases for vector search
        texts = ["Text 1", "Text 2", "Text 3", "Text 4", "Text 5"]
        vectors = [np.random.rand(384) for _ in range(len(texts))]
        index = create_vector_index(vectors)
        query_vector = np.random.rand(384)
        top_k_docs = search_vectors(query_vector, index, texts)
        self.assertEqual(len(top_k_docs), 5)  # Assuming top 5 results are returned

if __name__ == '__main__':
    unittest.main()