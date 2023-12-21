# app.py
from flask import Flask, render_template, request, jsonify
from llama_index import SimpleDirectoryReader, Document, ServiceContext, VectorStoreIndex,  StorageContext
from werkzeug.utils import secure_filename
from llama_index.llms import OpenAI
from llama_index import load_index_from_storage
import openai
import os
from flask_cors import CORS
import json


app = Flask(__name__)
CORS(app)


# Create a variable to store the uploaded file path
uploaded_file_path = ""
documents = None
document = None
index_instance = None


def build_basicRAG():
    global documents, document, index

    # Check if a document has been uploaded
    if not uploaded_file_path or not os.path.isfile(uploaded_file_path):
        return jsonify({'error': 'Please upload a document first'})

    # Load the document
    documents = SimpleDirectoryReader(input_files=[uploaded_file_path]).load_data()
    document = Document(text="\n\n".join([doc.text for doc in documents]))

    # Build the sentence window index
    index=build_basicRAGhelper('index')
    
    

    return jsonify({'success': True})



def build_basicRAGhelper(save_dir):

    sentence_context = ServiceContext.from_defaults(
        llm=OpenAI(model="gpt-3.5-turbo", temperature=0.1),
        embed_model="local:BAAI/bge-small-en-v1.5",
    )

    if not os.path.exists(save_dir):
        index = VectorStoreIndex.from_documents([document], service_context=sentence_context)
        index.storage_context.persist(persist_dir=save_dir)
    else:
        index = load_index_from_storage(
            StorageContext.from_defaults(persist_dir=save_dir),
            service_context=sentence_context
        )

    return index

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload_document', methods=['POST'])
def upload_document():
    global uploaded_file_path, documents, document, index

    # Check if 'file' is in request.files
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'})

    file = request.files['file']

    # Check if the file is empty
    if file.filename == '':
        return jsonify({'error': 'No selected file'})

    # Save the file to the current working directory
    upload_folder = os.getcwd()  # Get the current working directory
    uploaded_file_path = os.path.join(upload_folder, secure_filename(file.filename))
    file.save(uploaded_file_path) 
    
    build_basicRAG()


    return jsonify({'success': True})




@app.route('/generate_response', methods=['POST'])
def generate_response():
    global uploaded_file_path, documents, document, index

    # Check if a document has been uploaded
    if not uploaded_file_path or not os.path.isfile(uploaded_file_path):
        return jsonify({'error': 'Please upload a document first'})

    question = request.form.get('question')

    # Get the query engine
    query_engine = index.as_query_engine()

    # Query for the response

    response = query_engine.query(question)
    
    
    return render_template('results.html',question=question, response=response)




if __name__ == '__main__':
    app.run(debug=True)

