from boto3.session import Session
import boto3


class S3Connector:
    def __init__(self, bucket_name: str):
        self.bucket_name = bucket_name
        self.session = Session()
        self.s3_session = self.session.resource('s3')
        self.s3client = boto3.client('s3')
        self.bucket = self.s3_session.Bucket(bucket_name)

    def show_bucket_files(self):
        for s3_file in self.bucket.objects.all():
            print(s3_file.key)

    def download_file(self, filepath: str, target_path: str):
        file = filepath.split("/")[-1]
        path = filepath.split(file)[0]
        self.s3client.download_file(self.bucket_name, path + file, target_path+file)
