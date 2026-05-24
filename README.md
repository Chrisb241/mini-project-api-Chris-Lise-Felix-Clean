# Mini Projet API Flask - GCP

## Description
API Flask déployée sur Google Cloud Run avec intégration Vertex AI pour la génération de poèmes.

## Endpoints
- `GET /hello` → message de bienvenue
- `GET /status` → date/heure serveur
- `GET /data` → lit un fichier JSON depuis GCS
- `POST /data` → ajoute une entrée dans GCS
- `GET /poem` → génère un poème via Gemini AI

## Exécution en local
```bash
cat > README.md << 'EOF'
# Mini Projet API Flask - GCP

## Description
API Flask déployée sur Google Cloud Run avec intégration Vertex AI pour la génération de poèmes.

## Endpoints
- `GET /hello` → message de bienvenue
- `GET /status` → date/heure serveur
- `GET /data` → lit un fichier JSON depuis GCS
- `POST /data` → ajoute une entrée dans GCS
- `GET /poem` → génère un poème via Gemini AI

## Exécution en local
```bash
pip install -r requirements.txt
export GEMINI_API_KEY=ta-clé
python -m flask --app app.main run --host=0.0.0.0 --port=8080
```

## Build Docker
```bash
docker build -t flask-vertex-api .
docker run -p 8080:8080 -e GEMINI_API_KEY=ta-clé flask-vertex-api
```

## Déploiement Cloud Run
```bash
docker buildx build --platform linux/amd64 -t europe-west1-docker.pkg.dev/PROJECT_ID/flask-api/flask-vertex-api --push .
gcloud run deploy flask-vertex-api --image europe-west1-docker.pkg.dev/PROJECT_ID/flask-api/flask-vertex-api --platform managed --region europe-west1 --allow-unauthenticated
```

## URL Cloud Run
https://flask-vertex-api-685634288851.europe-west1.run.app

## Membres de l'équipe
- **Félix** : endpoint /poem, Dockerfile, déploiement Cloud Run
- **Chris** : endpoint /data, module GCS
- **Lise** : endpoint /hello, /status
