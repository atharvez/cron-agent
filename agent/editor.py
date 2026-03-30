import datetime


def apply_simple_edit(file_path):
    try:
        with open(file_path, "a") as f:
            f.write(f"\n# update: {datetime.datetime.now()}\n")
        return True
    except:
        return False