import os
from boto3 import client
import pytest
from moto import mock_s3
from tempfile import NamedTemporaryFile

from finanzen_base.Utils.s3connector import S3Connector


@pytest.fixture
def aws_credentials():
    """Mocked AWS Credentials for moto."""
    os.environ["AWS_ACCESS_KEY_ID"] = "testing"
    os.environ["AWS_SECRET_ACCESS_KEY"] = "testing"
    os.environ["AWS_SECURITY_TOKEN"] = "testing"
    os.environ["AWS_SESSION_TOKEN"] = "testing"


@pytest.fixture
def s3_client(aws_credentials):
    with mock_s3():
        conn = client("s3", region_name="us-east-1")
        yield conn


@pytest.fixture
def bucket_name():
    return "my-test-bucket"


@pytest.fixture
def s3_test(s3_client, bucket_name):
    s3_client.create_bucket(Bucket=bucket_name)
    yield


def test_list_buckets(s3_client, s3_test, bucket_name):
    my_client = S3Connector(bucket_name)
    buckets = my_client.list_buckets()
    assert buckets == [bucket_name]


def test_list_objects(s3_client, s3_test, bucket_name):
    file_text = "test"
    filenames = ["file12", "file22"]
    with NamedTemporaryFile(delete=True, suffix=".txt") as tmp:
        with open(tmp.name, "w", encoding="UTF-8") as f:
            f.write(file_text)
        for file in filenames:
            s3_client.upload_file(tmp.name, bucket_name, file)

    my_client = S3Connector(bucket_name)
    objects = my_client.list_objects(bucket_name=bucket_name, prefix="file")
    assert objects == filenames
    objects_no_prefix = my_client.list_objects(bucket_name=bucket_name)
    assert objects_no_prefix == filenames


def test_download_file(s3_client, s3_test, bucket_name):
    file_text = "test"
    filenames = ["file12", "file22"]
    with NamedTemporaryFile(delete=True, suffix=".txt") as tmp:
        with open(tmp.name, "w", encoding="UTF-8") as f:
            f.write(file_text)
        for file in filenames:
            s3_client.upload_file(tmp.name, bucket_name, file)

    my_client = S3Connector(bucket_name)

    # Test with default value for target_path
    _ = my_client.download_file(filenames[0])
    assert filenames[0] in os.listdir()

    # Test with value for target_path
    os.remove(filenames[0])
    test_dir = "data"
    os.mkdir("data")
    dir_s3 = my_client.download_file(file_path=filenames[0],
                                     target_path=test_dir)
    assert dir_s3 == test_dir+"/"+filenames[0]
    assert [filenames[0]] == os.listdir(test_dir)
    os.remove(dir_s3)
    os.rmdir(test_dir)


def test_upload_file(s3_client, s3_test, bucket_name):
    filenames = ["file12", "file22"]
    my_client = S3Connector(bucket_name)
    uploaded_files = []

    file_text = "test"
    with NamedTemporaryFile(delete=True, suffix=".txt") as tmp:
        tmp_file_path = tmp.name
        with open(tmp.name, "w", encoding="UTF-8") as f:
            f.write(file_text)
        # Case 1 file with default target_path
        uploaded_files.append(my_client.upload_file(file_path=tmp.name))
        # Case 2 target_path is subdir
        uploaded_files.append(my_client.upload_file(file_path=tmp.name,
                                                    target_path=tmp_file_path))
        # Case 3 target_path is new file name without subdir
        for file in filenames:
            uploaded_files.append(my_client.upload_file(file_path=tmp.name,
                                                        target_path=file))

    objects = my_client.list_objects(bucket_name=bucket_name)

    # Append name of temp file to filenames
    filenames.extend([tmp_file_path.split("/")[-1], tmp_file_path])
    # Check is files are uploaded
    assert set(filenames) == set(objects)
    # Check if return of upload file is correct
    assert set(filenames) == set(uploaded_files)
