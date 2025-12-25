import os
from flask import Flask, request, jsonify
from flask_cors import CORS
from dotenv import load_dotenv
from loguru import logger
from langchain_openai import ChatOpenAI 
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import Chroma
from flask import render_template

load_dotenv()

app = Flask(__name__)
CORS(app)  # Enable CORS for frontend communication

# Initialize models globally
embeddings_model = OpenAIEmbeddings(model="text-embedding-3-small")
llm = ChatOpenAI(model="gpt-5-nano", temperature=0)  # Changed from gpt-5-nano to gpt-4

# Load vector store
logger.info('Loading persistent vector store')
vectorstore_persist = Chroma(
    persist_directory='./CompanyDB/',
    embedding_function=embeddings_model
)
logger.info('Vector store loaded successfully')

@app.route("/")
def home():
    return render_template("index.html")

@app.route('/api/chat', methods=['POST'])
def chat():
    try:
        data = request.json
        user_query = data.get('message', '')
        
        if not user_query:
            return jsonify({'error': 'No message provided'}), 400
        
        logger.info(f'Received query: {user_query}')
        
        # Query the vector store
        logger.info('Querying the vector store')
        context_docs = vectorstore_persist.similarity_search(user_query, k=3)
        context = "\n\n".join([doc.page_content for doc in context_docs])
        logger.info('Query complete')
        
        # Create prompt with context
        prompt = f"""Based on the following context about the company, please answer the question.
        
Context:
{context}

Question: {user_query}

Answer:"""
        
        # Invoke LLM
        logger.info('Invoking LLM with context')
        response = llm.invoke(prompt)
        logger.info('LLM response received')
        
        return jsonify({
            'response': response.content,
            'success': True
        })
        
    except Exception as e:
        logger.error(f'Error processing request: {str(e)}')
        return jsonify({
            'error': str(e),
            'success': False
        }), 500

@app.route('/api/health', methods=['GET'])
def health():
    return jsonify({'status': 'healthy', 'message': 'API is running'})

if __name__ == '__main__':
    app.run(debug=True, port=5000)