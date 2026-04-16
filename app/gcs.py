from google.cloud import storage
import os
import json 

BUCKET_NAME = os.getenv("BUCKET_NAME" )
FILE_NAME = os.getenv("FILE_NAME")

def read_json_from_gcs():
    client = storage.Client()
    bucket = client.bucket(BUCKET_NAME)
    blob = bucket.blob(FILE_NAME)

    content = blob.download_as_text()
    return json.loads(content)


