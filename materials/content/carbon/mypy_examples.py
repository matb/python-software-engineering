import pathlib


def read_file_content(file: pathlib.Path):
    print(file.read_text("utf-8"))

read_file_content(pathlib.Path("example.txt")) # Error not supported
read_file_content("example.txt") # Works fine
