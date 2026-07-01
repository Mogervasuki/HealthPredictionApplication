import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))


def get_health_prediction(glucose, haemoglobin, cholesterol):

    prompt = f"""
You are an AI healthcare assistant.

Analyze the following patient's blood test values.

Blood Test Results

Glucose: {glucose} mg/dL
Haemoglobin: {haemoglobin} g/dL
Cholesterol: {cholesterol} mg/dL

Using your medical knowledge, determine the most likely health condition or disease risk.

Do NOT use predefined responses.
Analyze the values carefully.

Return ONLY in the following format.

Possible Condition:
<condition>

Reason:
<short explanation>

Keep the answer under 60 words.
"""

    try:

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )

        return response.text.strip()

    except Exception as e:

        print("Gemini Error:", e)

        return "Prediction could not be generated."