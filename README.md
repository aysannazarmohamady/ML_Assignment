# ML_Assignment
Develop a vector database API that utilizes search through a large number of PDF documents. 


**Step 1: Choose a Database Management System (DBMS)**
I select a suitable DBMS that supports efficient storage and retrieval of high-dimensional vectors. Some popular options include Elasticsearch, Apache Solr, and PostgreSQL with the pg_similarity extension. For this task, I will use Elasticsearch.

**Step 2: Install Elasticsearch**
I install Elasticsearch on my local machine or set up a cloud-based Elasticsearch cluster. Following the official Elasticsearch documentation for installation instructions.

**Step 3: Define the Vector Database Schema**
I decide on the structure and format of the vectors to be stored in the database. For example, Can choose to represent vectors as dense vectors or sparse vectors.
Define the necessary fields to store vector data, document metadata, and any additional information required.

**Step 4: Indexing PDF Documents**
I use a document parsing library or tool, such as Apache Tika or PDFMiner, to extract textual content from the PDF documents.
And clean the extracted text by applying text preprocessing techniques like tokenization, stop word removal, stemming, and lemmatization.
Implement text summarization techniques (e.g., extractive or abstractive summarization) to generate short summaries of the documents.
Utilize vectorization techniques like word embeddings (e.g., Word2Vec, GloVe) to convert the preprocessed text data into vector representations.
Store the vector representations and other relevant metadata (e.g., document ID, title, summary) in the Elasticsearch index.

- Using parsing tools to extract the textual content from the PDF documents
To extract the textual content from PDF documents, I can use the PyPDF2 library in Python.

- Install the PyPDF2 library:
```python
pip install PyPDF2
```

- Import the necessary modules:
```python
import PyPDF2
```

- Define a function to extract text from a PDF file:
```python
def extract_text_from_pdf(file_path):
    text = ""
    with open(file_path, "rb") as file:
        reader = PyPDF2.PdfFileReader(file)
        total_pages = reader.numPages
        for page_num in range(total_pages):
            page = reader.getPage(page_num)
            text += page.extractText()
    return text
```

- Provide the file path to the PDF document you want to extract text from:
```python
pdf_file_path = "path_to_your_pdf_file.pdf"
```

- Call the extract_text_from_pdf function and store the extracted text in a variable:
```python
extracted_text = extract_text_from_pdf(pdf_file_path)
```

- Print the extracted text:
```python
print(extracted_text)
```

Now, if there are multiple PDF documents, we can iterate over them and call the extract_text_from_pdf function for each file to extract their content.

*Reasoning: The PyPDF2 library is a popular choice for extracting text from PDF documents in Python. It provides an easy-to-use interface to extract text page by page. By iterating over the pages, we can extract the textual content and concatenate it to form a complete text representation of the document.*






**Step 5: Implement Vector Retrieval**
I implement vector indexing techniques like similarity search using cosine similarity or other relevant algorithms in Elasticsearch.
Create appropriate queries to retrieve PDF documents based on similarity to a query vector. 
I ensure the vector search process is efficient and scalable by optimizing Elasticsearch settings and indexing strategies.

**Step 6: Test and Validate**
I develop test cases to validate the functionality and quality of the vector database.
I perform unit tests on individual components (e.g., PDF parsing, text preprocessing, vectorization) to ensure they work as expected.

**Step 7: GRPC API Development**
I implement a GRPC API to interact with the vector database.
And define appropriate API endpoints for uploading PDF documents, searching through documents, and text summarization.
Ensure proper error handling and input validation within the API.

**Step 8: Containerization with Docker-compose**
I create a Dockerfile to define the environment and dependencies required for running the vector database and GRPC API.
I write a docker-compose.yml file to configure the entire solution, including the vector database, GRPC API, and any other required services.
Set up a CI/CD pipeline for the solution to automatically build containers and deploy the application.
Configure automated testing to validate the functionality and quality of the API.
Ensure the solution is containerized and can be deployed using Docker-compose or similar tools for continuous integration and deployment.
Docker-compose for easy deployment and continuous integration. Additionally, GRPC endpoints can be implemented for efficient data uploading and retrieval.
