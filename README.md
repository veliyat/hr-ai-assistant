# Intelligent HR Assistant: RAG-based Document QA 📄🧠

This project is a **Retrieval-Augmented Generation (RAG)** system designed to help employees query internal HR policy documents. Instead of searching through long PDFs, users can ask questions in natural language and receive accurate answers backed by specific document citations.

## 🌟 Key Features
* **Automated Ingestion:** Processes complex PDF documents into manageable, semantic chunks.
* **Vector Search:** Utilizes vector embeddings to find the most relevant context for any query.
* **Source Attribution:** Every response includes the specific page number and document source to ensure transparency and trust.
* **Production-Ready Structure:** Modular Python architecture designed for scalability and maintainability.

## 🛠️ Tech Stack
* **Language:** Python 3.x 🐍
* **Orchestration:** [LangChain](https://www.langchain.com/) 🦜🔗
* **Vector Database:** ChromaDB (Placeholder)
* **LLM:** OpenAI GPT-4 (Placeholder)

## 🚀 Getting Started

### Prerequisites
* Python 3.10+
* An API key for your chosen LLM (stored in a `.env` file)

### Installation
1. Clone the repository:
   ```bash
   git clone [https://github.com/your-username/hr-document-ai.git](https://github.com/your-username/hr-document-ai.git)
   cd hr-document-ai