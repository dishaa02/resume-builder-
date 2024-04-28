from flask import Flask, request
import docx2txt
from difflib import SequenceMatcher

app = Flask(__name__)

def calculate_similarity(text1, text2):
    """Calculate similarity percentage between two texts."""
    matcher = SequenceMatcher(None, text1, text2)
    similarity_ratio = matcher.ratio()
    similarity_percentage = round(similarity_ratio * 100, 2)
    return similarity_percentage

@app.route('/')
def upload_file():
    return '''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Job Description Matching</title>
    </head>
    <body>
        <div class="container">
            <h2>Job Description Matching</h2>
            <div class="box">
                <h2>Submit Your Resume</h2>
                <form action="/match" method="post" enctype="multipart/form-data">
                    <label for="resume-upload" class="upload-button">Upload Resume</label>
                    <input type="file" id="resume-upload" name="resume" accept=".docx">
                </div>
                <div class="box">
                    <h2>Submit Your Job Description</h2>
                    <label for="job-description-upload" class="upload-button">Upload Job Description</label>
                    <input type="file" id="job-description-upload" name="job_description" accept=".docx">
                </div>
                <button class="button" type="submit">Match Your Resume</button>
            </form>
        </div>
    </body>
    </html>
    '''

@app.route('/match', methods=['POST'])
def match_resume():
    if 'resume' not in request.files or 'job_description' not in request.files:
        return "Please upload both resume and job description files."

    resume_file = request.files['resume']
    job_description_file = request.files['job_description']

    if resume_file.filename == '' or job_description_file.filename == '':
        return "Please select both resume and job description files."

    resume_text = docx2txt.process(resume_file)
    job_description_text = docx2txt.process(job_description_file)

    similarity_percentage = calculate_similarity(resume_text, job_description_text)

    return f"Similarity Percentage: {similarity_percentage}%"

if __name__ == '__main__':
    app.run(debug=True)
