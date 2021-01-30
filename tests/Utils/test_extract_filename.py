from finanzen_base.Utils.extract_filename import extract_filename


def test_list_of_files():
    file_paths = ["test1/test2/test.csv", "test1/test3/test2.csv", "test.csv"]
    file_names = extract_filename(file_paths)
    assert file_names == ["test.csv", "test2.csv", "test.csv"]


def test_single_file():
    file_paths = ["test1/test2/test.csv"]
    file_names = extract_filename(file_paths)
    assert file_names == ["test.csv"]


def test_single_file_string():
    file_paths = "test1/test2/test.csv"
    file_names = extract_filename(file_paths)
    assert file_names == ["test.csv"]
