📌 Document-to-Vector DB RAG Chatbot
================================

ABOUT THE PROJECT
-----------------
With the rise of Generative AI, the role of a Data Engineer is evolving beyond
traditional ETL/ELT pipelines. Today, an important responsibility is preparing,
transforming, and serving internal company data to Large Language Models (LLMs)
in a reliable and scalable way.

Most publicly available GenAI tools such as ChatGPT or Gemini are trained only
on public data. While they can answer generic questions, they cannot answer
company-specific questions such as:

1) Changes in HR policy based on newly released internal PDFs
2) Revenue details of specific departments
3) Growth insights based on historical company performance

These questions can only be answered when an LLM has access to internal,
proprietary company data.

------------------------------------------------------------

🎯 PROJECT GOAL
------------
The goal of this project is to build a custom Retrieval-Augmented Generation
(RAG) pipeline that:

- Ingests unstructured documents (PDF, DOC, TXT)
- Converts them into vector embeddings
- Stores them in a vector database
- Powers a company-specific chatbot that answers queries strictly
  using indexed internal data

This approach ensures:
- Grounded, data-backed answers
- Reduced hallucinations
- Full control over company knowledge

------------------------------------------------------------

🧠 HOW RAG WORKS (HIGH LEVEL)
--------------------------
1) Company documents are ingested and processed
2) Text is chunked and converted into embeddings
3) Embeddings are stored in a vector database
4) User queries retrieve relevant document chunks
5) Retrieved context is passed to an LLM for answer generation

The LLM generates answers only from retrieved company data,
not from its general training knowledge.

![RAG Architecture](https://github.com/Sharmaaditya22/document-to-vector-db-rag-pipeline-chatbot/blob/ca3d687866a71f4c4c4dca75dcf5d70acbafe9f7/png_folder/RAG_flow.png)

------------------------------------------------------------

🏢 DUMMY COMPANY CONTEXT
---------------------
For demonstration purposes, this project uses dummy company data generated
using Gemini.

Company Name: Localhost 404 Ltd

This company does not exist in the real world. The chatbot simulates realistic
conversations and predictions using dummy internal data. The same pipeline
can be applied to real company data in production environments.

------------------------------------------------------------


🧩 HIGH LEVEL ARCHITECTURE
-----------------------
![Project Architecture](https://github.com/Sharmaaditya22/document-to-vector-db-rag-pipeline-chatbot/blob/ca3d687866a71f4c4c4dca75dcf5d70acbafe9f7/png_folder/RAG_project_HLD.png)

------------------------------------------------------------

🤖  MODELS USED
-----------
Generation Model : gpt-5-nano
Embedding Model  : text-embedding-3-small

At the time of development, these models provide a good balance
between cost efficiency and performance.

------------------------------------------------------------

🚀 HOW TO RUN THE PROJECT
---------------------

FIRST-TIME SETUP
----------------
1) (Optional) Create a virtual environment using uv
2) Install dependencies:
   uv pip install -r requirements.txt

3) Create an OpenAI API key from the OpenAI portal
   (minimum $10 balance required)

4) Add your API key in a .env file(refer .env.example file):
   OPENAI_API_KEY=your_api_key_here

5) Place company documents in the Company_pdf folder
   (sample PDFs are already provided and can use sample file for project testing)

6) Run the training script:
   python train_model.py

   - If using your own PDFs, update the pdf_path variable inside
     the train_model function in train_model.py

7) After successful execution, a vector database folder
   (e.g., companyDB) will be created

------------------------------------------------------------

SUBSEQUENT RUNS (After first time run direct run below steps for next runs skip above steps)
---------------
1) Activate the virtual environment (option if stepup eariler)
2) Start the Flask backend:
   python flask_backend.py

3) Open the application in a browser:
   http://127.0.0.1:5000/

4) Start chatting with the company-specific AI assistant

------------------------------------------------------------

💬 CHATBOT BEHAVIOR
----------------
- Answers only company-specific questions
- Responses are grounded in vector database retrieval
- Generic queries do not produce hallucinated answers

------------------------------------------------------------

📂 PROJECT STRUCTURE & FILE OVERVIEW
--------------------------------

1) RAG Practice Files
   - Files containing "RAG" in their name
   - Jupyter notebooks (.ipynb)
   - Used to understand and experiment with RAG components

2) train_model.py
   - Handles document ingestion
   - Generates embeddings
   - Creates and persists the vector database

3) flask_backend.py
   - Flask application
   - Receives user queries from frontend
   - Performs retrieval + generation
   - Returns grounded responses

4) templates/index.html
   - Frontend UI
   - Provides chat interface for the company assistant

------------------------------------------------------------

📸 SCREENSHOTS
-----------
Attach screenshots showing:
- User prompts
- Chatbot responses

![ScreenShot1](https://github.com/Sharmaaditya22/document-to-vector-db-rag-pipeline-chatbot/blob/b58b21c6275581b37c5998a8ad499836ef308964/png_folder/Chatbot_ouput.png)
![ScreenShot2](https://github.com/Sharmaaditya22/document-to-vector-db-rag-pipeline-chatbot/blob/b58b21c6275581b37c5998a8ad499836ef308964/png_folder/Chatbot_ouput1.png)

------------------------------------------------------------

🧑‍💻 TARGET AUDIENCE
---------------
- Data Engineers
- Machine Learning Engineers
- Backend Engineers
- Anyone interested in RAG pipelines

------------------------------------------------------------

KEY TAKEAWAYS
-------------
- Demonstrates real-world RAG architecture
- Focuses on data engineering responsibilities
- Emphasizes grounded and controlled AI responses
- Easily extensible to enterprise environments
