import google.generativeai as genai
import os
import json

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-1.5-flash")


def generate_task(repo_summary):
    prompt = f"""
    You are an AI software engineer.

    Analyze this repository:
    {repo_summary}

    Suggest ONE small, safe improvement task.
    Keep it short.
    """

    response = model.generate_content(prompt)
    return response.text.strip()


def generate_code_edit(file_path, file_content):
    prompt = f"""
    You are an expert developer.

    Improve the following file safely.

    Rules:
    - Do NOT break functionality
    - Improve readability / structure
    - Keep logic same
    - Return ONLY valid Python code
    - No explanations

    File: {file_path}

    Code:
    {file_content}
    """

    response = model.generate_content(prompt)
    return response.text.strip()