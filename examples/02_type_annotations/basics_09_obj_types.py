from pprint import pprint
from pathlib import Path


def add_path_to_files(path: Path, files: list[str]) -> list[Path]:
    full_path = [path / file for file in files]
    return full_path


if __name__ == "__main__":
    common_path = Path("/home/user1/data")
    # print(f"{common_path=}")
    file_list = ["file1.txt", "file2.txt"]
    pprint(add_path_to_files(common_path, file_list))
