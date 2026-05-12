import os

from google import genai
from dotenv import load_dotenv

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


def summarize_text(text):

    text = text[:1000]

    prompt = f"""
    Summarize the following document in 5-10 sentences.

    Document:
    {text}
    """

    response = client.models.generate_content(
        model="gemini-3-flash-preview",
        contents=prompt
    )

    return response.text