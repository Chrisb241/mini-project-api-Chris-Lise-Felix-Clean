# Mini Projet API - Chris, Lise, Félix
API REST développée avec Flask, déployée sur Google Cloud Run, utilisant Google Cloud Storage et Vertex AI.

## Endpoints

| Méthode | Endpoint | Description |
|---------|----------|-------------|
| GET | `/hello` | Message de bienvenue |
| GET | `/status` | Date et heure du serveur |
| GET | `/data` | Lit le fichier JSON depuis GCS |
| POST | `/data` | Ajoute une entrée dans le fichier GCS |
| GET | `/poem` | Génère un poème via Vertex AI (Gemini) |

## Lancer en local

### Prérequis
- Python 3.11+
- Un compte de service GCP avec accès GCS et Vertex AI
- Un bucket GCS créé

### Installation

```bash
git clone https://github.com/Chrisb241/mini-project-api-Chris-Lise-Felix-Clean.git
cd mini-project-api-Chris-Lise-Felix-Clean
pip install -r requirements.txt
```

### Variables d'environnement

```bash
export BUCKET_NAME=mini-projet-chris-lise-123
export FILE_NAME=data.json
export GCP_PROJECT_ID=datatools-493010
export GCP_LOCATION=europe-west1
export GOOGLE_APPLICATION_CREDENTIALS=chemin/vers/service-account-key.json
```

### Lancement

```bash
python -m flask --app app.main run --host=0.0.0.0 --port=8080
```

## Build Docker

```bash
docker build --platform linux/amd64 -t chrisb045/mini-api:v2 .
docker push chrisb045/mini-api:v2
```

## Déploiement Cloud Run

```bash
gcloud run deploy mini-api \
  --image docker.io/chrisb045/mini-api:v2 \
  --platform managed \
  --region europe-west1 \
  --allow-unauthenticated \
  --port 8080 \
  --set-env-vars BUCKET_NAME=mini-projet-chris-lise-123,FILE_NAME=data.json,GCP_PROJECT_ID=datatools-493010,GCP_LOCATION=europe-west1
```

## Liens

- API déployée : https://mini-api-119046353840.europe-west1.run.app
- Image Docker Hub : https://hub.docker.com/r/felixmartinet/flask-vertex-api

## Répartition des rôles

| Membre | Contribution |
|--------|-------------|
| Chris (Chrisb241) | Initialisation Flask, endpoints `/hello`, `/status`, `/data` GET, endpoint `/poem` Vertex AI |
| Lise (lisecolinot-hash) | Endpoint `POST /data`, fonction `write_to_gcs`, intégration GCS écriture |
| Félix (felixmartinet) | Dockerfile, `.gitignore`, `requirements.txt`, configuration GCP, déploiement Cloud Run |
