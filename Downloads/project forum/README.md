# Forum API

## Description

API REST pour la gestion d'un forum développé avec Django et Django REST Framework. Cette API permet de gérer des forums, des sujets et des messages.

## Technologies Utilisées

- Python 3.12
- Django 5.x ou superieur
- Django REST Framework
- PostgreSQL
- Postman (pour la documentation de l'API)

## Installation

### Prérequis

- Python 3.12
- PostgreSQL

### Étapes

1. **Cloner le Repository**

   ```bash
   git clone https://github.com/Soimaial/projet_final_-forum.git
   cd forum_api

2.Créer et activer un environnement virtuel
    python -m venv env
#      Activation de l'environnement virtuel
    source env/bin/activate (Linux ou MacOS)
    env\Scripts\activate (Windows )

3.Installer les dépendances
    pip install -r requirements.txt

4. Créer et Configurer la base de données PostgreSQL
-Pour la création de la base de donnée lancer votre Pg Admin puis votre base

- pour la configuration de la base de donnée rendez-vous dans le settings de votre projet et cherchez la partie  Database puis faite ceci:

DATABASES = {
    'default': {
        "ENGINE": "django.db.backends.postgresql",
        "NAME":  "le nom de votre base de donnée",
        "USER": "postgres",
        "PASSWORD": "le mot de passe de votre postgresql",
        "HOST": "localhost",
        "PORT": "5432",

    }
}

 5.Faire et Appliquer les migrations

    -python manage.py makemigrations
    -python manage.py migrate
6. python manage.py runserver

7. Lancer le serveur de développement

    -python manage.py runserver
# Accédez à l'interface de votre api à l'adresse suivante : http://127.0.0.1:8000/api/