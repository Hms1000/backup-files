# i use a python baseline image
FROM python:3.11-slim

# i setup working directory
WORKDIR /app
 
# i copy dependencies to the contaniner
COPY requirements.txt .

# i install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# i then copy the rest of the file contents to the container from the soource directory
COPY src/ .

# i declared a volume to store data locally (i will use this later for in test and deploy jobs)
#VOLUME ["/app/data"]

# i execute the script
CMD ["python3", "backup-files.py"]
