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

**Step 8: Containerization with Docker-compose**
I create a Dockerfile to define the environment and dependencies required for running the vector database and GRPC API.
I write a docker-compose.yml file to configure the entire solution, including the vector database, GRPC API, and any other required services.
Set up a CI/CD pipeline for the solution to automatically build containers and deploy the application.
Configure automated testing to validate the functionality and quality of the API.
Ensure the solution is containerized and can be deployed using Docker-compose or similar tools for continuous integration and deployment.
Docker-compose for easy deployment and continuous integration. Additionally, GRPC endpoints can be implemented for efficient data uploading and retrieval.
