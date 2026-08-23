print("AI FILE LOADED")

from groq import Groq
from dotenv import load_dotenv
import os


# =====================================
# Load Environment Variables
# =====================================

load_dotenv()

api_key = os.getenv("GROQ_API_KEY")

print("AI FILE:", __file__)
print("GROQ API KEY LOADED:", bool(api_key))


# =====================================
# Groq Client
# =====================================

if not api_key:
    raise ValueError(
        "GROQ_API_KEY not found. "
        "Make sure your .env file contains GROQ_API_KEY=your_key"
    )

client = Groq(
    api_key=api_key
)


# =====================================
# Model
# =====================================

# NOTE: gpt-oss-120b is a REASONING model — it can burn its entire
# max_tokens budget on internal "thinking" before it ever writes the
# final answer, leaving message.content empty. If that keeps happening
# even after raising max_tokens, switch to a non-reasoning model, e.g.:
# MODEL_NAME = "llama-3.3-70b-versatile"
MODEL_NAME = "openai/gpt-oss-120b"


# =====================================
# Generate AI Resume Summary
# =====================================

def generate_summary(role, skills, experience):

    prompt = f"""
You are an expert professional resume writer.

Create a professional ATS-friendly resume summary for the candidate.

Target Role:
{role}

Skills:
{skills}

Experience:
{experience}

Requirements:
- Write between 70 and 100 words.
- Make the summary professional and concise.
- Tailor the summary to the target role.
- Naturally include relevant skills provided by the candidate.
- Use ONLY information provided by the candidate.
- Do not invent companies, achievements, education, certifications, experience, or skills.
- Do not exaggerate the candidate's experience.
- Do not use headings.
- Do not use bullet points.
- Return ONLY the final resume summary.
"""

    try:

        response = client.chat.completions.create(
            model=MODEL_NAME,

            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ],

            temperature=0.7,
            max_tokens=600
        )

        print("========== GROQ SUMMARY RESPONSE ==========")
        print(response)
        print("============================================")

        # Check whether the API returned choices
        if not response.choices:
            print("ERROR: Groq returned no choices.")
            return ""

        choice = response.choices[0]

        # Debug info to diagnose empty-content issues
        print("FINISH REASON:", choice.finish_reason)
        print("MESSAGE OBJECT:", choice.message)

        if choice.finish_reason == "length":
            print(
                "WARNING: Response was cut off before finishing "
                "(finish_reason=length). The model may have used up "
                "the token budget on internal reasoning. Consider "
                "raising max_tokens further or switching MODEL_NAME "
                "to a non-reasoning model."
            )

        # Extract generated text
        summary = choice.message.content

        print("========== GENERATED SUMMARY ==========")
        print(repr(summary))
        print("=======================================")

        if not summary:
            print("ERROR: Groq returned empty content.")
            return ""

        return summary.strip()

    except Exception as e:

        print("========== GROQ SUMMARY ERROR ==========")
        print("Error Type:", type(e).__name__)
        print("Error:", str(e))
        print("========================================")

        raise


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
- Do not add an introduction.
- Do not invent information.
- Make every suggestion specific and actionable.
- Focus on improving ATS compatibility, clarity, impact, keywords,
  measurable achievements, and resume structure.
"""

    try:

        response = client.chat.completions.create(
            model=MODEL_NAME,

            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ],

            temperature=0.5,
            max_tokens=500
        )

        if not response.choices:
            print("ERROR: Groq returned no choices for resume analysis.")
            return []

        choice = response.choices[0]

        print("FINISH REASON (analysis):", choice.finish_reason)

        if choice.finish_reason == "length":
            print(
                "WARNING: Analysis response was cut off before finishing "
                "(finish_reason=length). Consider raising max_tokens further."
            )

        text = choice.message.content

        if not text:
            print("ERROR: Groq returned empty analysis.")
            return []

        text = text.strip()

        suggestions = [
            line.strip("-•* ").strip()
            for line in text.split("\n")
            if line.strip()
        ]

        # Keep exactly 5 suggestions if the model returns more
        suggestions = suggestions[:5]

        print("========== AI SUGGESTIONS ==========")

        for suggestion in suggestions:
            print(suggestion)

        print("====================================")

        return suggestions

    except Exception as e:

        print("========== GROQ ANALYSIS ERROR ==========")
        print("Error Type:", type(e).__name__)
        print("Error:", str(e))
        print("==========================================")

        raise