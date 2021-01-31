from typing import Union


def extract_filename(file_path: Union[list, str],
                     file_ext: bool = True) -> dict:
    """
    Takes in a file_path or a list of file paths and returns a dict

    Returns
    dict(file_path: file_name)
    """
    if type(file_path) is not list:
        file_path = [file_path]

    file_names = {}
    for single_path in file_path:
        if "/" in single_path:
            file_name = single_path.split("/")[-1]
        else:
            file_name = single_path
        if file_name == ".":
            file_name = ""
        if file_ext:
            file_names[single_path] = file_name
        else:
            file_names[single_path] = ".".join(file_name.split(".")[:-1])

    return file_names
