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

    def download_file(self, filepath: str, target_path: str = None):
        """
        Download a single file from S3 to local

        Returns
        -------
        Path to created file
        """
        file = filepath.split("/")[-1]
        path = filepath.split(file)[0]
        if target_path:
            self.s3client.download_file(Bucket=self.bucket_name,
                                        Key=path + file,
                                        Filename=target_path + file)
            return target_path + file
        else:
            self.s3client.download_file(Bucket=self.bucket_name,
                                        Key=path + file,
                                        Filename=file)
            return file

    def list_buckets(self):
        """
        Show all buckets in S3
        Returns
        -------
        List of string
        """
        response = self.s3client.list_buckets()
        return [bucket["Name"] for bucket in response["Buckets"]]

    def list_objects(self, bucket_name: str, prefix: str = None):
        """
        Returns a list of all objects with specified prefix.

        Returns
        -------
        List of string
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

    def upload_file(self, filepath: str, target_path: str = None):
        """
        Uploading a single file to S3

        Parameters
        ----------
        filepath
        target_path

        Returns
        -------
        None
        """
        if target_path:
            self.s3client.upload_file(Filename=filepath,
                                      Bucket=self.bucket_name,
                                      Key=target_path)
        else:
            self.s3client.upload_file(Filename=filepath,
                                      Bucket=self.bucket_name,
                                      Key="")
