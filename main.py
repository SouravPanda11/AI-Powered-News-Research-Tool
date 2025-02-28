import os
import streamlit as st
import pickle
import time
from dotenv import load_dotenv
from langchain import OpenAI
from langchain.chains import RetrievalQAWithSourcesChain
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.document_loaders import UnstructuredURLLoader
from langchain.embeddings import OpenAIEmbeddings

# Load environment variables
load_dotenv()

# Check for OpenAI API Key
openai_api_key = os.getenv("OPENAI_API_KEY")
ui_test_mode = False

if not openai_api_key:
    st.sidebar.warning("⚠️ OpenAI API key not found. Running in **UI Test Mode**. Embedding & QA features will be simulated.")
    ui_test_mode = True

# App title and sidebar configuration
st.title("News Research Tool 📰")
st.sidebar.title("Input URLs")

# Section for URL input
num_urls = st.sidebar.number_input("Number of URLs", min_value=1, max_value=10, value=3)

urls = []
for i in range(num_urls):
    url = st.sidebar.text_input(f"URL {i+1}")
    urls.append(url.strip())

# Process button
process_url_clicked = st.sidebar.button("Process URLs")

# FAISS index file path
file_path = "faiss_store_openai.pkl"

# Placeholder for showing progress messages
main_placeholder = st.empty()

# Initialize LLM if available
llm = None
if not ui_test_mode:
    llm = OpenAI(temperature=0.9, max_tokens=500)

def is_valid_url(url):
    """Basic URL validation."""
    return url.startswith("http")

if process_url_clicked:
    # Collect valid URLs
    valid_urls = [url for url in urls if is_valid_url(url)]

    if not valid_urls:
        st.sidebar.error("Please enter at least one valid URL.")
    else:
        if ui_test_mode:
            st.success(f"✅ Processed {len(valid_urls)} URL(s). (UI Test Mode — No embeddings generated)")
        else:
            try:
                # Load documents from URLs
                loader = UnstructuredURLLoader(urls=valid_urls)
                main_placeholder.text("Loading data from URLs... ✅")
                data = loader.load()

                # Split data into chunks
                text_splitter = RecursiveCharacterTextSplitter(
                    separators=['\n\n', '\n', '.', ','],
                    chunk_size=1000
                )
                main_placeholder.text("Splitting documents into chunks... ✅")
                docs = text_splitter.split_documents(data)

                # Create embeddings and FAISS index
                embeddings = OpenAIEmbeddings()
                vectorstore_openai = FAISS.from_documents(docs, embeddings)
                main_placeholder.text("Building FAISS index with embeddings... ✅")
                time.sleep(2)

                # Save FAISS index to file
                with open(file_path, "wb") as f:
                    pickle.dump(vectorstore_openai, f)

                st.sidebar.success(f"Processed {len(docs)} chunks from {len(valid_urls)} URL(s).")

            except Exception as e:
                st.sidebar.error(f"Error processing documents: {str(e)}")

# Pre-configured prompt buttons
st.sidebar.subheader("Quick Prompts")
predefined_questions = [
    "What are the key takeaways from the articles?",
    "Summarize the main events covered.",
    "Are there any risks or warnings mentioned?",
    "What companies or organizations are mentioned?",
    "Provide a sentiment summary (positive/negative)."
]
selected_question = st.sidebar.selectbox("Choose a predefined question:", [""] + predefined_questions)

# User query input
query = main_placeholder.text_input("Ask your own question:")

# Use pre-configured question if no manual query is entered
if selected_question and not query:
    query = selected_question

if query:
    if ui_test_mode:
        st.info("ℹ️ UI Test Mode — No actual LLM call will be made.")
        st.write(f"Sample response for: **{query}**")
        st.write("This is a placeholder response since OpenAI key is not available.")
    elif not os.path.exists(file_path):
        st.error("No processed documents found. Please process URLs first.")
    else:
        try:
            with open(file_path, "rb") as f:
                vectorstore = pickle.load(f)

            chain = RetrievalQAWithSourcesChain.from_llm(
                llm=llm,
                retriever=vectorstore.as_retriever()
            )

            result = chain({"question": query}, return_only_outputs=True)

            st.header("Answer")
            st.write(result["answer"])

            sources = result.get("sources", "")
            if sources:
                st.subheader("Sources:")
                for source in sources.split("\n"):
                    if source.strip():
                        st.write(f"- {source}")
        except Exception as e:
            st.error(f"Failed to retrieve answer: {str(e)}")
