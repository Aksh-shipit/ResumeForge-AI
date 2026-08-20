print("AI FILE LOADED")
from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()
print(__file__)

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)


# =====================================
# Generate AI Resume Summary
# =====================================

def generate_summary(role, skills, experience):

    prompt = f"""
You are an expert resume writer.

Write a professional ATS-friendly resume summary.

Target Role:
{role}

Skills:
{skills}

Experience:
{experience}

Keep it between 70 and 100 words.
"""

    response = client.chat.completions.create(

        model="llama-3.3-70b-versatile",

        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],

        temperature=0.7,
        max_tokens=200

    )

    return response.choices[0].message.content


# =====================================
# Analyze Resume
# =====================================

def analyze_resume(data):

    prompt = f"""
You are an experienced technical recruiter and ATS expert.

Analyze the following resume.

Name:
{data.get('name', '')}

Target Role:
{data.get('role', '')}

Professional Summary:
{data.get('summary', '')}

Education:
{data.get('education', [])}

Skills:
{data.get('skills', [])}

Experience:
{data.get('experience', [])}

Projects:
{data.get('projects', [])}

Give exactly 5 short improvement suggestions.

Requirements:
- Return ONLY the suggestions.
- One suggestion per line.
- Do not number them.
- Do not add any introduction.
"""

    response = client.chat.completions.create(

        model="llama-3.3-70b-versatile",

        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],

        temperature=0.5,
        max_tokens=250

    )

    text = response.choices[0].message.content.strip()

    suggestions = [
        line.strip("-• ").strip()
        for line in text.split("\n")
        if line.strip()
    ]

    return suggestions