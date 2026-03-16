from fastapi import FastAPI
from pathlib import Path
from backup_files import backup_file

app = FastAPI()

@app.get("/")
def home():
    return {"status": "Backup service running..."}

@app.post("/backup")
def post_backup(path_to_backup: str, destination: str):
    backup_file(
        Path(path_to_backup),
        Path(destination)
    )
    return {"status": "backup completed"}

@app.get("/health")
def healthcheck():
    return {"status": "healthy"}
