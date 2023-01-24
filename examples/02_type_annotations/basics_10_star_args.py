from pprint import pprint
from pathlib import Path


def add_path_to_files(path: Path, *files: str) -> list[Path]:
    full_path = [path / file for file in files]
    return full_path


if __name__ == "__main__":
    common_path = Path("/home/user1/data")
    pprint(add_path_to_files(common_path, "file.txt"))
    pprint(add_path_to_files(common_path, "file1.txt", "file2.txt"))
