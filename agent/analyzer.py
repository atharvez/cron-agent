import os

def analyze_repo(repo_path):
    summary = []

    for root, _, files in os.walk(repo_path):
        for file in files:
            if file.endswith(".py"):
                summary.append(os.path.join(root, file))

    return "\n".join(summary)


def get_python_files(repo_path):
    py_files = []

    for root, _, files in os.walk(repo_path):
        for file in files:
            if file.endswith(".py"):
                py_files.append(os.path.join(root, file))

    return py_files