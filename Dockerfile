FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8080

ENV PORT=8080
ENV GCP_PROJECT_ID=project-3f443971-257c-4f30-9d3
ENV GCP_LOCATION=europe-west1

CMD ["python", "-m", "flask", "--app", "app.main", "run", "--host=0.0.0.0", "--port=8080"]
