# Blog API

Bienvenue dans la documentation de l'API de Blog.

## Description

Cette API permet de gérer un blog avec des fonctionnalités telles que la création, la lecture, la mise à jour et la suppression d'articles de blog.

## Prérequis

- Python 3.x
- pip
- virtualenv
- Node.js
- npm

## Installation

1. Clonez le dépôt :
   ```bash
   git clone https://github.com/Franckfetuedirane/blog_api.git
   ```
2. Accédez au répertoire du projet :
   ```bash
   cd blog_api
   ```
3. Créez un environnement virtuel :
   ```bash
   virtualenv venv
   ```
4. Activez l'environnement virtuel :
   - Sur Windows :
     ```bash
     venv\Scripts\activate
     ```
   - Sur macOS/Linux :
     ```bash
     source venv/bin/activate
     ```
5. Installez les dépendances :
   ```bash
   pip install -r requirements.txt
   ```

## Utilisation

Pour démarrer le serveur de développement :
```bash
python app.py
npm start
```

L'API sera disponible à l'adresse `http://127.0.0.1:8000`.

## Endpoints

- `GET /articles` : Récupère tous les articles de blog.
- `GET /articles/<id>` : Récupère un article de blog spécifique.
- `POST /articles` : Crée un nouvel article de blog.

## Autres
- `PUT /articles/<id>` : Met à jour un article de blog existant.
- `DELETE /articles/<id>` : Supprime un article de blog.

## Auteurs

- Tchumamo Franck Fetue Dirane
