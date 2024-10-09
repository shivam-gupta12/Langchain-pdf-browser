import streamlit as st
import PyPDF2
import os
import google.generativeai as genai

# Configure API Key for Google Generative AI
genai.configure(api_key=os.environ["API_KEY"])

# Configuration for file upload
UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'pdf'}

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def extract_text_from_pdf(pdf_path):
    text = ""
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        for page in reader.pages:
            text += page.extract_text() + "\n"
    return text

def ask_question_with_genai(question, context):
    model = genai.GenerativeModel("gemini-1.5-flash")
    prompt = f"The following is a document:\n{context}\n\nQ: {question}\nA:"
    response = model.generate_content(prompt)
    return response.text

def main():
    st.title("Chat with PDF")
    st.write("Upload a PDF and ask questions about its content.")

    uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")

    if uploaded_file is not None:
        # Save the uploaded file
        filepath = os.path.join(UPLOAD_FOLDER, uploaded_file.name)
        with open(filepath, 'wb') as f:
            f.write(uploaded_file.getbuffer())

        # Extract text from PDF
        text = extract_text_from_pdf(filepath)
        st.write("### Extracted Content:")
        st.text_area("PDF Content", text, height=300)

        # Ask questions
        question = st.text_input("Ask a question about the content:")
        if st.button("Get Answer"):
            if question:
                answer = ask_question_with_genai(question, text)
                st.write("### Answer:")
                st.write(answer)
            else:
                st.warning("Please enter a question.")

if __name__ == '__main__':
    main()
