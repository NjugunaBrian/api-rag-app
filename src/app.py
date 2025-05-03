from fastapi import FastAPI, BackgroundTasks
from pydantic import BaseModel
import uvicorn
import os
from modules.document_loader import DocumentProcessor
from modules.embedder import DocumentEmbedder
from modules.retriever import DocumentRetriever
from modules.generator import ResponseGenerator
import config


app = FastAPI(title="RAG API")

#global variables
generator = None

class Query(BaseModel):
    text: str

class RebuildRequest(BaseModel):
    rebuild: bool = True

def setup_rag_system(rebuild_index=False):
    """Setup the RAG system"""
    document_processor = DocumentProcessor() 
    embedder = DocumentEmbedder()

    #create or load vector store
    if rebuild_index or not os.path.exists(config.VECTOR_DB_PATH):
        print("Building document index...")
        chunks = document_processor.process_documents()
        vector_store = embedder.create_vector_store(chunks)
    else:
        print("Loading existing document index...")
        vector_store = embedder.load_vector_store()

    #setup retriever and generator
    retriever = DocumentRetriever(vector_store).setup_retriever()
    generator = ResponseGenerator(retriever)

    return generator

@app.on_event("startup")
async def startup_event():
    global generator
    generator = setup_rag_system()

@app.post("/query")
async def process_query(query: Query):
    global generator
    if not generator:
        return {"error": "RAG system not initialized"}
    
    result = generator.generate_response(query.text)
    return result

@app.post("/rebuild-index")
async def rebuild_index(request: RebuildRequest, background_tasks: BackgroundTasks):

    global generator
    def rebuild():
        global generator
        generator = setup_rag_system(rebuild_index=True)

    background_tasks.add_task(rebuild)
    return {"message": "Rebuilding index in background"}

@app.get("/healthcheck")
async def health_check():
    return {"status": "healthy"}

if __name__ == "__main__":
    # Run the app with uvicorn
    uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=True)
    # Note: In production, you might want to set `reload=False` and use a proper ASGI server like Daphne or Gunicorn.



