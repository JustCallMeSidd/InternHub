import streamlit as st
import json
import re
import base64
from llm import call_llm
from prompts.resume_parser_prompt import RESUME_PARSER_SYSTEM_PROMPT, get_resume_parser_prompt
from prompts.internship_match_prompt import INTERNSHIP_MATCH_SYSTEM_PROMPT, get_internship_match_prompt
from utils.resume_reader import read_pdf, read_txt

st.set_page_config(page_title="InternHub AI", page_icon="favicon.png", layout="wide")



# CSS part
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;800&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
    }
    
    .stApp {
        background: radial-gradient(circle at top right, #1f2937, #111827);
    }
    
    .main-header {
        text-align: center;
        padding: 2rem 0 1rem 0;
        background: linear-gradient(135deg, #6366f1 0%, #a855f7 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-weight: 800;
        font-size: 3.5rem;
        margin-bottom: 0px;
    }
    
    .sub-header {
        text-align: center;
        color: #9ca3af;
        font-size: 1.2rem;
        margin-bottom: 3rem;
        font-weight: 500;
    }
    
    .card {
        background: rgba(17, 24, 39, 0.7);
        backdrop-filter: blur(10px);
        border-radius: 20px;
        padding: 2rem;
        border: 1px solid rgba(75, 85, 99, 0.4);
        box-shadow: 0 10px 30px rgba(0,0,0,0.2);
        margin-bottom: 2rem;
    }
    
    .stButton>button {
        width: 100%;
        border-radius: 12px;
        height: 3.5rem;
        font-weight: 600;
        background: linear-gradient(135deg, #6366f1 0%, #a855f7 100%);
        color: white !important;
        border: none;
        transition: all 0.3s ease;
        font-size: 1.1rem;
    }
    
    .stButton>button:hover {
        transform: translateY(-2px);
        box-shadow: 0 8px 20px rgba(99, 102, 241, 0.3);
        background: linear-gradient(135deg, #4f46e5 0%, #9333ea 100%);
    }
    
    .section-title {
        color: #f3f4f6;
        font-weight: 700;
        font-size: 1.6rem;
        margin-bottom: 1.5rem;
        display: flex;
        align-items: center;
        gap: 12px;
    }

    .footer {
        text-align: center;
        color: #9ca3af;
        font-size: 0.9rem;
        margin-top: 3rem;
        padding-bottom: 1rem;
    }

    /* Hide default Streamlit elements */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)

def render_ats_gauge(score):
    color = "#ef4444" if score < 40 else "#f59e0b" if score < 70 else "#10b981"
    
    st.markdown(f"""
        <div style="display: flex; flex-direction: column; align-items: center; justify-content: center; margin-bottom: 30px;">
            <div style="
                position: relative;
                width: 180px; 
                height: 180px; 
                border-radius: 50%; 
                background: conic-gradient({color} {score * 3.6}deg, #e5e7eb 0deg);
                display: flex;
                align-items: center;
                justify-content: center;
                box-shadow: 0 10px 25px rgba(0,0,0,0.05);
            ">
                <div style="
                    width: 145px; 
                    height: 145px; 
                    border-radius: 50%; 
                    background: #111827;
                    display: flex;
                    flex-direction: column;
                    align-items: center;
                    justify-content: center;
                    border: 1px solid #374151;
                ">
                    <span style="font-size: 42px; font-weight: 800; color: {color}; font-family: 'Inter', sans-serif;">{score}%</span>
                    <span style="font-size: 14px; font-weight: 600; color: #6b7280; font-family: 'Inter', sans-serif; text-transform: uppercase; letter-spacing: 1px;">Match</span>
                </div>
            </div>
        </div>
    """, unsafe_allow_html=True)

def extract_score(text):
    match = re.search(r"Score:\s*(\d+)", text)
    if match:
        return int(match.group(1))
    return None

def get_img_as_base64(file):
    with open(file, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()

img = get_img_as_base64("favicon.png")

st.markdown(f"""
    <div style="text-align: center;">
        <img src="data:image/png;base64,{img}" style="width: 80px; height: 80px; margin-bottom: 10px;">
        <h1 class="main-header" style="margin-top: 0;">InternHub AI Evaluator</h1>
    </div>
""", unsafe_allow_html=True)
st.markdown('<p class="sub-header">AI-Powered Resume Analysis & Internship Matching</p>', unsafe_allow_html=True)

# internship details
st.markdown('<div class="card">', unsafe_allow_html=True)
st.markdown('<div class="section-title">📋 Internship Job Description</div>', unsafe_allow_html=True)
job_description = st.text_area(
    "Paste the Job Description (JD) here to analyze the match", 
    height=180, 
    placeholder="Example: We are looking for a Python Intern with experience in Streamlit and LLMs...",
    help="The AI will use this description to evaluate your profile or resume.",
    label_visibility="collapsed"
)
st.markdown('</div>', unsafe_allow_html=True)

st.divider()

# main content
col1, col2 = st.columns(2)

with col1:
    st.markdown('<div class="card" style="height: 100%;">', unsafe_allow_html=True)
    st.markdown('<div class="section-title">👤 Student Profile</div>', unsafe_allow_html=True)
    input_method = st.radio("Choose Input Method", ["Manual Input", "Upload Resume"], horizontal=True, label_visibility="collapsed")
    
    st.write("")
    
    skills = ""
    interests = ""
    experience = ""
    
    if input_method == "Manual Input":
        skills = st.text_area("Skills (comma separated)", placeholder="Python, SQL, React...")
        interests = st.text_area("Interests", placeholder="AI, Web Development, Data Science...")
        experience = st.text_area("Experience Summary", height=150, placeholder="Briefly describe past internships or projects...")
    else:
        uploaded_file = st.file_uploader("Upload Resume (PDF/TXT)", type=["pdf", "txt"])
        if uploaded_file is not None:
            with st.spinner("Parsing Resume..."):
                if uploaded_file.type == "application/pdf":
                    resume_text = read_pdf(uploaded_file)
                else:
                    resume_text = read_txt(uploaded_file)
                
                
                messages = [
                    {"role": "system", "content": RESUME_PARSER_SYSTEM_PROMPT},
                    {"role": "user", "content": get_resume_parser_prompt(resume_text)}
                ]
                
                parsed_data_json = call_llm(messages, json_mode=True)
                
                try:
                    parsed_data = json.loads(parsed_data_json)
                    skills = ", ".join(parsed_data.get("skills", []))
                    interests = ", ".join(parsed_data.get("interests", []))
                    experience = parsed_data.get("experience", "")
                    
                    st.success("Resume Parsed Successfully!")
                    st.json(parsed_data)
                except:
                    st.error("Failed to parse resume JSON. Raw output:")
                    st.write(parsed_data_json)
    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="card" style="height: 100%;">', unsafe_allow_html=True)
    st.markdown('<div class="section-title">📊 Match Analysis</div>', unsafe_allow_html=True)
    analyze_btn = st.button("Run AI Analysis", type="primary")
    
    if analyze_btn:
        if not job_description:
            st.warning("Please enter a Job Description.")
        elif not skills and not experience:
            st.warning("Please provide student details.")
        else:
            with st.spinner("Performing Deep Analysis..."):
                messages = [
                    {"role": "system", "content": INTERNSHIP_MATCH_SYSTEM_PROMPT},
                    {"role": "user", "content": get_internship_match_prompt(skills, interests, experience, job_description)}
                ]
                
                analysis_result = call_llm(messages)
                
                # extract score and show
                score = extract_score(analysis_result)
                if score is not None:
                    render_ats_gauge(score)
                
                st.markdown('<div style="background: rgba(99, 102, 241, 0.05); padding: 20px; border-radius: 12px; border: 1px solid rgba(99, 102, 241, 0.1);">', unsafe_allow_html=True)
                st.markdown(analysis_result)
                st.markdown('</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

st.markdown('<div class="footer">Powered by InternHub AI</div>', unsafe_allow_html=True)
