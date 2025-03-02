import streamlit as st
import logging
from langchain_community.document_loaders import PDFPlumberLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.vectorstores import InMemoryVectorStore
from langchain_ollama import OllamaEmbeddings
from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama.llms import OllamaLLM

# Configure logging
logging.basicConfig(level=logging.ERROR)

# Custom CSS for Professional Design
st.markdown("""
    <style>
    .stApp {
        background-color: #0E1117;
        color: #FFFFFF;
        font-family: 'Arial', sans-serif;
    }
    h1 {
        color: #00FFAA;
        text-align: center;
        font-size: 2.5rem;
        margin-bottom: 10px;
    }
    h3 {
        color: #00FFAA;
        text-align: center;
        font-size: 1.2rem;
        margin-top: 5px;
    }
    hr {
        border: 1px solid #00FFAA;
        margin: 20px 0;
    }
    .stFileUploader {
        background-color: #1E1E1E;
        border: 2px dashed #00FFAA;
        border-radius: 10px;
        padding: 20px;
        text-align: center;
        transition: all 0.3s ease;
    }
    .stFileUploader:hover {
        background-color: #2A2A2A;
        border-color: #FFFFFF;
    }
    .stChatInput input {
        background-color: #1E1E1E !important;
        color: #FFFFFF !important;
        border: 1px solid #3A3A3A !important;
        border-radius: 5px;
        padding: 10px;
        font-size: 1rem;
    }
    .stChatMessage[data-testid="stChatMessage"]:nth-child(odd) {
        background-color: #1E1E1E !important;
        border: 1px solid #3A3A3A !important;
        color: #E0E0E0 !important;
        border-radius: 10px;
        padding: 15px;
        margin: 10px 0;
        font-size: 1rem;
    }
    .stChatMessage[data-testid="stChatMessage"]:nth-child(even) {
        background-color: #2A2A2A !important;
        border: 1px solid #404040 !important;
        color: #F0F0F0 !important;
        border-radius: 10px;
        padding: 15px;
        margin: 10px 0;
        font-size: 1rem;
    }
    .stChatMessage .avatar {
        background-color: #00FFAA !important;
        color: #000000 !important;
        border-radius: 50%;
        width: 30px;
        height: 30px;
        display: flex;
        align-items: center;
        justify-content: center;
        font-weight: bold;
    }
    .stProgress > div > div > div {
        background-color: #00FFAA !important;
    }
    </style>
    """, unsafe_allow_html=True)

PROMPT_TEMPLATE = """
You are an expert research assistant. Use the provided context to answer the query. 
If unsure, state that you don't know. Be concise and factual (max 3 sentences).

Query: {user_query} 

Answer:
"""
PDF_STORAGE_PATH = 'document_store/pdfs/'
EMBEDDING_MODEL = OllamaEmbeddings(model="deepseek-r1:1.5b")
DOCUMENT_VECTOR_DB = InMemoryVectorStore(EMBEDDING_MODEL)
LANGUAGE_MODEL = OllamaLLM(model="deepseek-r1:1.5b")

def save_uploaded_file(uploaded_file):
    try:
        file_path = PDF_STORAGE_PATH + uploaded_file.name
        with open(file_path, "wb") as file:
            file.write(uploaded_file.getbuffer())
        return file_path
    except Exception as e:
        logging.error(f"Error saving file: {e}")
        st.error("An error occurred while saving the file. Please try again.")
        return None

def load_pdf_documents(file_path):
    try:
        document_loader = PDFPlumberLoader(file_path)
        return document_loader.load()
    except Exception as e:
        logging.error(f"Error loading PDF: {e}")
        st.error("An error occurred while loading the PDF. Please check the file format.")
        return []

def chunk_documents(raw_documents):
    try:
        text_processor = RecursiveCharacterTextSplitter(
            chunk_size=1000,
            chunk_overlap=200,
            add_start_index=True
        )
        return text_processor.split_documents(raw_documents)
    except Exception as e:
        logging.error(f"Error chunking documents: {e}")
        st.error("An error occurred while processing the document chunks.")
        return []

def index_documents(document_chunks):
    try:
        DOCUMENT_VECTOR_DB.add_documents(document_chunks)
    except Exception as e:
        logging.error(f"Error indexing documents: {e}")
        st.error("An error occurred while indexing the document.")

def find_related_documents(query):
    try:
        return DOCUMENT_VECTOR_DB.similarity_search(query)
    except Exception as e:
        logging.error(f"Error finding related documents: {e}")
        st.error("An error occurred while searching for related documents.")
        return []
    
def generate_answer(user_query, context_documents):
    try:
        if not context_documents:
            return "I couldn't find any relevant information in the document."
        
        context_text = "\n\n".join([doc.page_content for doc in context_documents])
        conversation_prompt = ChatPromptTemplate.from_template(PROMPT_TEMPLATE)
        response_chain = conversation_prompt | LANGUAGE_MODEL
        raw_response = response_chain.invoke({"user_query": user_query, "document_context": context_text})
        
        # Extract only the final answer after "Final Answer:"
        final_answer = raw_response.strip().split("Final Answer:")[-1].strip()
        return final_answer
    except Exception as e:
        logging.error(f"Error generating answer: {e}")
        return "An error occurred while generating the response."

# UI Configuration
st.title("📘 DocuMind AI")
st.markdown("### Your Intelligent Document Assistant")
st.markdown("---")

# Initialize Session State
if "document_processed" not in st.session_state:
    st.session_state.document_processed = False
if "uploaded_pdf_path" not in st.session_state:
    st.session_state.uploaded_pdf_path = None



uploaded_pdf = st.file_uploader(
    "Upload Research Document (PDF)",
    type="pdf",
    help="Select a PDF document for analysis",
    accept_multiple_files=False
)

if uploaded_pdf:
    try:
        # Progress Bar for Upload
        progress_bar = st.progress(0)
        status_text = st.empty()
        status_text.text("Uploading and processing your document...")

        # Simulate progress for saving the file
        saved_path = None
        for percent_complete in range(25, 101, 25):
            progress_bar.progress(percent_complete)
            # import time; time.sleep(5)
            status_text.text(f"Uploading and processing your document... {percent_complete}%")
            # Simulate some processing delay
            if percent_complete == 100:
                saved_path = save_uploaded_file(uploaded_pdf)

        # Finalize progress
        progress_bar.progress(100)
        #status_text.text("Document uploaded successfully!")
        import time; time.sleep(5)

        if saved_path:
            st.session_state.uploaded_pdf_path = saved_path
            st.success("✅ Document uploaded successfully!")
            
            # Load and process the PDF
            raw_docs = load_pdf_documents(saved_path)
            if raw_docs:
                processed_chunks = chunk_documents(raw_docs)
                if processed_chunks:
                    index_documents(processed_chunks)
                    st.session_state.document_processed = True
                    import time; time.sleep(3);
                    st.success("✅ Document processed successfully! Ask your questions below.")
        else:
            st.error("Failed to save the uploaded file.")
    except Exception as e:
        st.error(f"An error occurred while uploading or processing the document: {str(e)}")

# Chat Interface
if st.session_state.document_processed:
    user_input = st.chat_input("Enter your question about the document...")
    if user_input:
        with st.chat_message("user"):
            st.write(user_input)

        try:
            # Progress Bar for Analysis
            progress_bar = st.progress(0)
            status_text = st.empty()
            status_text.text("Analyzing document...")

            for percent_complete in range(10, 101, 35):
                progress_bar.progress(percent_complete)
                status_text.text(f"Analyzing document... {percent_complete}%")

            # Find relevant documents and generate an answer
            relevant_docs = find_related_documents(user_input)
            if not relevant_docs:
                ai_response = "I couldn't find any relevant information in the document."
            else:
                ai_response = generate_answer(user_input, relevant_docs)

            # Finalize progress
            progress_bar.progress(100)
            status_text.text("Analysis complete!")
        except Exception as e:
            ai_response = f"An error occurred while generating the response: {str(e)}"

        with st.chat_message("Assistant", avatar="🤖"):
            st.write(ai_response)