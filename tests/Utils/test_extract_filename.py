from finanzen_base.Utils.extract_filename import extract_filename


def test_list_of_files():
    file_paths = ["test1/test2/test.csv", "test1/test3/test2.csv", "test.csv"]
    file_names = extract_filename(file_paths)
    assert file_names == {file_paths[0]: "test.csv",
                          file_paths[1]: "test2.csv",
                          file_paths[2]: "test.csv"}


def test_single_file_list():
    file_paths = ["test1/test2/test.csv"]
    file_names = extract_filename(file_paths)
    assert file_names == {file_paths[0]: "test.csv"}


def test_single_file_string():
    file_paths = "test1/test2/test.csv"
    file_names = extract_filename(file_paths)
    assert file_names == {file_paths: "test.csv"}


def test_single_without_fileext():
    file_paths = ["test1/test2/test.csv",
                  "test1/test3/test2.csv",
                  "halo.test.csv"]
    file_names = extract_filename(file_paths, file_ext=False)
    assert file_names == {file_paths[0]: "test",
                          file_paths[1]: "test2",
                          file_paths[2]: "halo.test"}
