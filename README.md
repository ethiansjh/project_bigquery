# Project BigQuery
La donnée brute avec explications du dataset est ici : https://www.kaggle.com/competitions/spaceship-titanic/data?select=train.csv
Les consignes pour aujourd'hui :
Loader la donnée sur BigQuery
Créer un notebook pour prototyper la logique d'entrainement, le workflow devra être :
1. Loader la donnée de BQ dans un Dataframme
2. Nettoyer la donnée
3. Instancier un modèle
4. Entrainer le modele et l'upload sur Cloud Storage
Une fois que votre prototype marche, packager votre code sous forme de fonction

# ML Workflow
1.Download Raw data (internet)
2.Import data to the gcp cloud storage 
3.Process Data (train) 
4.Export trained data to Cloud Storage
5.Read data in Bigquery from Cloud Storage 
