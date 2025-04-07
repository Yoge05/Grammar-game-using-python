📚 Grammar Quest - Interactive Grammar Learning Application
Grammar Quest is an educational web application designed to help users improve their English grammar skills through fun and interactive exercises. It offers two modes:
🔹 Computer Mode – Pre-defined grammar stories with errors
🔹 Upload Mode – Allows users to upload their own PDFs and receive grammar practice from custom content.

🚀 Key Features
🖥️ Computer Mode
Includes 5 levels of increasing difficulty.

Each level contains grammar stories with 3 intentional errors.

Users identify and correct mistakes directly on the web interface.

Error types include:

Subject-verb agreement (e.g., was vs were)

Contractions vs. possessives (e.g., its vs it's)

Commonly confused words (their/there/they're) and more.

📄 Upload Mode
Users can upload their own PDF files.

The app will scan and introduce 2–3 grammar errors per section.

Text layout and flow are preserved.

Users can then practice identifying and correcting those errors.

🛠️ Technical Setup
Prerequisites
Python 3.7 or higher

Node.js and npm

A virtual environment for Python (recommended)

Project Architecture
Backend: Built using Flask (Python), handles PDF processing and error generation.

Frontend: Developed using React.js, manages the user interface and communicates with the backend.

Folder Structure
backend/: Contains the Flask server and logic for processing PDFs.

frontend/: Contains the React front-end and user interface components.

venv/: Python virtual environment setup.

README.md: Documentation for the project.

🌐 How to Use the Application
Computer Mode
Visit the homepage of the web application.

Choose a level from 1 to 5.

Read the story and find the grammar mistakes.

Submit your corrections to get feedback.

Upload Mode
Prepare a PDF file with grammatically correct English text.

Use the "Upload PDF" feature in the app.

The app will process your PDF, add grammar errors, and present it as an interactive quiz.

Find and fix the errors as part of your learning journey.

🔄 API Overview
GET /api/computer-stories: Fetches the pre-defined stories with grammar mistakes.

POST /api/upload-pdf: Accepts user-uploaded PDFs and returns processed content with errors for correction.

🧠 Grammar Concepts Practiced
Subject-verb agreement

Tense consistency

Possessive forms

Articles (a, an, the)

Contractions

Commonly confused words

Pronoun use and consistency

🧩 Troubleshooting Tips
Backend
Ensure Python 3.7+ is installed.

Use a virtual environment and install the required dependencies.

Check if the server is running on the correct port (5001).

Frontend
Make sure all npm packages are installed.

If there are display issues, try clearing the cache or reinstalling node modules.

Confirm the frontend is running on port 3000.

👨‍💻 Developers & Contributors
Grammar Quest was built by a team of passionate developers focused on enhancing grammar education through tech innovation. Contributions are always welcome!

