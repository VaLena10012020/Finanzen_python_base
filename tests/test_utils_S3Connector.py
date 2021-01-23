import boto3
import os
import pytest
from tempfile import NamedTemporaryFile

from finanzen_base.Utils.S3Connector import S3Connector

from moto import mock_s3, mock_sqs


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
        conn = boto3.client("s3", region_name="us-east-1")
        yield conn


@pytest.fixture
def sqs_client(aws_credentials):
    with mock_sqs():
        conn = boto3.client("sqs", region_name="us-east-1")
        yield conn


@pytest.fixture
def bucket_name():
    return "my-test-bucket"


@pytest.fixture
def s3_test(s3_client, bucket_name):
    s3_client.create_bucket(Bucket=bucket_name)
    yield


def test_list_buckets(s3_client, s3_test):
    my_client = S3Connector("my-test-bucket")
    buckets = my_client.list_buckets()
    assert buckets == ["my-test-bucket"]


def test_list_objects(s3_client, s3_test):
    file_text = "test"
    with NamedTemporaryFile(delete=True, suffix=".txt") as tmp:
        with open(tmp.name, "w", encoding="UTF-8") as f:
            f.write(file_text)

        s3_client.upload_file(tmp.name, "my-test-bucket", "file12")
        s3_client.upload_file(tmp.name, "my-test-bucket", "file22")

    my_client = S3Connector("my-test-bucket")
    objects = my_client.list_objects(bucket_name="my-test-bucket", prefix="file1")
    assert objects == ["file12"]


def test_show_bucket_files(s3_client, s3_test):
    file_text = "test"
    with NamedTemporaryFile(delete=True, suffix=".txt") as tmp:
        with open(tmp.name, "w", encoding="UTF-8") as f:
            f.write(file_text)

        s3_client.upload_file(tmp.name, "my-test-bucket", "file12")
        s3_client.upload_file(tmp.name, "my-test-bucket", "file22")
    my_client = S3Connector("my-test-bucket")
    files = my_client.show_bucket_files()
    assert type(files) is list
    assert files[0] == "file12"
