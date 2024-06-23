import boto3
import os

S3_BUCKET = 'cpu-monitoring-app'
LOCAL_DIRECTORY = 'D:\Monitoring-application'  
s3_client = boto3.client('s3')

def upload_directory_to_s3(local_directory, bucket_name):
    for root, dirs, files in os.walk(local_directory):
        for file in files:
            local_path = os.path.join(root, file)
            relative_path = os.path.relpath(local_path, local_directory)
            s3_path = relative_path.replace("\\", "/")  # For Windows compatibility

            print(f'Uploading {local_path} to s3://{bucket_name}/{s3_path}')
            s3_client.upload_file(local_path, bucket_name, s3_path)

if __name__ == "__main__":
    upload_directory_to_s3(LOCAL_DIRECTORY, S3_BUCKET)
