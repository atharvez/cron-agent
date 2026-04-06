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
# update: 2026-03-30 12:00:15.153836

# update: 2026-03-31 06:17:35.060814

# update: 2026-03-31 16:09:50.010400

# update: 2026-04-01 06:27:04.279014

# update: 2026-04-02 06:13:41.666256

# update: 2026-04-03 06:13:32.933125

# update: 2026-04-04 06:00:24.042103

# update: 2026-04-05 06:15:07.475200

# update: 2026-04-06 06:55:59.657635
