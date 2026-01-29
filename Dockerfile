# i use a python baseline image
FROM python:3.11-slim As builder

# make sure that unnecessary meta data is not downloaded
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# get updated pacakges
RUN apt-get update && apt-get upgrade -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/* 

# i setup working directory
WORKDIR /build

# upgrade pip
RUN python -c pip install --no-cacher-dir --upgrade pip

#Copy requirements
COPY requirements.txt .

#create wheels
RUN pip wheel --no-cache-dir --no-deps --wheel-dir /build/wheels -r requirements.txt


# Runner stage
FROM python:3.12-slim As runner

# create working directory
WORKDIR /app

# upgrade pip
RUN pip install --no-cacher-dir --upgrade pip

#create user
RUN useradd -u 1000 -m appuser

# handover wheels to runner
COPY --from=builder /build/wheels /wheels

# install wheels
RUN pip install --no-cacher-dir /wheels*

# ensure that the files are not owned by root
USER --chown=appuser:appuser

# ensure the app is healthy
HEALTHCHECK --interval=30s --timeout=5s --retries=3 --start-time=40s
           CMD python -c "import urllib.request; urlib.request.open('http://127.0.0.1/health:8000') || exit 1"

EXPOSE 8000

# i execute the script
CMD ["python3", "backu=p-files.py"]
