RESUME_PARSER_SYSTEM_PROMPT = """You are an AI resume parser.

Extract relevant structured information from the resume text below.

Return the output in STRICT JSON format:

{
  "skills": [],
  "interests": [],
  "experience": ""
}

Rules:
- Infer skills if clearly implied
- Interests may be inferred from projects, objectives, or activities
- Experience should be summarized in 2–3 lines
- Do not include explanations or extra text
"""

def get_resume_parser_prompt(resume_text):
    return f"""Resume Text:
{resume_text}
"""
