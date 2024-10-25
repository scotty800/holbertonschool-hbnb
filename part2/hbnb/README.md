![images (1)](https://github.com/user-attachments/assets/8406017c-c847-43fd-b88c-d5bc6c3c115f)

# HBnB Application - Initial Project Setup

### Description
This project is a Flask-based application designed to manage users, places, reviews, and amenities for a lodging reservation platform, similar to Airbnb. This README.md file describes the project structure and provides instructions for setting up the application.

In this stage, we’ve set up the basic project structure, including the Presentation layer (API), Business Logic, and Data Persistence (currently in memory). The in-memory storage logic will later be replaced with a database. The Facade design pattern is also implemented to manage communication between these layers.

## Project Structure
The project is organized modularly into three main layers:
Presentation Layer (API)
Business Logic
Data Persistence (In-Memory Repository)

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

### Folder Explanations:
- `app`/ : Contains all the application codeon.
    - `api`/ :Manages API entry points (routes). Endpoints for managing `users`, `places`, `reviews`, and `amenities` are defined here.
    - `models`/ : Contains classes representing business objects (`User`, `Place`, `Review`, `Amenity`).
    - `services`/ :Contains the HBnBFacade class, which centralizes interactions between the different layers (API, Business Logic, Persistence).
    - `persistence`/ :  Contains the in-memory storage repository to simulate data persistence before using a real database.
- `run.py` : Main file to launch the Flask application.
- `config.py` : Application configuration file, including environment variables and debug options.
- `requirements.txt` :List of Python libraries required for the project (Flask, Flask-RESTx, etc.).
- `README.md` : This file, which provides a project description and installation instructions.

## Prerequisites
Before running the application, make sure you have the following installed:

- Python 3.x
-pip (the Python package manager)
### 1. Clonez le dépôt :
```

git clone https://github.com/votre-repo/hbnb.git
cd hbnb

```

### 2. Install dependencies: :

Use the requirements.txt file to install the necessary libraries:
```
    pip install -r requirements.txt

```

## Configuration
The `config.py` file contains the application’s basic configuration. Currently, it uses a default secret key and enables debug mode for the development environment. You can adjust these settings as needed.

## Running the Application

1. Start the Flask application by running the following command:

2. Access the application:

Open your browser and go to the following address to see the application running:
```
http://127.0.0.1:5000
```

At this stage, no routes are defined yet, but the application is ready for development.

## Features
- Modular Organization: The project structure follows a modular architecture, facilitating the management and addition of new features..
- Facade Pattern: Simplifies interactions between the layers (API, business logic, persistence)..
- In-Memory Repository: Allows temporary storage of objects before integrating a database.

## Prochaines Étapes
- Add API routes to manage users, places, reviews, and amenities.
- Implement CRUD functionalities in the in-memory repository.
- Replace the in-memory repository with a real database (SQLAlchemy) in the next project stage.
- Add tests to validate API functionality.

## Ressources
- [Flask Documentation](https://flask.palletsprojects.com/en/stable/)
- [Flask-RESTx Documentation](https://flask-restx.readthedocs.io/en/latest/)
- [Best Practices for Structuring a Python Project](https://docs.python-guide.org/writing/structure/)
- [Facade Design Pattern](https://refactoring.guru/design-patterns/facade/python/example)

## Auteurs

[Yannis Ranguin](https://github.com/Yannis95200)

[Scotty Ndanga](https://github.com/scotty800)

[Antonin Noyelle](https://github.com/Ninotna)

