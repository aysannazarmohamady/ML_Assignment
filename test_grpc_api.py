import unittest
import grpc
from concurrent import futures
import pdf_vector_search_pb2
import pdf_vector_search_pb2_grpc
from pdf_vector_search import VectorSearchService

class TestGRPCAPI(unittest.TestCase):
    def setUp(self):
        # Set up a test server
        self.server = grpc.server(futures.ThreadPoolExecutor(max_workers=1))
        pdf_vector_search_pb2_grpc.add_VectorSearchServiceServicer_to_server(
            VectorSearchService(index, texts, summaries), self.server)
        self.server.add_insecure_port('[::]:50051')
        self.server.start()

        # Create a test client
        self.channel = grpc.insecure_channel('localhost:50051')
        self.stub = pdf_vector_search_pb2_grpc.VectorSearchServiceStub(self.channel)

    def tearDown(self):
        # Stop the test server
        self.server.stop(None)

    def test_search_documents(self):
        # Test cases for the SearchDocuments method
        request = pdf_vector_search_pb2.SearchRequest(query="Sample query")
        response = self.stub.SearchDocuments(request)
        self.assertGreater(len(response.documents), 0)  # Assuming some documents are returned

if __name__ == '__main__':
    unittest.main()