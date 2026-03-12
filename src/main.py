from fastapi import FastAPI
from pathlib import Path
from backup_files import backup_file

# fastapi client 
app = FastAPI()

# checking if the api is accessible
@app.get("/")
def home():
    return {"status": "Backup service running..."}

# perfoming the backup
@app.post("/backup")
def post_backup(path_to_backup:str, destination: str):
    
    backup_file(
            Path(path_to_backup),
            Path(destination)
            )
    return {"status": "backup completed"}

# simple healthcheck
@app.get("/heath")
def healthcheck():
    return {"status": "healthy"}
