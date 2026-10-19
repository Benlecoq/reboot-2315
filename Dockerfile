FROM python:3.10-slim

COPY requirements.txt requirements.txt
COPY api_folder api_folder
COPY models models

RUN pip install -r requirements.txt

# Local
#CMD uvicorn api_folder.api_file:app --host 0.0.0.0

# Deployment
CMD uvicorn api_folder.api_file:app --host 0.0.0.0  --port $PORT
