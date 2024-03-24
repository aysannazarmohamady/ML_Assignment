# PDF Vector Search

This project is a vector database API that utilizes search through a large number of PDF documents. It follows a pipeline approach to extract text from PDF files, preprocess the text, generate summaries, create vector representations of the documents, and index these vectors for efficient similarity search. The main steps in this pipeline are:

## Step 1: Text Extraction

The `main.py` script reads PDF files from the `pdf_folder` directory and extracts the text content using the `extract_text_from_pdf` function defined in `main.py`. This function uses the `pdfplumber` library to extract text from each page of the PDF document.

### Instructions
1. Create a directory named `pdf_folder` in the project root.
2. Place your PDF files in the `pdf_folder` directory.

## Step 2: Text Preprocessing

The extracted text is then preprocessed using the `preprocess_text` function in `main.py`. This step involves tokenization, stop word removal, stemming, and lemmatization to clean and prepare the text for further processing. You can customize the preprocessing steps by modifying this function.

### Customization
To customize the text preprocessing steps, modify the `preprocess_text` function in `main.py`. You can use libraries like NLTK, spaCy, or other NLP tools to implement your desired preprocessing techniques, such as using different tokenizers, stop word lists, or stemming/lemmatization algorithms.

## Step 3: Text Summarization

The preprocessed text is summarized using the `summarize_text` function in `main.py`. This function utilizes the `summarizer` library to generate a concise summary of the document.

## Step 4: Text Vectorization

The `vectorize_text` function in `main.py` converts the preprocessed text into a dense vector representation using the pre-trained sentence embedding model from the `sentence-transformers` library.

## Step 5: Vector Indexing

The document vectors are indexed using the `create_vector_index` function in `main.py`, which creates a flat L2 index using the `faiss` library. This index allows for efficient similarity search between the document vectors and a query vector. You can modify the index type and metric type in the `config.ini` file.

### Customization
To change the index type and metric type used by the `faiss` library for vector indexing, modify the `config.ini` file and update the `index_type` and `metric_type` values under the `[faiss]` section.

## Step 6: Search and Retrieval

When a user submits a query through the GRPC API, the `SearchDocuments` method in the `VectorSearchService` class (defined in `main.py`) vectorizes the query text, performs a similarity search on the vector index using the `search_vectors` function, and returns the top k most relevant documents along with their summaries and distances from the query vector.

## Step 7: GRPC API

The GRPC API is defined in the `pdf_vector_search.proto` file, which specifies the service and message types for the vector search functionality. The `pdf_vector_search_pb2.py` and `pdf_vector_search_pb2_grpc.py` files are generated from the `.proto` file using the `grpc_tools` module and provide the Python implementation of the GRPC service and messages.

### Instructions
1. Generate the GRPC Python files by running the following command:
   `python -m grpc_tools.protoc -I./protos --python_out=. --grpc_python_out=. ./protos/pdf_vector_search.proto`
2. To interact with the GRPC API, you can use a GRPC client library in your preferred programming language or use a tool like `grpc_cli`.

## Step 8: Containerization

The project can be containerized using Docker for easy deployment and scaling. The `Dockerfile` defines the steps to build the Docker image, including installing dependencies, copying the project files, and setting the entry point to run the `main.py` script.

### Instructions
1. Build the Docker image:
   `docker build -t pdf-vector-search .`
2. Run the Docker container:
   `docker run -p 50051:50051 pdf-vector-search`

## Step 9: CI/CD Pipeline

The `.github/workflows/ci-cd.yml` file defines the CI/CD pipeline using GitHub Actions. The pipeline consists of two jobs: `build` and `deploy`. The `build` job sets up the Python environment, installs dependencies, and runs tests. The `deploy` job builds and pushes the Docker image to a Docker registry (e.g., Azure Container Registry). You can customize the deployment target by modifying the `deploy` job in the workflow file.

### Customization
To customize the CI/CD pipeline, modify the `.github/workflows/ci-cd.yml` file. You can add additional jobs, change the deployment target, or integrate with other tools and services as per your requirements.

## Step 10: Configuration

The `config.ini` file stores the project configuration settings, such as the PDF folder location, GRPC port, pre-trained model for text vectorization, Faiss index and metric types, Docker image and container names, and logging settings. The `config.py` module provides a helper function to load and access these configuration values.

## Step 11: Tests

The `tests` directory contains test files for different components of the project, such as `test_text_processing.py` for testing the text extraction, preprocessing, and summarization functions, `test_vectorization.py` for testing the vectorization and vector indexing functions, `test_grpc_api.py` for testing the GRPC API implementation, and `test_containerization.py` for testing the containerization and CI/CD implementation. You can extend these test files or add new ones as needed.

### Customization
To extend or add new test cases, modify the existing test files or create new ones in the `tests` directory. Follow the existing test structure and use the `unittest` module to write and run your tests.

## Customization

This project is designed to be customizable and extensible. You can modify various components to suit your specific requirements:

- **Text Preprocessing**: Customize the `preprocess_text` function in `main.py` to implement your desired text preprocessing steps, such as using different tokenizers, stop word lists, or stemming/lemmatization algorithms.
- **Vector Indexing**: Modify the `config.ini` file to change the index type and metric type used by the `faiss` library for vector indexing.
- **CI/CD Pipeline**: Customize the `.github/workflows/ci-cd.yml` file to modify the CI/CD pipeline, such as adding additional jobs, changing the deployment target, or integrating with other tools and services.
- **Tests**: Extend the existing test files or add new ones to cover additional functionality or edge cases.

