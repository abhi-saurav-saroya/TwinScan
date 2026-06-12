import os


def is_path_valid(folder_path: str) -> bool:
    return os.path.isdir(folder_path)