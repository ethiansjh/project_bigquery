# Project BigQuery
La donnée brute avec explications du dataset est ici : https://www.kaggle.com/competitions/spaceship-titanic/data?select=train.csv

1. Loader la donnée sur BigQuery
2. Créer un notebook pour prototyper la logique d'entrainement, le workflow devra être :
3. Loader la donnée de BQ dans un Dataframme
4. Nettoyer la donnée
5. Instancier un modèle
6. Entrainer le modele et l'upload sur Cloud Storage
7. Une fois que votre prototype marche, packager votre code sous forme de fonction

# ML Workflow
1. Download Raw data csv (internet) 
2. Import data to the gcp cloud storage 
3. Process Data (train)
4. Export trained data to Cloud Storage (pkl, csv)
5. Read data in Bigquery from Cloud Storage

# FastAPI
1. Construire une API avec fastapi (back) pour faire une prédiction avec le model, il faudra loader le modèle depuis GCS !
3. Construire  un streamlit pour faire une interface graphique sur cette api
4. Tester l'api et le bact en local
5. Deployer l'API sur CLoud RUN
6. Deployer le streamlit sur streamlit share

# Dockerisation
1. Créer dockerfile
2. dockeriser les services (build & push to artifact gcp)
3. Créer un pipeline CI (depuis github actions ou autre)
4. Déployer les containers
5. Mise en service