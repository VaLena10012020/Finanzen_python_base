from boto3.session import Session
from boto3 import client


class S3Connector:
    def __init__(self, bucket_name: str):
        """
        Class for interacting with AWS S3 buckets
        """
        self.bucket_name = bucket_name
        self.s3client = client('s3')
        self.bucket = Session().resource('s3').Bucket(bucket_name)

    def download_file(self, file_path: str, target_path: str = None) -> str:
        """
        Download a single file from S3 to local

        Returns
        -------
        Path to created file
        """
        file_name = file_path.split("/")[-1]
        path = file_path.split(file_name)[0]
        if target_path:
            self.s3client.download_file(Bucket=self.bucket_name,
                                        Key=path + file_name,
                                        Filename=target_path + "/" + file_name)
            return target_path + "/" + file_name
        else:
            self.s3client.download_file(Bucket=self.bucket_name,
                                        Key=path + file_name,
                                        Filename=file_name)
            return file_name

    def list_buckets(self) -> list:
        """
        Show all buckets in S3
        """
        response = self.s3client.list_buckets()
        return [bucket["Name"] for bucket in response["Buckets"]]

    def list_objects(self, bucket_name: str, prefix: str = None) -> list:
        """
        Returns a list of all objects with specified prefix.

        """
        if prefix:
            response = self.s3client.list_objects(
                Bucket=bucket_name,
                Prefix=prefix,
            )
        else:
            response = self.s3client.list_objects(
                Bucket=bucket_name
            )
        return [object["Key"] for object in response["Contents"]]

    def upload_file(self, file_path: str, target_path: str = None) -> None:
        """
        Uploading a single file to S3
        """
        if target_path:
            self.s3client.upload_file(Filename=file_path,
                                      Bucket=self.bucket_name,
                                      Key=target_path)
            return target_path
        else:
            if "/" in file_path:
                target_path = file_path.split("/")[-1]
            else:
                target_path = file_path
            self.s3client.upload_file(Filename=file_path,
                                      Bucket=self.bucket_name,
                                      Key=target_path)
            return target_path
