from abc import ABC, abstractmethod

class Repository(ABC):
    @abstractmethod
    def add(self, obj):
        pass

    @abstractmethod
    def get(self, obj_id):
        pass

    @abstractmethod
    def get_all(self):
        pass

    @abstractmethod
    def update(self, obj_id, data):
        pass

    @abstractmethod
    def delete(self, obj_id):
        pass

    @abstractmethod
    def get_by_attribute(self, attr_name, attr_value):
        pass


class InMemoryRepository(Repository):
    def __init__(self):
        self._storage = {}
        self._user_storage = {}  # Dictionnaire pour stocker les objets par ID utilisateur
        print("Repository initialisé.")

    def add(self, obj, user_id=None):
        """Ajoute un objet dans le stockage, avec un ID d'utilisateur optionnel."""
        if obj.id in self._storage:
            print(f"Erreur : L'objet avec l'ID {obj.id} existe déjà.")
            raise ValueError(f"Object with ID {obj.id} already exists.")
        
        # Stocker l'objet dans le stockage principal
        self._storage[obj.id] = obj
        
        # Stocker l'objet par ID d'utilisateur, s'il est fourni
        if user_id:
            if user_id not in self._user_storage:
                self._user_storage[user_id] = []
            self._user_storage[user_id].append(obj.id)  # Ajouter l'ID de l'objet à la liste de l'utilisateur
            print(f"Objet {obj.id} ajouté à l'utilisateur {user_id}")

        print(f"Objet ajouté : {obj}")

    def get(self, obj_id):
        """Récupère un objet par son ID."""
        result = self._storage.get(obj_id)
        if result is None:
            print(f"L'objet avec l'ID {obj_id} n'existe pas dans le dépôt.")
        else:
            print(f"Objet récupéré : {result}")
        return result

    def get_all(self):
        """Retourne tous les objets stockés."""
        all_objects = list(self._storage.values())
        print(f"Tous les objets dans le dépôt : {all_objects}")
        return all_objects

    def update(self, obj_id, data):
        """Met à jour les informations d'un objet existant."""
        obj = self.get(obj_id)
        if obj:
            print(f"Objet avant mise à jour : {obj}")
            if hasattr(obj, 'update') and callable(getattr(obj, 'update')):
                obj.update(data)  # Mettez à jour les attributs de l'objet existant
                print(f"Objet après mise à jour : {obj}")
            else:
                print(f"L'objet avec ID {obj_id} ne peut pas être mis à jour car il ne possède pas de méthode 'update'.")
                raise ValueError(f"L'objet avec l'ID {obj_id} ne peut pas être mis à jour.")
        else:
            print(f"L'objet avec l'ID {obj_id} n'existe pas dans le dépôt.")
            raise ValueError(f"L'objet avec l'ID {obj_id} n'existe pas dans le dépôt.")

    def delete(self, obj_id):
        """Supprime un objet du dépôt par son ID."""
        if obj_id in self._storage:
            # Supprime l'objet de _user_storage pour chaque utilisateur
            for user_id, obj_ids in self._user_storage.items():
                if obj_id in obj_ids:
                    obj_ids.remove(obj_id)
                    if not obj_ids:  # Si l'utilisateur n'a plus d'objets, on peut supprimer la clé
                        del self._user_storage[user_id]
            del self._storage[obj_id]
            print(f"L'objet avec l'ID {obj_id} a été supprimé.")
        else:
            print(f"Erreur : L'objet avec l'ID {obj_id} n'existe pas dans le dépôt.")
            raise ValueError(f"L'objet avec l'ID {obj_id} n'existe pas dans le dépôt.")

    def get_by_attribute(self, attr_name, attr_value):
        """Récupère un objet en fonction d'un attribut spécifique."""
        result = next((obj for obj in self._storage.values() if hasattr(obj, attr_name) and getattr(obj, attr_name) == attr_value), None)
        if result:
            print(f"Objet trouvé par l'attribut {attr_name}={attr_value} : {result}")
        else:
            print(f"Aucun objet trouvé avec l'attribut {attr_name}={attr_value}.")
        return result

    def get_by_user_id(self, user_id):
        """Récupère tous les objets associés à un ID utilisateur."""
        if user_id in self._user_storage:
            user_objects = [self._storage[obj_id] for obj_id in self._user_storage[user_id]]
            print(f"Objets trouvés pour l'utilisateur {user_id} : {user_objects}")
            return user_objects
        else:
            print(f"Aucun objet trouvé pour l'utilisateur {user_id}.")
            return []