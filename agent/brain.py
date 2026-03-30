from google import genai
import os

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))


def generate_task(repo_summary):
    prompt = f"""
    You are an AI software engineer.

    Analyze this repository:
    {repo_summary}

    Suggest ONE small, safe improvement.
    Keep it short.
    """

    response = client.models.generate_content(
        model="gemini-3-flash-preview",
        contents=prompt
    )

    return response.text.strip()


def generate_code_edit(file_path, file_content):
    prompt = f"""
    Improve this code safely.

    Rules:
    - Do NOT break functionality
    - Improve readability
    - Return ONLY full updated code
    - No explanation

    File: {file_path}

    Code:
    {file_content}
    """

    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=prompt
    )

    return response.text.strip()