import os
import streamlit as st
import time
import asyncio
import sys
from dotenv import load_dotenv

# LangChain & Google Gemini
from langchain.chains import RetrievalQAWithSourcesChain
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import UnstructuredURLLoader
from langchain_community.vectorstores import FAISS
from langchain_google_genai import ChatGoogleGenerativeAI, GoogleGenerativeAIEmbeddings

# Ensure event loop policy for Windows (important for Streamlit + asyncio)
if sys.platform.startswith("win"):
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

try:
    asyncio.get_event_loop()
except RuntimeError:
    asyncio.set_event_loop(asyncio.new_event_loop())

# Load .env variables
load_dotenv()

# Streamlit UI
st.title("News Research Tool 📈")
st.sidebar.title("News Article URLs")

urls = []
for i in range(3):
    url = st.sidebar.text_input(f"URL {i+1}")
    if url:   # only append non-empty URLs
        urls.append(url)

process_url_clicked = st.sidebar.button("Process URLs")
faiss_path = "faiss_index_gemini"

main_placeholder = st.empty()

# Gemini LLM (use a valid available model)
llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0.9)

if process_url_clicked and urls:
    # Load data
    loader = UnstructuredURLLoader(urls=urls)
    main_placeholder.text("Data Loading...Started...✅✅✅")
    data = loader.load()

    # Split data
    text_splitter = RecursiveCharacterTextSplitter(
        separators=['\n\n', '\n', '.', ','],
        chunk_size=1000
    )
    main_placeholder.text("Text Splitter...Started...✅✅✅")
    docs = text_splitter.split_documents(data)

    # Create embeddings and save to FAISS index
    embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
    vectorstore_gemini = FAISS.from_documents(docs, embeddings)
    main_placeholder.text("Embedding Vector Started Building...✅✅✅")
    time.sleep(2)

    # Save FAISS index properly (creates a folder)
    vectorstore_gemini.save_local(faiss_path)

# Input for questions
# Input for questions
query = st.text_input("Question: ")
if query:
    if os.path.isdir(faiss_path):   # check for directory instead of file
        embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
        vectorstore = FAISS.load_local(
            faiss_path,
            embeddings,
            allow_dangerous_deserialization=True  # required in new LangChain versions
        )

        chain = RetrievalQAWithSourcesChain.from_llm(
            llm=llm, retriever=vectorstore.as_retriever()
        )
        result = chain.invoke({"question": query})

        st.header("Answer")
        st.write(result["answer"])

        sources = result.get("sources", "")
        if sources:
            st.subheader("Sources:")
            for source in sources.split("\n"):
                if source.strip():
                    st.write(source)
