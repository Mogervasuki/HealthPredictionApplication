import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-2.5-flash")


def get_health_prediction(glucose, haemoglobin, cholesterol):

    prompt = f"""
You are a healthcare prediction assistant.

Patient values:

Glucose = {glucose}
Haemoglobin = {haemoglobin}
Cholesterol = {cholesterol}

Predict ONLY ONE possible health condition or disease risk.

Examples:

Healthy

Diabetes Risk

High Cholesterol Risk

Possible Anemia

Prediabetes Risk

Return ONLY:

Possible Condition:
<condition>

Do not explain.
Do not give recommendation.
Do not use bullet points.
"""

    try:
        response = model.generate_content(prompt)
        return response.text.strip()

    except Exception as e:
        print("Gemini Error:", e)
        return "Prediction Not Available"