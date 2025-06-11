from flask import Flask, request, jsonify
from parser import parse_resume
from database import connect_db

app = Flask(__name__)

@app.route('/upload', methods=['POST'])
def upload_resume():
    file = request.files['resume']
    file_path = f"resumes/{file.filename}"
    file.save(file_path)

    data = parse_resume(file_path)
    
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO resumes (name, email, phone, skills) VALUES (%s, %s, %s, %s)", 
                   (data["Name"], data["Email"], data["Phone"], ",".join(data["Skills"])))
    conn.commit()
    conn.close()

    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
