from flask import Flask, jsonify, send_from_directory, request
from flask_cors import CORS
import PyPDF2
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from base64 import b64encode, b64decode
import openai
import os

app = Flask(__name__, static_folder='../frontend')
CORS(app)

# Set your OpenAI API key
openai.api_key = 'your-api-key-here'  # Replace with your actual API key

class SecurePDFHandler:
    def __init__(self):
        self.key = b'ThisIsA32ByteLongSecureKey12345678'

    def process_pdf(self, file):
        try:
            pdf_reader = PyPDF2.PdfReader(file)
            text = ""
            for page in pdf_reader.pages:
                text += page.extract_text() + "\n"
            return text
        except Exception as e:
            print(f"PDF processing error: {e}")
            return None

pdf_handler = SecurePDFHandler()

# Fixed computer-generated stories with proper format
stories = [
    {
        "id": 1,
        "level": 1,
        "title": "The Park Day 🌳",
        "text": "The children was playing in the park. They seen a beautiful bird in it's nest. The flowers was blooming everywhere.",
        "errors": [
            {"original": "was", "corrected": "were"},
            {"original": "seen", "corrected": "saw"},
            {"original": "it's", "corrected": "its"}
        ]
    },
    {
        "id": 2,
        "level": 2,
        "title": "School Day 📚",
        "text": "Every student have their own project. Neither John or Mary were finished yet. The teacher don't like late work.",
        "errors": [
            {"original": "have", "corrected": "has"},
            {"original": "or", "corrected": "nor"},
            {"original": "don't", "corrected": "doesn't"}
        ]
    },
    {
        "id": 3,
        "level": 3,
        "title": "The Beach Trip 🏖️",
        "text": "They was excited about there beach trip. The waves is very high today. Sarah and Tom has forgot their sunscreen.",
        "errors": [
            {"original": "was", "corrected": "were"},
            {"original": "there", "corrected": "their"},
            {"original": "is", "corrected": "are"}
        ]
    },
    {
        "id": 4,
        "level": 4,
        "title": "The Zoo Adventure 🦁",
        "text": "The lion were sleeping in it's cage. The monkeys is playing with there toys. Each animal have different foods.",
        "errors": [
            {"original": "were", "corrected": "was"},
            {"original": "it's", "corrected": "its"},
            {"original": "have", "corrected": "has"}
        ]
    },
    {
        "id": 5,
        "level": 5,
        "title": "Birthday Party 🎂",
        "text": "Everyone bring presents to the party. The cake don't look good. Neither the ice cream or the juice were cold.",
        "errors": [
            {"original": "bring", "corrected": "brings"},
            {"original": "don't", "corrected": "doesn't"},
            {"original": "or", "corrected": "nor"}
        ]
    }
]

@app.route('/')
def index():
    return send_from_directory(app.static_folder, 'index.html')

@app.route('/api/computer-stories')
def get_computer_stories():
    return jsonify({"stories": stories})

@app.route('/api/upload-pdf', methods=['POST'])
def upload_pdf():
    if 'file' not in request.files:
        return jsonify({"error": "No file uploaded"}), 400
        
    file = request.files['file']
    if not file.filename.endswith('.pdf'):
        return jsonify({"error": "Please upload a PDF file"}), 400

    try:
        content = pdf_handler.process_pdf(file)
        if not content:
            return jsonify({"error": "Could not process PDF"}), 400

        # Define common grammar error patterns
        error_patterns = [
            ("were", "was"),
            ("saw", "seen"),
            ("their", "there"),
            ("its", "it's"),
            ("has", "have")
        ]

        chapters = []
        titles = []
        current_chapter = ""
        current_title = ""
        
        for line in content.split('\n'):
            line = line.strip()
            if line.lower().startswith(('chapter', 'story', 'tale')):
                if current_chapter:
                    chapters.append(current_chapter.strip())
                    titles.append(current_title or f"Story {len(chapters)}")
                current_chapter = ""
                current_title = line
            else:
                current_chapter += line + "\n"
        
        if current_chapter:
            chapters.append(current_chapter.strip())
            titles.append(current_title or f"Story {len(chapters)}")

        pdf_stories = []
        for i, (chapter, title) in enumerate(zip(chapters, titles), 1):
            if len(chapter.strip()) > 0:
                # Create version with errors
                text_with_errors = chapter
                errors = []
                
                # Introduce exactly 2-3 errors per story
                import random
                num_errors = random.randint(2, 3)  # Only 2-3 errors
                possible_errors = []
                
                # Find all possible errors we can introduce
                for correct, incorrect in error_patterns:
                    if correct in text_with_errors and len(errors) < num_errors:
                        possible_errors.append((correct, incorrect))
                
                # Select random errors to introduce (maximum 3)
                if possible_errors:
                    selected_errors = random.sample(
                        possible_errors, 
                        min(num_errors, len(possible_errors))
                    )
                    
                    # Introduce the selected errors
                    for correct, incorrect in selected_errors:
                        # Only replace the first occurrence
                        text_with_errors = text_with_errors.replace(correct, incorrect, 1)
                        errors.append({
                            "original": incorrect,
                            "corrected": correct
                        })

                pdf_stories.append({
                    "id": i,
                    "level": i,
                    "title": title,
                    "text": text_with_errors,
                    "errors": errors
                })

        return jsonify({"stories": pdf_stories})
        
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({"error": "Error processing PDF"}), 500

if __name__ == '__main__':
    print("\n=== Grammar Quest Game ===")
    print("1. Open http://localhost:5001 in your browser")
    print("2. Choose between computer stories or upload PDF")
    print("3. Press Ctrl+C to stop the server")
    print("========================\n")
    app.run(port=5001, debug=True) 










