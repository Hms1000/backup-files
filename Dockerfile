# i use a python baseline image
FROM python:3.12-slim AS builder

# make sure that unnecessary meta data is not downloaded
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# get updated packages
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/* 

# I setup working directory
WORKDIR /build

# upgrade pip
RUN python -m pip install --no-cache-dir --upgrade pip

#Copy requirements
COPY requirements.txt .

#create wheels
RUN pip wheel --no-cache-dir --no-deps \ 
    --wheel-dir /build/wheels -r requirements.txt


# Runner stage
FROM python:3.12-slim AS runner

# create working directory
WORKDIR /app

# create the user
RUN useradd -u 1000 -m appuser

# upgrade pip
RUN python -m pip install --no-cache-dir --upgrade pip

# handover wheels to runner
COPY --from=builder /build/wheels /wheels

# install wheels
RUN pip install --no-cache-dir /wheels/*.whl

# copy source code and ensure that the files are not owned by root
COPY --chown=appuser:appuser src/ .

# ensure the app is healthy
HEALTHCHECK --interval=30s --timeout=5s --retries=3 --start-period=40s CMD python -c "import urllib.request; urllib.request.urlopen('http://127.0.0.1:8000/health')"
EXPOSE 8000

# the container will stop running as root and will run as appuser now
USER appuser

# i execute the script
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
