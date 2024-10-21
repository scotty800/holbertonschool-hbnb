
def main():
    from .facade import HBnBFacade
    # Initialiser le facade
    facade = HBnBFacade()

    # Créer un nouvel utilisateur
    user_data = {
        "first_name": "Alice",
        "last_name": "Smith",
        "email": "alice.smith@example.com"
    }

    new_user = facade.create_user(user_data)
    print(f"New User ID: {new_user.id}")

    # Créer un lieu avec l'ID du nouvel utilisateur
    place_data = {
        "title": "Cozy Apartment",
        "description": "A nice place to stay",
        "price": 100.0,
        "latitude": 37.7749,
        "longitude": -122.4194,
        "owner_id": new_user.id  # Utiliser l'ID du nouvel utilisateur
    }

    new_place = facade.create_place(place_data)
    print(f"New Place ID: {new_place.id}")

if __name__ == "__main__":
    main()