# AI-Powered News & Web Research Tool

This project is an **AI-driven news and web research tool** that combines document processing, vector similarity search, and question-answering capabilities to extract insights from online news articles or web content.

## Overview

- **Fetch article content** from URLs and process them into embeddings using **OpenAI embeddings**.
- **Store and index embeddings** using **FAISS** for efficient similarity search.
- **Ask questions about the articles** using an LLM (ChatGPT), with responses grounded in the indexed content.
- **Interactive interface** built with **Streamlit**, enabling users to input URLs, process content, and query the system.

## Key Technologies

- 🧠 **LangChain** - Document loading, text splitting, and retrieval pipeline design.
- 🧠 **OpenAI API** - Embedding generation and LLM-powered question answering.
- 🔍 **FAISS** - Vector similarity search for fast and accurate retrieval.
- 🌐 **Streamlit** - Building interactive AI-powered web applications.
- 🐍 **Python** - Full orchestration of the data pipeline, vector processing, and LLM interaction.

## Improvements Over the Original Version

This project is based on concepts from the **Codebasics LangChain tutorial**, but it includes several improvements and custom features:

✅ **Pre-configured Quick Prompts:**  
   - Users can choose from common research questions without typing, improving usability.  

✅ **UI Test Mode (No OpenAI Key Required):**  
   - Allows users to preview and test the interface without needing an OpenAI API key.  
   - Simulates processing and retrieval steps when the API key is missing.  

✅ **Enhanced Error Handling:**  
   - Improved input validation (e.g., checking valid URLs before processing).  
   - Displays detailed error messages for debugging.  

✅ **Cleaner & More Dynamic UI:**  
   - Sidebar now allows users to set the number of URLs dynamically.  
   - More structured layout with intuitive controls.  

✅ **Optimized FAISS Index Handling:**  
   - Avoids overwriting the FAISS index unnecessarily.  
   - Provides better UI feedback during processing.  

## Future Enhancements (In the Pipeline)

The following improvements are planned to make this tool even more robust and feature-rich:

🚀 **Support for Text File Uploads:**  
   - Users will be able to upload `.txt` files, allowing research on offline documents.  

🚀 **Session Management for FAISS Indexes:**  
   - Users will be able to **save and reload** different research sessions.  
   - FAISS index files will be timestamped (e.g., `faiss_2025-02-28.pkl`).  

🚀 **Automatic Summarization & Thematic Tagging:**  
   - The tool will **auto-generate summaries** for processed articles.  
   - It will detect key topics (e.g., "Finance", "Technology", "Politics") for easier filtering.  

🚀 **Hybrid Search (Keyword + Vector Search):**  
   - Combines **keyword-based filtering** with FAISS similarity search for **better retrieval**.  

🚀 **Multilingual Processing Support:**  
   - The system will detect **article language** and allow querying across **multiple languages**.  

🚀 **Automatic URL Scraping for Related Articles:**  
   - If a user inputs a URL, the system will (optionally) suggest and fetch **related articles** from the same source.  

## FAISS Index Handling

The FAISS index, which stores the article embeddings, is **not included in this repository**. On the first run, the system will automatically:

- Download and process the articles.
- Generate embeddings using OpenAI's API.
- Build a new FAISS index from scratch.
- Save the index locally (typically as `faiss_store_openai.pkl`).

This ensures the latest articles are processed, but may result in **slower startup times** on the initial run.

To speed up subsequent runs, the FAISS index file can be retained locally, but it is excluded from version control.

## How to Use

1. **Enter Article URLs**  
   Open the Streamlit app and enter one or more URLs pointing to any online articles or webpages you want to analyze.

2. **Process the Articles**  
   Click the **Process URLs** button to load, split, and process the articles into embeddings. The system will store these embeddings in a FAISS index.

3. **Ask Questions**  
   Once processing is complete, you can enter questions such as:
   > What are the key points mentioned in the articles?

   The system will retrieve relevant information and provide an answer.

4. **Repeat for New Articles**  
   You can continue adding new URLs or clear the previous data to process a fresh batch of articles.

## UI Screenshot

Below is a screenshot of the application interface:

![UI Screenshot](./ui_screenshot.png)

> ⚠️ Be sure to save your screenshot as `ui_screenshot.png` in the same folder as this `README.md` so it displays correctly on GitHub.

## Acknowledgement

This project was created by following and extending concepts from the [Codebasics LangChain tutorial](https://github.com/codebasics/langchain). 

## Quick Start

Explore the code in `main.py` to see how the different components work together to power this **AI-based news research tool**.
