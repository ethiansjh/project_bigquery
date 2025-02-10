from google.cloud import bigquery
from google.cloud import storage

# connexion à api google cloud par la clé SA (clé à copier sous le répertoire credentials/)
def gcp_client_auth(key_json_file):
    try:
        storage_client = storage.Client.from_service_account_json(key_json_file)
        bigquery_client = bigquery.Client.from_service_account_json(key_json_file)  
        return storage_client, bigquery_client
    except Exception as e:
        print(f"Error connecting to Google Cloud: {e}")
    exit(1) # Exit with an error code

#def import_data_to_bq_from_cs(bigquery_client, table_name):
#   table_id = f"{project}.{dataset_id}.{table_name}"

def get_data_from_bq(bigquery_client, table_name):
    dataset_ref = bigquery.DatasetReference(project, dataset_id)
    table_ref = dataset_ref.table(table_name)
    print(table_ref)
    df = bigquery_client.list_rows(table_ref).to_dataframe()
    print(df)
    return df

def push_data_to_cs(storage_client, bucket_name, destination_blob_name, table_name):
    bucket_name = bucket_name
    blob_name = table_name + "/" + destination_blob_name
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)
    blob.upload_from_filename(destination_blob_name)
    print(f"File uploaded to gs://{bucket_name}/{blob_name}")

# Variables, Make sure these match your project and dataset.
key_json_file = "credentials/devops-practice-449210-bigquery-editor.json"
project = "devops-practice-449210"
dataset_id = "project_bigquery"
table_name = "Titanic"
bucket_name = "projectbigquery"
raw_data_file_name = "data/train.csv"
processed_data_file_name = "data/Spaceship_Titanic_Preprocessed2.csv"

# gcp client auth
storage_client, bigquery_client = gcp_client_auth(key_json_file)

# export raw data to CS
push_data_to_cs(storage_client, bucket_name, raw_data_file_name, table_name)

# import data to bq from cs
import_data_to_bq_from_cs(bigquery_client, table_name)

# read data from bq
get_data_from_bq(bigquery_client, table_name)

# export processed data to CS
push_data_to_cs(storage_client, bucket_name, processed_data_file_name, table_name)