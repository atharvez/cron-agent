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

# update: 2026-04-07 06:20:34.573106

# update: 2026-04-08 06:21:45.316652

# update: 2026-04-09 06:22:57.749744

# update: 2026-04-10 06:54:26.549755

# update: 2026-04-11 06:03:21.016167

# update: 2026-04-12 06:24:20.001007

# update: 2026-04-13 07:16:00.692397

# update: 2026-04-14 06:53:54.946828

# update: 2026-04-15 06:56:11.813877

# update: 2026-04-16 06:57:54.389355

# update: 2026-04-17 06:58:43.605137

# update: 2026-04-18 06:14:28.866947

# update: 2026-04-19 06:48:03.469279

# update: 2026-04-20 07:18:35.112940

# update: 2026-04-21 06:59:27.829877
