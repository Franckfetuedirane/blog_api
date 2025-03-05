# filepath: /e:/Mon Bureau/OneDrive/Bureau/blog_api/Dockerfile
# Utiliser une image de base officielle de Python
FROM python:3.9-slim

# Définir le répertoire de travail dans le conteneur
WORKDIR /app

# Copier les fichiers de l'application dans le répertoire de travail
COPY . /app

# Installer les dépendances
RUN pip install --no-cache-dir -r requirements.txt

# Exposer le port sur lequel l'application va s'exécuter
EXPOSE 8000

# Exécuter Flake8 pour vérifier les conventions PEP8
RUN flake8 .
# Définir la commande par défaut pour exécuter l'application
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]