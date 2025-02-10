from google.cloud import bigquery
from google.cloud import storage

# connect to api client avec service account key (clé à copier sous le répertoire credentials)
try:
    storage_client = storage.Client.from_service_account_json("credentials/devops-practice-449210-bigquery-editor.json")
    bigquery_client = bigquery.Client.from_service_account_json("credentials/devops-practice-449210-bigquery-editor.json")  
except Exception as e:
    print(f"Error connecting to Google Cloud: {e}")
    exit(1) # Exit with an error code

# Variables.  Make sure these match your project and dataset.
project = "devops-practice-449210"
dataset_id = "project_bigquery"
table = "Titanic"

dataset_ref = bigquery.DatasetReference(project, dataset_id)
table_ref = dataset_ref.table("Titanic")
table = bigquery_client.get_table(table_ref)
print(table)
df = bigquery_client.list_rows(table).to_dataframe()
print(df)
