# Research_paper_summarization_MohanKrishna

The **Research Paper Summarizer** is a web application that allows users to search, fetch, and summarize research papers. It helps users to:
- Search for research papers based on topics.
- Upload PDF files of papers.
- Fetch papers using URLs or DOIs.
- Generate text summaries of papers.
- Synthesize summaries from multiple papers into one.
- Convert summaries into audio podcasts.

This project is built using **Flask** for the web framework, along with several Python libraries for natural language processing and text-to-speech conversion.

## Features

- **Paper Search**: Allows users to search for papers based on a given topic (e.g., AI, NLP).
- **DOI-based Fetching**: Retrieve paper metadata and summary using DOI.
- **URL-based Fetching**: Fetch paper content directly from a provided URL.
- **PDF Upload**: Users can upload a PDF of a research paper, which is then processed to extract its summary.
- **Cross-paper Synthesis**: Combines multiple paper summaries into one synthesized summary.
- **Text-to-Speech**: Converts the generated summaries into audio podcasts for listening.

## System Architecture

The system is designed using a **Modular Architecture**, where different components of the application handle different tasks. Below are the key components:

- **Frontend (Flask App)**: The user interface for searching, uploading, and viewing the results.
- **Topic Classifier**: An agent that classifies the user's topic input to search relevant papers.
- **Search Agent**: A module responsible for fetching papers from online sources.
- **Paper Processor**: A module that extracts text and metadata from uploaded PDFs or fetched papers.
- **Synthesizer**: This component generates a synthesized summary from multiple paper summaries.
- **Audio Generator**: Converts the synthesized summary or individual paper summaries into MP3 format using gTTS (Google Text-to-Speech).

### System Flow:
1. The user inputs a topic, DOI, URL, or uploads a PDF.
2. Based on the input, the system fetches papers and generates summaries.
3. If multiple papers are provided, their summaries are synthesized into one.
4. The generated summary can be downloaded as an MP3 file or viewed on the webpage.

## Setup Instructions

Follow these steps to set up the application locally on your machine:

### 1. Clone the repository:
   First, clone the project repository to your local machine:
   ```bash
   git clone <repository_url>
### 2.Install dependencies:
This project uses the following dependencies:
Flask: A lightweight web framework for Python.
gTTS (Google Text-to-Speech): Converts text to speech.
PyPDF2: For extracting text from PDF files.
Requests: To make HTTP requests (for fetching papers from URLs).
You can install all dependencies using:
Navigate to the project directory and install the required Python libraries:
cd <project_directory>
pip install -r requirements.txt

### 3.Running the application
python app.py

### 4.File Structure
/research-paper-summarizer
│
├── app.py               # Main application file
├── requirements.txt     # List of Python dependencies
├── static/              # Static files like images (e.g., architecture diagram)
│   └── architecture.png # System architecture diagram
├── templates/           # HTML templates
│   └── index.html       # Main HTML page
└── agents/              # Python modules for various agents (e.g., search, synthesizer)
    ├── search_agent.py  # Paper search agent
    ├── paper_processor.py # Paper processing (PDF extraction)
    ├── synthesizer.py   # Summarization and synthesis
    └── topic_classifier.py # Topic classificatio
 └──train_topic_model.py

### 5.Future Improvements
  1.Improve the topic classification accuracy using advanced NLP techniques.
  2.Add more features like paper citation generation and advanced PDF extraction.
  3.Enable multilingual support for summaries and audio.
  4.Support batch processing of multiple PDFs.
    

