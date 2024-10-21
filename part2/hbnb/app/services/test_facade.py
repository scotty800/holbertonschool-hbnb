from app.persistence.repository import InMemoryRepository
from app.models.user import User
from app.models.place import Place
user_repo = InMemoryRepository()
from ..models.base_models import BaseModel

def test_create_place_for_user():
    repo = InMemoryRepository()
    
    # Création de l'utilisateur
    user = User(first_name="John", last_name="Doe", email="john.doe@example.com")
    repo.add(user)

    # Récupération de l'utilisateur ajouté
    retrieved_user = repo.get(user.id)
    
    # Vérification que l'utilisateur existe
    if not retrieved_user:
        print("Erreur : Utilisateur non trouvé")
        return

    # Création de la place associée à l'utilisateur
    try:
        place = Place(
            title="Beautiful Place",
            description="A lovely place to stay.",
            price=150,
            latitude=40.7128,
            longitude=-74.0060,
            owner_id=retrieved_user.id  # Utilisation de l'ID utilisateur récupéré
        )
        print(f"Place créée avec succès : {place}")
    except ValueError as e:
        print(f"Erreur lors de la création de la place : {e}")

# Appel du test
test_create_place_for_user()