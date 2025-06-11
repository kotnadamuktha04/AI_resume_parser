import streamlit as st
import requests

st.title("AI Resume Parser")

uploaded_file = st.file_uploader("Upload a Resume (PDF)", type=["pdf"])

if uploaded_file:
    with open(f"resumes/{uploaded_file.name}", "wb") as f:
        f.write(uploaded_file.getbuffer())

    response = requests.post("http://127.0.0.1:5000/upload", files={"resume": uploaded_file})
    
    if response.status_code == 200:
        data = response.json()
        st.write("### Extracted Details:")
        st.write(f"**Name:** {data['Name']}")
        st.write(f"**Email:** {data['Email']}")
        st.write(f"**Phone:** {data['Phone']}")
        st.write(f"**Skills:** {', '.join(data['Skills'])}")
    else:
        st.error("Error processing the resume.")
