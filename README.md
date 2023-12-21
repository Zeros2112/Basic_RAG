# Basic RAG System with Flask and Sentence Window Indexing
This repository contains code for building a basic Retrieval-Augmented Generation (RAG) system using Flask and Sentence Window Indexing.

## Overview
The system allows users to upload a document, build a Sentence Window Index, and query the system for responses. It utilizes Flask for the web interface and integrates the OpenAI language model for document processing.

## Components
1. Flask Web Interface
A web interface created using Flask for user interaction.
Users can upload documents, build a Sentence Window Index, and generate responses.

2. Sentence Window Indexing
Implements a basic Sentence Window Index for efficient document retrieval.
Utilizes the OpenAI language model for document processing.

## Usage
### Prerequisites
* Python 3.x
* Pip package manager

### Installation
1. Clone the repository:

```
git clone https://github.com/Zeros2112/basic-rag-system.git
cd basic-rag-system
```

2. Install dependencies:

```
pip install -r requirements.txt
```

## Running the Application

Run the Flask application:

```
python app.py
```

2. Access the web interface:

Open your browser and navigate to http://localhost:5000.

## Web Interface
* Home: Displays the main page with options to upload a document and generate responses.

* Upload Document: Allows users to upload documents for processing.

* Generate Response: Accepts user queries and provides responses based on the Sentence Window Index.

## Contributors

Nguyen Gia Hy

## Acknowledgements

Special thanks to OpenAI for providing a powerful language model.
Flask for simplifying web development.

## License
This project is licensed under the MIT License - see the LICENSE file for details.
