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
To extract the textual content from PDF documents, I can use the `PyPDF2` library in Python.

- Install the `PyPDF2` library:
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

- Call the `extract_text_from_pdf` function and store the extracted text in a variable:
```python
extracted_text = extract_text_from_pdf(pdf_file_path)
```

- Print the extracted text:
```python
print(extracted_text)
```

Now, if there are multiple PDF documents, we can iterate over them and call the `extract_text_from_pdf` function for each file to extract their content.

*Reasoning: The `PyPDF2` library is a popular choice for extracting text from PDF documents in Python. It provides an easy-to-use interface to extract text page by page. By iterating over the pages, we can extract the textual content and concatenate it to form a complete text representation of the document.*

**Apply text preprocessing techniques such as tokenization, stop word removal, stemming, and lemmatization to clean the extracted text data.**

To apply text preprocessing techniques such as tokenization, stop word removal, stemming, and lemmatization to clean the extracted text data, follow these steps:

- Tokenization: Tokenization is the process of splitting the text into individual tokens or words. Can use the nltk library in Python to perform tokenization.
```python
import nltk

text = "This is an example sentence."

tokens = nltk.word_tokenize(text)

print(tokens)
```

- Stop Word Removal: Stop words are common words that do not carry much meaning and can be removed from the text. Can use the nltk library's stopwords corpus to remove stop words.
```python
from nltk.corpus import stopwords

stop_words = set(stopwords.words('english'))

filtered_tokens = [token for token in tokens if token.lower() not in stop_words]

print(filtered_tokens)
```

- Stemming or Lemmatization: Stemming and lemmatization both aim to reduce words to their base or root form. Stemming is a simpler process that chops off the ends of words, while lemmatization uses language and context to determine the base form. Can choose either stemming or lemmatization based on requirements.
*(Stemming: I can use the nltk library's Porter stemmer to perform stemming.)*
```python
from nltk.stem import PorterStemmer

stemmer = PorterStemmer()

stemmed_tokens = [stemmer.stem(token) for token in filtered_tokens]

print(stemmed_tokens)

```

- Lemmatization: Use the nltk library's WordNet lemmatizer to perform lemmatization.
```python
from nltk.stem import WordNetLemmatizer

lemmatizer = WordNetLemmatizer()

lemmatized_tokens = [lemmatizer.lemmatize(token) for token in filtered_tokens]

print(lemmatized_tokens)

```

**To implement text summarization techniques for generating short summaries of documents, you can follow these steps:**
- Import the necessary libraries:
```python
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.stem import PorterStemmer
from nltk.probability import FreqDist
from heapq import nlargest
```

- Define a function for text summarization:
```python
def generate_summary(text, num_sentences):
    # Tokenize the text into sentences
    sentences = sent_tokenize(text)
    
    # Tokenize the sentences into words
    words = word_tokenize(text)
    
    # Remove stop words
    stop_words = set(stopwords.words('english'))
    words = [word for word in words if word.casefold() not in stop_words]
    
    # Stem the words
    stemmer = PorterStemmer()
    words = [stemmer.stem(word) for word in words]
    
    # Calculate word frequencies
    word_frequencies = FreqDist(words)
    
    # Calculate sentence scores based on word frequencies
    sentence_scores = {}
    for sentence in sentences:
        for word in word_tokenize(sentence.lower()):
            if word in word_frequencies:
                if sentence not in sentence_scores:
                    sentence_scores[sentence] = word_frequencies[word]
                else:
                    sentence_scores[sentence] += word_frequencies[word]
    
    # Get the top 'num_sentences' sentences with highest scores
    summary_sentences = nlargest(num_sentences, sentence_scores, key=sentence_scores.get)
    
    # Join the summary sentences into a summary paragraph
    summary = ' '.join(summary_sentences)
    
    return summary
```

- Use the text summarization function on a sample PDF document:
```python
# Read the PDF document
with open('sample.pdf', 'rb') as file:
    pdf_text = extract_text_from_pdf(file)

# Generate a summary of the document
num_sentences = 3
summary = generate_summary(pdf_text, num_sentences)
print(summary)
```

*In this implementation, I have used NLTK (Natural Language Toolkit) library for text processing tasks such as tokenization, stop word removal, stemming, and frequency distribution calculation. The text summarization technique used here is extractive summarization, where sentences with the highest scores based on word frequencies.*

**Step 5: Implement Vector Retrieval**
I implement vector indexing techniques like similarity search using cosine similarity or other relevant algorithms in Elasticsearch.
Create appropriate queries to retrieve PDF documents based on similarity to a query vector. 
I ensure the vector search process is efficient and scalable by optimizing Elasticsearch settings and indexing strategies.

**To utilize vectorization techniques such as word embeddings and convert the preprocessed text data into vector representations, I follow these steps:**

**- Choose a word embedding technique:** In this case, I use Word2Vec, a popular word embedding technique that represents words as dense vectors.

**- Preprocess the text data:** Apply text preprocessing techniques such as tokenization, stop word removal, stemming, and lemmatization to clean the extracted text data. This step helps in reducing noise and preparing the text for vector representation.

**- Train the Word2Vec model:** Use the preprocessed text data to train the Word2Vec model. This model learns the vector representations of words based on their context in the text data. The model can be trained using the Gensim library in Python.

**- Convert the preprocessed text data into vector representations:** Iterate through each document in the preprocessed text data. For each document, split it into individual words and obtain their corresponding word embeddings from the trained Word2Vec model. Sum up the word embeddings to obtain a vector representation for the document.

**- Store the vector representations in the vector database:** Store the document vector representations in the vector database for efficient storage and retrieval.

*The preprocessed text data can be effectively converted into vector representations using word embeddings. The Word2Vec technique is chosen due to its ability to capture semantic meaning and context of the textual content.*



**Step 6: Test and Validate**
I develop test cases to validate the functionality and quality of the vector database.
I perform unit tests on individual components (e.g., PDF parsing, text preprocessing, vectorization) to ensure they work as expected.

**To test and validate the functionality and quality of the vector database, the following steps can be taken:**

- Develop Test Cases
- Unit Testing
- GRPC API Development
- Error Handling and Input Validation
- Containerization with Docker-compose
- docker-compose.yml Configuration
- Automated Testing
- Container Deployment


**Step 7: GRPC API Development**
I implement a GRPC API to interact with the vector database.
And define appropriate API endpoints for uploading PDF documents, searching through documents, and text summarization.
Ensure proper error handling and input validation within the API.

For GRPC API Development, we need to implement a GRPC API to interact with the vector database. Also need to define appropriate API endpoints for uploading PDF documents, searching through documents, and text summarization. I should ensure proper error handling and input validation within the API.
**Here is a detailed response for the GRPC API development:**

**7.1. Define the protobuf file:**
  
- Create a file called `vector_database.proto` to define the GRPC service and message types.
  
- Define the `Document` message type with fields like `id`, `title`, `content`, and `vector`.

- Define the `UploadDocumentRequest` and `UploadDocumentResponse` message types for uploading documents.

- Define the `SearchRequest` and `SearchResponse` message types for searching through documents.

- Define the `SummarizeRequest` and `SummarizeResponse` message types for text summarization.

- Define the `VectorDatabaseService` with methods for uploading documents, searching, and text summarization.


**7.2. Generate code from the protobuf file:**

- Use the `protoc` compiler to generate the Python code from the `vector_database.proto` file.
- Run the command to generate the code:
```python
protoc -I=. --python_out=. --grpc_python_out=. vector_database.proto
```

**7.3. Implement the server-side of the GRPC API:**

- Create a Python file, e.g., `vector_database_server.py`, to implement the server-side of the GRPC API.
- Import the necessary libraries, including the generated code from the protobuf file.
- Implement the methods defined in the `VectorDatabaseServicer` class.
- For the `UploadDocument` method, handle the document uploading, parsing, and vectorization.
- For the `Search` method, perform the search operation on the vector database based on the provided query.
- For the `Summarize` method, generate a summary of the provided text.
- Implement proper error handling and input validation to ensure the API behaves as expected.


**7.4. Implement the client-side of the GRPC API (optional):**

- Create a Python file, e.g., `vector_database_client.py`, to implement the client-side of the GRPC API.
- Import the necessary libraries, including the generated code from the protobuf file.
- Create a GRPC channel to connect to the server

**To implement a GRPC API to interact with the vector database**

- Define the protobuf file: Create a protobuf file that defines the messages and services for your GRPC API. For example, Create a file named `vector_db.proto`:
```protobuf
syntax = "proto3";

package vectordb;

service VectorDatabase {
  rpc UploadDocument (Document) returns (UploadResponse) {}
  rpc SearchDocuments (SearchRequest) returns (SearchResponse) {}
  rpc SummarizeText (TextSummaryRequest) returns (TextSummaryResponse) {}
}

message Document {
  string id = 1;
  string content = 2;
}

message UploadResponse {
  bool success = 1;
  string message = 2;
}

message SearchRequest {
  string query = 1;
}

message SearchResponse {
  repeated Document found_documents = 1;
}

message TextSummaryRequest {
  string text = 1;
}

message TextSummaryResponse {
  string summary = 1;
}
```

**Generate code from the protobuf file:** Use the `grpc_tools` package to generate the Python code from the protobuf file. Open terminal and run the command to generate the necessary code:
```Bash
python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. vector_db.proto
```

**Implement the server:** I Create a Python file, let's say `vector_db_server.py`, and implement the server code using GRPC.
```Python
import grpc
from concurrent import futures
import vector_db_pb2
import vector_db_pb2_grpc

class VectorDatabaseServicer(vector_db_pb2_grpc.VectorDatabaseServicer):
    def UploadDocument(self, request, context):
        # Implement your logic to handle document upload
        # For example, you can store the document in the vector database and return a success message
        response = vector_db_pb2.UploadResponse()
        response.success = True
        response.message = "Document uploaded successfully"
        return response

    def SearchDocuments(self, request, context):
        # Implement your logic to search documents based on a query
        # For example, retrieve relevant documents from the vector database and return them as a response
        response = vector_db_pb2.Search
```

**Step 8: Containerization with Docker-compose**
**8.1. Install Docker and Docker Compose**
- Install/Open Docker Engine on my machine

8.2. Create a Dockerfile for the API
In the root directory of your project, create a new file called Dockerfile:

```
# Use a Python base image
FROM python:3.9

# Set the working directory
WORKDIR /app

# Copy the requirements file
COPY requirements.txt .

# Install the requirements
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire project
COPY . .

# Expose the port for the API
EXPOSE 5000

# Set the entry point
CMD ["python", "app.py"]
```


**8.3. Create a Docker Compose file**
In the root directory, create a new file called docker-compose.yml:

```yaml
version: '3'
services:
  api:
    build: .
    ports:
      - "5000:5000"
    volumes:
      - .:/app
    depends_on:
      - elasticsearch
  elasticsearch:
    image: docker.elastic.co/elasticsearch/elasticsearch:7.17.3
    environment:
      - discovery.type=single-node
    volumes:
      - elasticsearch-data:/usr/share/elasticsearch/data
volumes:
  elasticsearch-data:
```

**This Compose file defines two services:**
- api: Builds the API container from the current directory using the Dockerfile.
- elasticsearch: Runs an Elasticsearch container using the official Docker image.


**8.4. Update the API code to connect to Elasticsearch**
In API code, update the Elasticsearch connection settings to point to the Docker container. For using the elasticsearch Python client:

```python
from elasticsearch import Elasticsearch

es = Elasticsearch(hosts=["http://elasticsearch:9200"])
```

**8.5. Build and run the containers**
Open the terminal, navigate to the root directory of the project and then:
```
docker-compose up --build
```
*This command will build the API container and start both the API and Elasticsearch containers.*


**8.6. Test the API**
With the containers running, we should be able to access the API at http://localhost:5000. We can use tools like Postman or curl to send requests to the API endpoints.
*By following these steps, we have containerized the vector database API using Docker Compose. The API container is built from the provided Dockerfile, and the Elasticsearch container is pulled from the official Docker image. The containers are linked together using the Docker Compose file, allowing the API to communicate with Elasticsearch.*
