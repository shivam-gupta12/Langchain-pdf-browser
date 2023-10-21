# MultiPDF Chat App

## Task1 - uploading the pdf 

The pdf "Big_Mac_Index" is in docs folder

## Task2 - Using Langchain to create a question generation chain. 

questions that belong to three categories namely True or False, Multiple Choice Questions (MCQs), and one-word answers.

checkout notebook.ipynb for this task

## Task3 - Generate Questions and their corresponding answers.

checkout notebook.ipynb for this task also

# As extra, I have hosted my application on Streamlit 

To run the app : streamlit run app.py

## How It Works
------------

![MultiPDF Chat App Diagram](./docs/PDF-LangChain.jpg)

The application follows these steps to provide responses to your questions:

1. PDF Loading: The app reads multiple PDF documents and extracts their text content.

2. Text Chunking: The extracted text is divided into smaller chunks that can be processed effectively.

3. Language Model: The application utilizes a language model to generate vector representations (embeddings) of the text chunks.

4. Similarity Matching: When you ask a question, the app compares it with the text chunks and identifies the most semantically similar ones.

5. Response Generation: The selected chunks are passed to the language model, which generates a response based on the relevant content of the PDFs.

## Dependencies and Installation
----------------------------
To install the MultiPDF Chat App, please follow these steps:

1. Clone the repository to your local machine.

2. Install the required dependencies by running the following command:
   ```
   pip install -r requirements.txt
   ```

3. Obtain an API key from OpenAI and add it to the `.env` file in the project directory.
```commandline
OPENAI_API_KEY=your_secrit_api_key
```

## Usage
-----
To use the MultiPDF Chat App, follow these steps:

1. Ensure that you have installed the required dependencies and added the OpenAI API key to the `.env` file.

2. Run the `main.py` file using the Streamlit CLI. Execute the following command:
   ```
   streamlit run app.py
   ```

3. The application will launch in your default web browser, displaying the user interface.

4. Load multiple PDF documents into the app by following the provided instructions.

5. Ask questions in natural language about the loaded PDFs using the chat interface.

## screenshots
-------
category of question = explainatory
<img width="1097" alt="image" src="https://github.com/shivam-gupta12/Langchain-pdf-browser/assets/109721120/6f22109a-bcce-4860-8592-f2c646140eee">

category of question = one word answer
<img width="1097" alt="image" src="https://github.com/shivam-gupta12/Langchain-pdf-browser/assets/109721120/300496e9-fc52-46d5-bd6a-d1ad879caa15">

category of question = true/false
<img width="1097" alt="image" src="https://github.com/shivam-gupta12/Langchain-pdf-browser/assets/109721120/dc3ccbd8-ab55-4cde-9376-fe8f69c4266d">

category of question = MCQ (multiple choices)
<img width="1097" alt="image" src="https://github.com/shivam-gupta12/Langchain-pdf-browser/assets/109721120/73cadbe3-5f3e-4b69-aa90-5a5972afb5b6">
