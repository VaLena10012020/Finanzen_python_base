from typing import Union


def extract_filename(file_path: Union[list, str]) -> list:
    """
    Takes in a file_path or a list of file paths and returns only the file name
    """
    def extract_filename_single(path: str):
        if "/" in path:
            file_name = path.split("/")[-1]
        else:
            file_name = path
        if file_name == ".":
            file_name = ""
        return file_name

    if type(file_path) is not list:
        file_path = [file_path]

    file_name = []
    for single_path in file_path:
        file_name.append(extract_filename_single(single_path))

    return file_name
