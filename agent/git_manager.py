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

# update: 2026-04-11 06:03:21.023641

# update: 2026-04-12 06:24:20.010725

# update: 2026-04-13 07:16:00.702129

# update: 2026-04-14 06:53:54.957315

# update: 2026-04-15 06:56:11.822555

# update: 2026-04-16 06:57:54.399605

# update: 2026-04-17 06:58:43.614910

# update: 2026-04-18 06:14:28.877424

# update: 2026-04-19 06:48:03.478782

# update: 2026-04-20 07:18:35.122777

# update: 2026-04-21 06:59:27.839562

# update: 2026-04-22 06:58:53.097071

# update: 2026-04-23 07:01:53.791538

# update: 2026-04-24 07:05:01.656629

# update: 2026-04-25 06:21:19.033076

# update: 2026-04-26 06:59:58.189257

# update: 2026-04-27 07:35:55.775534

# update: 2026-04-28 07:32:32.888115

# update: 2026-04-29 07:25:43.332644

# update: 2026-04-30 07:29:36.594314

# update: 2026-05-01 07:27:00.181768

# update: 2026-05-02 07:02:22.045918

# update: 2026-05-03 07:20:43.549605
