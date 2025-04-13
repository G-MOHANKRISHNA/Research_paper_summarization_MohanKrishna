from flask import Flask, render_template, request, send_from_directory
from agents.topic_classifier import TopicClassifier
from agents.search_agent import search_papers
from agents.paper_processor import extract_text_from_pdf, fetch_metadata_from_doi, fetch_text_from_url
from agents.synthesizer import synthesize_across_papers  # ← Synthesizer import
import os
from gtts import gTTS

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['AUDIO_FOLDER'] = 'audio_files'
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
os.makedirs(app.config['AUDIO_FOLDER'], exist_ok=True)

@app.route('/', methods=['GET', 'POST'])
def index():
    papers = []
    synthesis_summary = None  # ← synthesized summary

    if request.method == 'POST':
        if 'topic' in request.form:
            topic = request.form['topic']
            papers = search_papers(topic)

        if 'doi' in request.form and request.form['doi']:
            doi = request.form['doi']
            metadata = fetch_metadata_from_doi(doi)
            papers = [metadata]

        if 'url' in request.form and request.form['url']:
            url = request.form['url']
            text = fetch_text_from_url(url)
            papers = [{
                "title": "Paper from URL",
                "summary": text[:500],
                "pdf_url": url,
                "link": url,
                "citation": url
            }]

        if 'pdf' in request.files:
            pdf_file = request.files['pdf']
            if pdf_file.filename.endswith('.pdf'):
                path = os.path.join(app.config['UPLOAD_FOLDER'], pdf_file.filename)
                pdf_file.save(path)
                text = extract_text_from_pdf(path)
                papers = [{
                    "title": pdf_file.filename,
                    "summary": text[:500],
                    "pdf_url": "",
                    "link": "",
                    "citation": f"Uploaded file: {pdf_file.filename}"
                }]

        for paper in papers:
            if paper.get('summary'):
                audio_file = generate_audio(paper['summary'], paper['title'])
                paper['audio_file'] = audio_file
            if 'link' in paper and paper['link']:
                paper['citation'] = paper['link']

        # 🔥 Generate cross-paper synthesis if multiple papers
        summaries = [paper['summary'] for paper in papers if 'summary' in paper]
        if len(summaries) > 1:
            synthesis_summary = synthesize_across_papers(summaries)

    return render_template('index.html', papers=papers, synthesis=synthesis_summary)

def generate_audio(text, title):
    try:
        tts = gTTS(text=text, lang='en')
        audio_filename = f"{title.replace(' ', '_')}.mp3"
        audio_path = os.path.join(app.config['AUDIO_FOLDER'], audio_filename)
        tts.save(audio_path)
        return audio_filename
    except Exception as e:
        print(f"Error generating audio: {e}")
        return None

@app.route('/audio/<filename>')
def download_audio(filename):
    return send_from_directory(app.config['AUDIO_FOLDER'], filename)

if __name__ == '__main__':
    app.run(debug=True)
