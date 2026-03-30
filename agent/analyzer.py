import os

def get_python_files(repo_path):
    files = []
    for root, _, filenames in os.walk(repo_path):
        for f in filenames:
            if f.endswith(".py"):
                files.append(os.path.join(root, f))
    return files


def analyze_repo(repo_path):
    files = get_python_files(repo_path)
    return "\n".join(files[:10])