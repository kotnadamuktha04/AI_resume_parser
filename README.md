# AI_resume_parser

Prerequisites


Python 3.8+ (Install from python.org)

Git (Optional, for cloning the repository)

Pip (Python package manager, comes with Python)

Step 1: Clone or Download the Project

Option A: Clone with Git

bash

git clone https://github.com/your-repository/resume-parser.git

cd resume-parser

Option B: Download Manually


Download the project ZIP from GitHub and extract it.

Step 2: Set Up a Virtual Environment (Recommended)


bash

# Create a virtual environment (Windows)

python -m venv venv

venv\Scripts\activate  # Activate on Windows

# Or for macOS/Linux

python3 -m venv venv

source venv/bin/activate

Step 3: Install Dependencies

bash

pip install -r requirements.txt  # If you have a requirements file
OR install manually:

bash

pip install flask werkzeug PyMuPDF python-docx spacy sqlite3

(Optional) Install spaCy's English model for NLP:

bash

python -m spacy download en_core_web_sm

Step 4: Initialize the Database

bash

python init_db.py  # Or run this in your Python shell

(If init_db.py doesn’t exist, the app will create the database automatically on first run.)

Step 5: Run the Application

bash

# On Windows/macOS/Linux

python app.py  # Or the name of your main Flask file

You should see output like:

* Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)

Step 6: Access the Web Interface

Open a browser and go to:

http://localhost:5000

Upload resumes (PDF/DOCX) and view parsed data.

Step 7: Test API Endpoints

Parse a resume via API:

bash

curl -X POST -F "resume=@resume.pdf" http://localhost:5000/api/parse-resume

Export data (if you added the export routes):

http://localhost:5000/export/candidates/csv

Deployment Options

1. Local Network Access

Run Flask publicly (not secure for production!):

bash

flask run --host=0.0.0.0
# Access via your local IP (e.g., http://192.168.x.x:5000)

2. Production Deployment

Use Gunicorn + Nginx (for Linux) or Waitress (for Windows):

bash
pip install gunicorn
gunicorn -w 4 app:app  # Run on port 8000
3. Docker (Advanced)

Create a Dockerfile:

dockerfile
FROM python:3.8-slim
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
CMD ["python", "app.py"]
Then build and run:

bash
docker build -t resume-parser .
docker run -p 5000:5000 resume-parser
