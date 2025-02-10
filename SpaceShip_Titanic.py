from google.cloud import storage
bucket_name = "projectbigquery"
destination_blob_name = "project_bigquery/SpaceShip_Titanic/Spaceship_Titanic_Preprocessed2.csv"  # or "data.json"
client = storage.Client()
bucket = client.bucket(bucket_name)
blob = bucket.blob(destination_blob_name)
blob.upload_from_filename("Spaceship_Titanic_Preprocessed2.csv")  # or "data.json"
print(f"File uploaded to gs://{bucket_name}/{destination_blob_name}")