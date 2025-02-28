# AI-Powered News Research Tool

This project is an **AI-driven news research tool** that combines document processing, vector similarity search, and question-answering capabilities to extract insights from financial news articles.

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

## FAISS Index Handling

The FAISS index, which stores the article embeddings, is **not included in this repository**. On the first run, the system will automatically:

- Download and process the articles.
- Generate embeddings using OpenAI's API.
- Build a new FAISS index from scratch.
- Save the index locally (typically as `faiss_store_openai.pkl`).

This ensures the latest articles are processed, but may result in **slower startup times** on the initial run.

To speed up subsequent runs, the FAISS index file can be retained locally, but it is excluded from version control.

## Sample Use Case

Example URLs:

- [Tesla stock jumps as company beats delivery estimates](https://www.cnbc.com/2024/02/15/tesla-stock-jumps-as-company-beats-delivery-estimates.html)
- [Federal Reserve signals no rate cuts until inflation slows](https://www.bloomberg.com/news/articles/2024-02-12/federal-reserve-signals-no-rate-cuts-until-inflation-slows)
- [Apple announces record revenue driven by strong iPhone sales](https://www.wsj.com/articles/apple-announces-record-revenue-driven-by-strong-iphone-sales-567abc)

Example query:

> *What is the Federal Reserve’s latest stance on interest rates?*

The system retrieves relevant excerpts from the articles and generates a response.


## Acknowledgement

This project was created by following and extending concepts from the [Codebasics LangChain tutorial](https://github.com/codebasics/langchain). 

## Quick Start

Explore the code in `main.py` to see how the different components work together to power this **AI-based news research tool**.
