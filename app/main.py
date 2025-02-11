from fastapi import FastAPI, Form, UploadFile
from fastapi.responses import HTMLResponse
import shutil
import os
import src.functions as func


app = FastAPI()

@app.route('/')
def index():
    return render_template('index.html')

@app.post("/uploadfile)")
async def upload_local_file_to_gcs(file: UploadFile = File(...)):
    if not file:
        return {"message": "No upload file sent"}
    else:
        local_path = f"/tmp{file.filename}"
        with open(local_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
        # Upload to GCS
        storage_client = func.gcp_client_auth(key_json_file)
        func.push_data_to_cs(storage_client, bucket_name, blob_name, local_path)
        return {"Uploaded File " : file.filename}