from boto3.session import Session
from boto3 import client


class S3Connector:
    def __init__(self, bucket_name: str):
        self.bucket_name = bucket_name
        self.s3client = client('s3')
        self.bucket = Session().resource('s3').Bucket(bucket_name)

    def download_file(self, filepath: str, target_path: str):
        file = filepath.split("/")[-1]
        path = filepath.split(file)[0]
        self.s3client.download_file(self.bucket_name, path + file, target_path+file)

    def list_buckets(self):
        """Returns a list of bucket names."""
        response = self.s3client.list_buckets()
        return [bucket["Name"] for bucket in response["Buckets"]]

    def list_objects(self, bucket_name, prefix):
        """Returns a list of all objects with specified prefix."""
        response = self.s3client.list_objects(
            Bucket=bucket_name,
            Prefix=prefix,
        )
        return [object["Key"] for object in response["Contents"]]
