import streamlit as st
import pdfplumber
import re
from sentence_transformers import SentenceTransformer, util

@st.cache_resource
def load_model():
    return SentenceTransformer("all-MiniLM-L6-v2")

model = load_model()


def clean_text(text):
    text = text.lower()
    text = re.sub(r"[^a-z\s]", "", text)
    return text

def find_missing_skills(resume_text, skills_text):
    resume_words = set(resume_text.split())
    skills = [s.strip().lower() for s in skills_text.split(",")]
    missing = [s for s in skills if s not in resume_words]
    return missing



st.set_page_config(page_title="ATS Resume Analyzer", layout="centered")

st.title("📄 ATS Resume Score & Skill Gap Analyzer")
st.write("Upload your resume and paste the job description to check ATS compatibility.")

resume_file = st.file_uploader("Upload Resume (PDF)", type=["pdf"])
job_description = st.text_area("Paste Job Description Here")

skills = st.text_input(
    "Expected Skills (comma separated)",
    "Python, Machine Learning, SQL, Data Preprocessing"
)


if st.button("Analyze Resume"):

    if resume_file is None or job_description.strip() == "":
        st.error("Please upload a resume PDF and paste a job description.")
        st.stop()



    with pdfplumber.open(resume_file) as pdf:
        text = ""
        for page in pdf.pages:
            if page.extract_text():
                text += page.extract_text()

    resume_clean = clean_text(text)
    jd_clean = clean_text(job_description)




    resume_embedding = model.encode(resume_clean, convert_to_tensor=True)
    jd_embedding = model.encode(jd_clean, convert_to_tensor=True)

    similarity_score = util.cos_sim(resume_embedding, jd_embedding)
    ats_score = round(float(similarity_score[0][0]) * 100, 2)



    st.subheader("📊 ATS Match Score")
    st.metric("ATS Score", f"{ats_score}%")

   
    st.subheader("💡 Suggestions")

    if ats_score < 50:
        st.warning("Low ATS score. Add more role-specific keywords and skills.")
    elif ats_score < 80:
        st.info("Good match, but resume can be optimized further.")
    else:
        st.success("Resume is well optimized for ATS 🎉")

    
    missing_skills = find_missing_skills(resume_clean, skills)

    st.subheader("❌ Missing Skills")
    if missing_skills:
        st.write(", ".join(missing_skills))
    else:
        st.success("No major skills missing 🎉")


    st.subheader("🧾 Cleaned Resume Text (Preview)")
    st.write(resume_clean[:500])
