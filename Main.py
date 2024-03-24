import os
import docker
from pdfplumber import open as open_pdf
from sentence_transformers import SentenceTransformer
from sklearn.feature_extraction.text import TfidfVectorizer
from summarizer import Summarizer
import faiss
import numpy as np

# Text extraction function
def extract_text_from_pdf(pdf_file):
    with open_pdf(pdf_file) as pdf:
        text = ""
        for page in pdf.pages:
            text += page.extract_text()
    return text

# Text preprocessing function
def preprocess_text(text):
    # Tokenize, remove stopwords, stem/lemmatize, etc.
    # You can use libraries like NLTK, spaCy, or other NLP tools here
    return preprocessed_text

# Text summarization function
def summarize_text(text):
    model = Summarizer()
    summary = model(text, ratio=0.2)  # Summarize to 20% of the original text
    return summary

# Vectorization function
def vectorize_text(text):
    model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')
    vector = model.encode([text])[0]
    return vector

# Vector indexing and search function
def create_vector_index(vectors):
    index = faiss.IndexFlatL2(len(vectors[0]))
    index.add(np.array(vectors))
    return index

def search_vectors(query_vector, index, texts):
    k = 5  # Number of top results to retrieve
    distances, indices = index.search(np.array([query_vector]), k)
    top_k_docs = [(texts[idx], distances[0][i]) for i, idx in enumerate(indices[0])]
    return top_k_docs

# GRPC API implementation
import grpc
from concurrent import futures
import pdf_vector_search_pb2
import pdf_vector_search_pb2_grpc

class VectorSearchService(pdf_vector_search_pb2_grpc.VectorSearchServiceServicer):
    def __init__(self, index, texts, summaries):
        self.index = index
        self.texts = texts
        self.summaries = summaries

    def SearchDocuments(self, request, context):
        query_text = request.query
        query_vector = vectorize_text(query_text)
        top_k_docs = search_vectors(query_vector, self.index, self.texts)
        response = pdf_vector_search_pb2.SearchResponse()
        for doc, distance in top_k_docs:
            doc_idx = self.texts.index(doc)
            summary = self.summaries[doc_idx]
            response.documents.add(text=doc, distance=distance, summary=summary)
        return response

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    pdf_vector_search_pb2_grpc.add_VectorSearchServiceServicer_to_server(VectorSearchService(index, texts, summaries), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()

# Containerization and CI/CD implementation
# Set up a CI/CD pipeline using Docker or Kubernetes
# Implement automated testing and deployment

# Main function
def main():
    # Process PDF documents
    pdf_files = [f for f in os.listdir('pdf_folder') if f.endswith('.pdf')]
    texts = []
    vectors = []
    summaries = []
    for pdf_file in pdf_files:
        text = extract_text_from_pdf(os.path.join('pdf_folder', pdf_file))
        preprocessed_text = preprocess_text(text)
        summary = summarize_text(preprocessed_text)
        vector = vectorize_text(preprocessed_text)
        texts.append(preprocessed_text)
        vectors.append(vector)
        summaries.append(summary)

    # Create vector index
    index = create_vector_index(vectors)

    # Start GRPC server
    serve()

if __name__ == "__main__":
    main()