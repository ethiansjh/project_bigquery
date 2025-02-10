
from google.cloud import bigquery
client = bigquery.Client.from_service_account_json("credentials/service-account.json")
project = "devops-practice-449210"
dataset_id = "devops-practice-449210.project_bigquery"
dataset_ref = bigquery.DatasetReference(project, dataset_id)
table_ref = dataset_ref.table("students")
table = client.get_table(table_ref)
df = client.list_rows(table).to_dataframe()
df.head()
