# Intelligent HR Assistant: GraphRAG-based Document QA 📄🕸️

This project is a **Graph-based Retrieval-Augmented Generation (GraphRAG)** system designed to help employees query internal HR policy documents. Unlike standard RAG, which relies solely on text similarity, this system uses a **Knowledge Graph** to understand the complex connections between different corporate policies, roles, and regulations.

## 🌟 Key Features
* **Graph-Based Ingestion:** Transforms PDF text into a structured Knowledge Graph of entities and relationships.
* **Semantic & Relational Search:** Combines vector similarity with graph traversal to answer complex, multi-hop questions.
* **Source Attribution:** Provides clear citations, linking answers back to specific documents and page numbers.
* **Advanced Reasoning:** Uses the relationships in **Neo4j** to provide more contextually accurate answers than standard vector-only approaches.

## 🛠️ Tech Stack
* **Language:** Python 3.x 🐍
* **Orchestration:** [LangChain](https://www.langchain.com/) 🦜🔗
* **Graph Database:** [Neo4j](https://neo4j.com/) 🕸️
* **LLM:** OpenAI GPT-4 (Placeholder)

## 🚀 Getting Started

### Prerequisites
* Python 3.10+
* A Neo4j instance (AuraDB or local)
* An API key for your chosen LLM (stored in a `.env` file)

### Installation
1. Clone the repository:
   ```bash
   git clone [https://github.com/your-username/hr-document-ai.git](https://github.com/your-username/hr-document-ai.git)
   cd hr-document-ai