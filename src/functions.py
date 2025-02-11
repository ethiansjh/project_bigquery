from google.cloud import bigquery
from google.cloud import storage
import os

# connexion à api google cloud par la clé SA (clé à copier sous le répertoire credentials/)
def gcp_client_auth(key_json_file):
    try:
        storage_client = storage.Client.from_service_account_json(key_json_file)
        bigquery_client = bigquery.Client.from_service_account_json(key_json_file)  
        return storage_client, bigquery_client
    except Exception as e:
        print(f"Error connecting to Google Cloud: {e}")
        exit(1) # Exit with an error code

def import_data_to_bq_from_cs(bigquery_client, table_name, bucket_name, blob_name, table_id):
    job_config = bigquery.LoadJobConfig(
    autodetect=True, source_format=bigquery.SourceFormat.CSV, skip_leading_rows=1, write_disposition=bigquery.WriteDisposition.WRITE_APPEND
    )
    uri = "gs://{bucket_name}/{blob_name}"
    # gs://projectbigquery/data/train.csv
    uri = uri.format(bucket_name=bucket_name, blob_name=blob_name)
    load_job = bigquery_client.load_table_from_uri(
        uri, table_id, job_config=job_config
    )  # Make an API request.
    load_job.result()  # Waits for the job to complete.
    destination_table = bigquery_client.get_table(table_id)
    print("Loaded {} rows.".format(destination_table.num_rows))

def get_data_from_bq(bigquery_client, table_name):
    dataset_ref = bigquery.DatasetReference(project, dataset_id)
    table_ref = dataset_ref.table(table_name)
    print("Table reference:", table_ref)
    df = bigquery_client.list_rows(table_ref).to_dataframe()
    print("Data frame: ", df)
    return df

def push_data_to_cs(storage_client, bucket_name, destination_blob_name, table_name):
    bucket_name = bucket_name
    blob_name = table_name + "/" + destination_blob_name
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)
    blob.upload_from_filename(destination_blob_name)
    print(f"File uploaded to gs://{bucket_name}/{blob_name}")

# Clé Json Service Account GCP à mettre dans le dossier credentials
key_json_file = "credentials/devops-practice-449210-bigquery-editor.json"
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = key_json_file

# GCP static variables
project = "devops-practice-449210"
dataset_id = "project_bigquery"
table_name = "Titanic"
bucket_name = "projectbigquery"
table_id = "devops-practice-449210.project_bigquery.Titanic"

# local variables
raw_data_file_name = "data/train.csv"
pickle_file_name = "data/model.pkl"
processed_data_file_name = "data/Spaceship_Titanic_Preprocessed.csv"
blob_name = "data/train.csv"

# gcp client auth
# storage_client, bigquery_client = gcp_client_auth(key_json_file)

