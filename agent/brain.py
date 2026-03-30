from google import genai
import os

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))


def generate_plan(repo_summary):
    prompt = f"""
    You are an AI developer.

    Repo:
    {repo_summary}

    Give ONE simple improvement idea.
    Keep it under 10 words.
    """

    try:
        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=prompt
        )
        return response.text.strip()
    except Exception as e:
        print("Gemini failed:", e)
        return "Minor code cleanup"