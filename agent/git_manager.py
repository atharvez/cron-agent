import os


def setup_git(repo_path):
    os.system(f'cd {repo_path} && git config user.name "ai-agent"')
    os.system(f'cd {repo_path} && git config user.email "ai-agent@users.noreply.github.com"')


def commit(repo_path, message):
    os.system(f'cd {repo_path} && git add .')
    os.system(f'cd {repo_path} && git commit -m "{message}"')


def push(repo_path):
    os.system(f'cd {repo_path} && git push')
# update: 2026-04-08 06:21:45.325983

# update: 2026-04-09 06:22:57.759961

# update: 2026-04-10 06:54:26.557408
