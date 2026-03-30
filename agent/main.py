from analyzer import analyze_repo, get_python_files
from brain import generate_plan
from editor import apply_simple_edit
from git_manager import setup_git, commit, push
from utils import validate

REPO_PATH = "."


def run_agent():
    setup_git(REPO_PATH)

    summary = analyze_repo(REPO_PATH)
    files = get_python_files(REPO_PATH)

    if not files:
        print("No Python files found")
        return

    # 🔥 ONLY ONE API CALL
    task = generate_plan(summary)
    print("Plan:", task)

    for i in range(3):
        print(f"Commit {i+1}")

        file = files[i % len(files)]

        success = apply_simple_edit(file)

        if success and validate():
            commit(REPO_PATH, f"{task} (part {i+1})")

    push(REPO_PATH)


if __name__ == "__main__":
    run_agent()