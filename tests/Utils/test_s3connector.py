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
    _ = my_client.download_file(filenames[0])
    assert filenames[0] in os.listdir()
    os.remove(filenames[0])


def test_upload_file(s3_client, s3_test, bucket_name):
    file_text = "test"
    filenames = ["file12", "file22"]
    my_client = S3Connector(bucket_name)
    with NamedTemporaryFile(delete=True, suffix=".txt") as tmp:
        with open(tmp.name, "w", encoding="UTF-8") as f:
            f.write(file_text)
        for file in filenames:
            my_client.upload_file(tmp.name, file)
    objects = my_client.list_objects(bucket_name=bucket_name, prefix="file")
    assert filenames[0] in objects
