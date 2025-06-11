import re
import pdfminer.high_level
import spacy
import nltk

nlp = spacy.load("en_core_web_sm")

def extract_text_from_pdf(pdf_path):
    return pdfminer.high_level.extract_text(pdf_path)

def extract_name(text):
    doc = nlp(text)
    for ent in doc.ents:
        if ent.label_ == "PERSON":
            return ent.text
    return "Not found"

def extract_email(text):
    match = re.search(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", text)
    return match.group() if match else "Not found"

def extract_phone(text):
    match = re.search(r"\+?\d{10,15}", text)
    return match.group() if match else "Not found"

def extract_skills(text):
    skills = ["Python", "Java", "C++", "Machine Learning", "Data Science", "SQL"]
    found_skills = [skill for skill in skills if skill.lower() in text.lower()]
    return found_skills if found_skills else "No skills found"

def parse_resume(pdf_path):
    text = extract_text_from_pdf(pdf_path)
    return {
        "Name": extract_name(text),
        "Email": extract_email(text),
        "Phone": extract_phone(text),
        "Skills": extract_skills(text)
    }
