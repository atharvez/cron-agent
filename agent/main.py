import os
from analyzer import analyze_repo, get_python_files
from brain import generate_task
from editor import apply_ai_edit
from git_manager import setup_git, commit, push
from utils import validate, revert

REPO_PATH = "."


def run_agent():
    setup_git(REPO_PATH)

    summary = analyze_repo(REPO_PATH)
    files = get_python_files(REPO_PATH)

    if not files:
        print("No Python files found.")
        return

    for i in range(3):
        print(f"\n--- Commit {i+1} ---")

        task = generate_task(summary)
        print("Task:", task)

        target_file = files[i % len(files)]

        success = apply_ai_edit(target_file)

        if not success:
            print("Edit failed, skipping...")
            continue

        if validate():
            commit(REPO_PATH, f"AI Task {i+1}: {task}")
        else:
            print("Validation failed. Reverting...")
            revert(REPO_PATH)

    push(REPO_PATH)


if __name__ == "__main__":
    run_agent()