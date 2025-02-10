from google.cloud import bigquery
from google.oauth2 import service_account

key_path = "credentials/devops-practice-449210-bigquery-editor.json"
credentials = service_account.Credentials.from_service_account_file(
    key_path,
    scopes=["https://www.googleapis.com/auth/cloud-platform"],
)

client = bigquery.Client(
    credentials=credentials,
    project=credentials.project_id,
)

project = "devops-practice-449210"
dataset_id = "project_bigquery"
dataset_ref = bigquery.DatasetReference(project, dataset_id)
try:
    table_ref = dataset_ref.table("Titanic")
    table = client.get_table(table_ref)
    df = client.list_rows(table).to_dataframe()
    print(df.head())
except Exception as e:
    print(f"An error occurred: {e}")
    if "Table" in str(e) and "does not exist" in str(e):
        print("Please create the table 'Titanic' in the specified dataset.")
    elif "Dataset" in str(e) and "does not exist" in str(e):
        print("Please create the dataset 'project_bigquery' in the specified project.")

