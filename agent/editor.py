from brain import generate_code_edit


def apply_ai_edit(file_path):
    with open(file_path, "r") as f:
        original = f.read()

    updated = generate_code_edit(file_path, original)

    # basic safety: don't overwrite empty response
    if len(updated.strip()) < 10:
        return False

    with open(file_path, "w") as f:
        f.write(updated)

    return True