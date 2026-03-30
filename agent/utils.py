import os

def validate():
    # optional: add tests here
    # return os.system("pytest") == 0
    return True


def revert(repo_path):
    os.system(f'cd {repo_path} && git reset --hard')