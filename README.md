# 🧠 RAG (Retrieval-Augmented Generation) Application

This project is a simple RAG (Retrieval-Augmented Generation) pipeline that allows you to query over your own documents using a local vector database and an LLM-powered response generator.

---

## 📦 Installation

1. Clone the repository:

```bash
git clone https://github.com/NjugunaBrian/api-rag-app.git
cd api-rag-app
```

2. Install Requirements:

```bash
pip install -r requirements.txt
```

## :file_folder: Adding Your Documents

Add your source documents to the data/ directory. The system supports the following file formats:

.txt (Plain text)

.pdf (PDF documents)

.docx (Word documents)

.md (Markdown files)

Example:
```bash 
rag-app/
  |- data/
    |-- document1.txt
    |-- slides.pdf
    |-- report.docx
```    
<br/>

## :rocket: Usage
### :green_circle: Run the API Server
```bash
python app.py
```
Access the API at http://localhost:8000
Swagger UI at http://localhost:8000/docs


## :hammer_and_wrench: Project Structure
```bash
rag-app/
   |- app.py              # Main entry point
   |- config.py           # Configuration settings
   |- requirements.txt    # Python dependencies
   |- data/               # Add your documents here
   |- embeddings/         # Stores vector embeddings
   |- modules/            # Core logic for document loading, embedding, retrieval, generation
```
<br/>

## :mailbox_with_mail: License
MIT License – feel free to use and adapt!



