import os
from llama_index.core import VectorStoreIndex, Document
from PyPDF2 import PdfReader
from dotenv import load_dotenv

# Load environment variables (if any)
load_dotenv()

# Define the path to the documents folder
DOCUMENTS_FOLDER = "documents"


def load_documents_from_folder(folder_path):
    documents = []
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        if filename.endswith(".pdf"):
            # Read PDF files
            reader = PdfReader(file_path)
            text = ""
            for page in reader.pages:
                text += page.extract_text()
            documents.append(Document(text=text, metadata={"filename": filename}))
        elif filename.endswith(".txt"):
            # Read text files
            with open(file_path, "r", encoding="utf-8") as file:
                text = file.read()
            documents.append(Document(text=text, metadata={"filename": filename}))
    return documents

def create_index(documents):
    # Create a vector index from the documents
    index = VectorStoreIndex.from_documents(documents)
    return index

def query_index(index, question):
    # Query the index with a question
    query_engine = index.as_query_engine()
    response = query_engine.query(question)
    return response

def main():
    # Load documents from the folder
    documents = load_documents_from_folder(DOCUMENTS_FOLDER)
    
    # Create the index
    index = create_index(documents)
    
    # Loop to ask multiple questions
    while True:
        # Get user input
        question = input("\nEnter your question (or type 'exit' to quit): ")
        
        # Exit the loop if the user types 'exit'
        if question.lower() == "exit":
            print("Exiting the program. Goodbye!")
            break
        
        # Query the index with the user's question
        response = query_index(index, question)
        
        # Display the response
        print("\nQuestion:", question)
        print("Answer:", response)

if __name__ == "__main__":
    main()