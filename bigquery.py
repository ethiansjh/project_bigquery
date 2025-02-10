from google.cloud import bigquery
from google.cloud import storage

# connect to api client avec service account key (clé à copier sous le répertoire credentials)
def gcp_client_auth(key_json_file):
    try:
        storage_client = storage.Client.from_service_account_json(key_json_file)
        bigquery_client = bigquery.Client.from_service_account_json(key_json_file)  
        return storage_client, bigquery_client
    except Exception as e:
        print(f"Error connecting to Google Cloud: {e}")
    exit(1) # Exit with an error code

def get_data_set(bigquery_client, table):
    dataset_ref = bigquery.DatasetReference(project, dataset_id)
    table_ref = dataset_ref.table(table)
    print(table)
    df = bigquery_client.list_rows(table_ref).to_dataframe()
    print(df)
    #return df

def push_data_set(storage_client, bucket_name, destination_blob_name):
    bucket_name = "projectbigquery"
    destination_blob_name = "Titanic/Spaceship_Titanic_Preprocessed2.csv"  # or "data.json"
    client = storage.Client()
    bucket = client.bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)
    blob.upload_from_filename("SpaceShip_Titanic/Spaceship_Titanic_Preprocessed2.csv")  # or "data.json"
    print(f"File uploaded to gs://{bucket_name}/{destination_blob_name}")

# Variables.  Make sure these match your project and dataset.
key_json_file = "credentials/devops-practice-449210-bigquery-editor.json"
project = "devops-practice-449210"
dataset_id = "project_bigquery"
table = "Titanic"
bucket_name = "projectbigquery"
destination_blob_name = "project_bigquery/SpaceShip_Titanic/Spaceship_Titanic_Preprocessed2.csv"


storage_client, bigquery_client = gcp_client_auth(key_json_file)
get_data_set(bigquery_client, table) 
push_data_set(storage_client, bucket_name, destination_blob_name)
