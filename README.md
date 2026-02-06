📄 ATS Resume Score & Skill Gap Analyzer

🚀 Live App:
👉 https://ats-resume-analyzer-327ap66qvkdz6vwy4xhqyn.streamlit.app/

An end-to-end Machine Learning + NLP web application that evaluates how well a resume matches a given job description using ATS-style scoring logic.
The system highlights missing skills, computes a match percentage, and helps candidates optimize their resumes for better shortlisting.


🎯 Why This Project?

=======
🎯 Why This Project?

>>>>>>> 062ac63ed075957450f6473f2b735faf4fcc9675
Applicant Tracking Systems (ATS) are widely used by recruiters to filter resumes before human review.
This project simulates that process using modern NLP techniques, helping job seekers understand where their resume stands and how to improve it.

🚀 Features

📄 Upload resume in PDF format

📝 Paste any Job Description

📊 ATS Match Score (%)

⚠️ Missing Skills Identification

🧹 Resume text preprocessing & cleaning

🔍 Resume preview after NLP cleaning

🌐 Fully deployed Streamlit Web App

🛠 Tech Stack

Python

Streamlit (Web UI)

Natural Language Processing (NLP)

Sentence Transformers (BERT)

Scikit-learn

PyTorch

pdfplumber

🧠 How It Works (ML Pipeline)

Resume PDF is parsed using pdfplumber

Text preprocessing:

Lowercasing

Special character removal

Resume & Job Description are converted into embeddings using Sentence Transformers (BERT)

Cosine Similarity is calculated between resume and JD

ATS score is generated as a percentage

Skill gaps are identified by comparing expected skills vs resume content

▶️ Run Locally
pip install -r requirements.txt
streamlit run app.py


🔮 Future Enhancements

Resume improvement suggestions powered by GenAI

Skill weightage based on job priority

Download ATS report as PDF

Support for multiple resume comparisons

👤 Author

Satheesh Mulinti
Final Year CSE Student | ML & NLP Enthusiast

🔗 GitHub: https://github.com/satheeshMulinti

⭐ If you like this project

<<<<<<< HEAD
Give it a ⭐ on GitHub — it motivates me to build more impactful projects!
=======
Give it a ⭐ on GitHub — it motivates me to build more impactful projects!
>>>>>>> 062ac63ed075957450f6473f2b735faf4fcc9675
