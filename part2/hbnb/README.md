# HBnB Application - Initial Project Setup

### Description
Ce projet est une application basée sur Flask qui servira à gérer les utilisateurs, les lieux, les avis et les commodités (amenities) pour une plateforme de réservation de logements, semblable à Airbnb. Ce fichier README.md décrit la structure du projet et fournit des instructions pour configurer l'application.

Dans cette étape, nous avons mis en place la structure de base du projet, y compris les couches de Présentation (API), Logique Métier, et Persistance des données (en mémoire pour l'instant). La logique de stockage en mémoire sera remplacée par une base de données dans les étapes suivantes. Le modèle de conception Façade est également mis en place pour gérer les communications entre ces couches.

## Structure du Projet
Le projet est organisé de manière modulaire en trois couches principales :

Couches de Présentation (API)
- Logique Métier
- Persistance des Données (In-Memory Repository)
- Voici l'arborescence des fichiers :

```text
hbnb/
├── app/
│   ├── __init__.py
│   ├── api/
│   │   ├── __init__.py
│   │   ├── v1/
│   │       ├── __init__.py
│   │       ├── users.py
│   │       ├── places.py
│   │       ├── reviews.py
│   │       ├── amenities.py
│   ├── models/
│   │   ├── __init__.py
│   │   ├── user.py
│   │   ├── place.py
│   │   ├── review.py
│   │   ├── amenity.py
│   ├── services/
│   │   ├── __init__.py
│   │   ├── facade.py
│   ├── persistence/
│       ├── __init__.py
│       ├── repository.py
├── run.py
├── config.py
├── requirements.txt
├── README.md
```

### Explication des dossiers :
- app/ : Contient l'ensemble du code de l'application.
    - api/ : Gère les points d'entrée API (routes). Les endpoints pour gérer les utilisateurs, les lieux, les avis et les commodités seront définis ici.
    - models/ : Contient les classes représentant les objets métier (Utilisateur, Lieu, Avis, Commodité).
    - services/ : Contient la classe HBnBFacade, qui centralise les interactions entre les différentes couches (API, Logique Métier, Persistance).
    - persistence/ : Contient le dépôt de stockage en mémoire pour simuler la persistance des données avant d’utiliser une base de données réelle.
- run.py : Fichier principal qui permet de lancer l'application Flask.
- config.py : Fichier de configuration de l'application, incluant les variables d'environnement et les options de debug.
- requirements.txt : Liste des bibliothèques Python nécessaires au projet (Flask, Flask-RESTx, etc.).
- README.md : Ce fichier, qui fournit une description du projet et des instructions d'installation.

## Prérequis
Avant de pouvoir exécuter l'application, assurez-vous d'avoir installé les éléments suivants :

- Python 3.x
- pip (le gestionnaire de paquets Python)
Installation
### 1. Clonez le dépôt :
```

git clone https://github.com/votre-repo/hbnb.git
cd hbnb

```

### 2. Installez les dépendances :

Utilisez le fichier requirements.txt pour installer les bibliothèques nécessaires :
```
    pip install -r requirements.txt

```

## Configuration
Le fichier `config.py` contient la configuration de base de l'application. Actuellement, il utilise une clé secrète par défaut et active le mode debug pour l'environnement de développement. Vous pouvez ajuster ces paramètres en fonction de vos besoins.

## Lancer l'application

1. Démarrez l'application Flask en exécutant la commande suivante :
python run.py

2. Accédez à l'application :

Ouvrez votre navigateur et allez à l'adresse suivante pour voir l'application en cours d'exécution :
```
http://127.0.0.1:5000
```

À ce stade, il n'y a pas encore de routes définies, mais l'application est prête à être développée.

## Fonctionnalités
- Organisation modulaire : La structure du projet suit une architecture modulaire, facilitant la gestion et l’ajout de nouvelles fonctionnalités.
- Modèle Façade : Simplifie les interactions entre les couches (API, logique métier, persistance).
- Dépôt en mémoire : Permet de stocker temporairement des objets avant l'intégration d'une base de données.

## Prochaines Étapes
- Ajouter les routes de l'API pour gérer les utilisateurs, les lieux, les avis, et les commodités.
- Implémenter les fonctionnalités CRUD dans le dépôt en mémoire.
- Remplacer le dépôt en mémoire par une base de données réelle (SQLAlchemy) dans la prochaine étape du projet.
- Ajouter des tests pour valider le bon fonctionnement de l'API.

## Ressources
- Documentation Flask
- Documentation Flask-RESTx
- Meilleures pratiques pour structurer un projet Python
- Modèle de conception Façade

## Auteurs





