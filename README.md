# 📄 Vectorless RAG System

A Retrieval-Augmented Generation (RAG) application that retrieves relevant document content **without using vector embeddings or a vector database**.

Instead of semantic vector search, this project uses **TF-IDF and BM25 ranking algorithms** to retrieve the most relevant document chunks before sending them to a Large Language Model (LLM) for answer generation.

---

## 🚀 Overview

Traditional RAG systems depend on:

- Embedding Models
- Vector Databases (FAISS, Pinecone, ChromaDB)

While they provide semantic search, they also increase infrastructure complexity and cost.

This project demonstrates a lightweight alternative called **Vectorless RAG**, where document retrieval is performed using classical Information Retrieval techniques.

The retrieved context is then provided to an LLM to generate accurate answers.

---

# ✨ Features

- 📄 Upload PDF documents
- 🔍 TF-IDF based retrieval
- 📚 BM25 ranking
- 🤖 LLM-powered answer generation
- ⚡ Fast retrieval without embeddings
- 💰 No Vector Database required
- 🌐 Simple Streamlit interface
- 📑 Context-aware responses

---

# 🏗️ Project Architecture

```
            PDF Document
                  │
                  ▼
         Text Extraction
                  │
                  ▼
         Text Chunking
                  │
                  ▼
       TF-IDF / BM25 Index
                  │
        User Question
                  │
                  ▼
      Relevant Chunk Retrieval
                  │
                  ▼
      Prompt Construction
                  │
                  ▼
         Large Language Model
                  │
                  ▼
            Final Answer
```

---

# 🛠️ Tech Stack

| Technology | Purpose |
|------------|----------|
| Python | Programming Language |
| Streamlit | Web Interface |
| LangChain | LLM Workflow |
| BM25 | Keyword Retrieval |
| TF-IDF | Text Similarity |
| Scikit-learn | TF-IDF Vectorizer |
| PyPDF | PDF Text Extraction |
| Google Gemini / Groq | LLM |
| NLTK | Text Processing |

---

# 📂 Project Structure

```
Vectorless-RAG/
│
├── app.py
├── rag.py
├── retriever.py
├── pdf_loader.py
├── requirements.txt
├── README.md
│
├── data/
│     └── sample.pdf
│
└── utils/
      ├── chunking.py
      ├── preprocessing.py
      └── prompts.py
```

---

# ⚙️ Installation

Clone the repository.

```bash
git clone https://github.com/Harsha-2232/Vectorless-RAG.git
```

Move into the project folder.

```bash
cd Vectorless-RAG
```

Install dependencies.

```bash
pip install -r requirements.txt
```

---

# 🔑 Environment Variables

Create a `.env` file.

```
GOOGLE_API_KEY=your_api_key
```

or

```
GROQ_API_KEY=your_api_key
```

---

# ▶️ Run the Application

```bash
streamlit run app.py
```

---

# 📌 Workflow

### Step 1

Upload a PDF.

↓

### Step 2

Extract text from the document.

↓

### Step 3

Split text into chunks.

↓

### Step 4

Build TF-IDF and BM25 indexes.

↓

### Step 5

User asks a question.

↓

### Step 6

Retrieve the most relevant chunks.

↓

### Step 7

Send retrieved context + question to the LLM.

↓

### Step 8

Generate the final answer.

---

# 💡 Why Vectorless RAG?

Compared to traditional RAG:

| Traditional RAG | Vectorless RAG |
|-----------------|----------------|
| Requires embeddings | No embeddings |
| Needs Vector DB | No Vector DB |
| Higher infrastructure cost | Lightweight |
| Better semantic search | Strong keyword search |
| Slower indexing | Faster indexing |
| More setup | Easy to deploy |

---

# 📊 Retrieval Methods

## TF-IDF

- Calculates term importance
- Fast keyword matching
- Effective for smaller document collections

## BM25

- Advanced ranking algorithm
- Better relevance scoring
- Widely used in search engines

---

# 🎯 Example Query

**Question**

```
What is Retrieval-Augmented Generation?
```

Retrieved Context

```
Retrieval-Augmented Generation combines external document retrieval with LLM reasoning...
```

Generated Answer

```
Retrieval-Augmented Generation (RAG) is an AI architecture that retrieves relevant information from external documents before generating an answer, reducing hallucinations and improving response accuracy.
```

---

# 📈 Advantages

- Lightweight
- Fast indexing
- No embedding models
- No vector databases
- Easy deployment
- Cost-effective
- Good for small and medium document collections

---

# ⚠️ Limitations

- Keyword-based retrieval
- Less effective for semantic queries
- Performance decreases with very large datasets
- Cannot understand synonyms as effectively as embedding-based search

---

# 🔮 Future Improvements

- Hybrid Search (BM25 + Embeddings)
- Cross Encoder Re-ranking
- OCR support for scanned PDFs
- Multi-document retrieval
- Citation generation
- Chat history memory
- Metadata filtering

---

# 📚 Skills Demonstrated

- Retrieval-Augmented Generation (RAG)
- Information Retrieval
- BM25
- TF-IDF
- LangChain
- Prompt Engineering
- Large Language Models
- PDF Processing
- Python
- Streamlit
- NLP
- Document Chunking

---

# 📷 Demo

Add screenshots here.

```
screenshots/
    home.png
    upload.png
    answer.png
```

---

# 🤝 Contributing

Contributions are welcome!

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Open a Pull Request

---

# 📄 License

This project is licensed under the MIT License.

---

# 👩‍💻 Author

**Harsha S**

AI & Machine Learning Engineer

- GitHub: https://github.com/Harsha-2232
- LinkedIn: https://www.linkedin.com/in/harsha-s-7b2720285/
- Medium: https://medium.com/@harshadevu2232
