# Document Q&A System using LlamaIndex

This Python program creates a **Document QA (Question & Answer) System** using the `LlamaIndex` library. It allows you to load documents (PDF or text files) from a folder, create a searchable index, and answer questions based on the content of those documents.

---

## Features

- **Document Loading**: Loads PDF and text files from a specified folder.
- **Index Creation**: Creates a searchable vector index using `LlamaIndex`.
- **Question Answering**: Allows users to ask questions and get answers based on the document content.
- **Interactive Mode**: Supports multiple questions in an interactive loop until the user exits.

---

## Prerequisites

Before running the program, ensure you have the following installed:

1. **Python 3.7 or higher**.
2. **Required Python libraries**:
   - `llama-index`
   - `PyPDF2`
   - `python-dotenv`

You can install the required libraries using `pip`:

```
pip install llama-index python-dotenv PyPDF2
```

---

## Setup

1. **Clone the Repository**:

```
git clone https://github.com/yourusername/document-qa-system.git
cd document-qa-system
```

2. **Create a Documents Folder**:

Create a folder named documents in the project directory.

Place your PDF or text files in this folder.

3. **Environment Variables (Optional)**:

If you are using an OpenAI API key, create a .env file in the project directory and add your API key:

```
OPENAI_API_KEY=your_api_key_here
```

---

## Usage

1. **Run the Program**:

```
python document_qa_system.py
```

1. **Ask Questions**:

The program will prompt you to enter a question.

Type your question and press Enter to get an answer.

To exit the program, type `exit` and press Enter.

---

## Example Interaction

```
Enter your question (or type 'exit' to quit): What is the main topic of the documents?

Question: What is the main topic of the documents?
Answer: The main topic of the documents is artificial intelligence and machine learning.

Enter your question (or type 'exit' to quit): Who is the author of the documents?

Question: What is the total current sales?
Answer: The total current sales amount is $638,000.

Enter your question (or type 'exit' to quit): exit
Exiting the program. Goodbye!
```

---

## Code Structure

* `load_documents_from_folder(folder_path)`:

Loads PDF and text files from the specified folder.

Extracts text from PDF files using `PyPDF2`.

Returns a list of documents.

* `create_index(documents)`:

Creates a vector index using LlamaIndex's VectorStoreIndex.

* `query_index(index, question)`:

Queries the index with a user-provided question and returns the answer.

* `main()`:

The main function that loads documents, creates the index, and runs the interactive Q&A loop.

---

## Customization

* **Add More Document Types**:

   * Extend the `load_documents_from_folder` function to support additional file types (e.g., Word documents, HTML files).

* **Advanced Querying**:

   * Use advanced features of `LlamaIndex`, such as metadata filtering or hybrid search, to improve query results.

* **Save Conversation History**:

   * Modify the program to save the conversation history to a file for future reference.

---

## Troubleshooting
# Common Issues

1. **Import Errors**:

   * Ensure you have installed the correct version of llama-index:

```
pip install llama-index --upgrade
```

2. **PDF Text Extraction Issues**:

   * Some PDF files may not extract text correctly. Use OCR tools for scanned PDFs.

3. **API Key Errors**:

   * If using OpenAI, ensure your API key is correctly set in the `.env` file or environment variables.

---

## License
This project is licensed under the MIT License. See the [LICENSE](https://opensource.org/license/mit) file for details.
