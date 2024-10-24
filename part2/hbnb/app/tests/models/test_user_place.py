def test_create_user():
    user = User(first_name="John", last_name="Doe", email="john.doe@example.com")
    assert user.first_name == "John"
    assert user.last_name == "Doe"
    assert user.email == "john.doe@example.com"


def test_create_place():
    user = User(first_name="John", last_name="Doe", email="john.doe@example.com")
    place = Place(
        title="Cozy Cabin",
        description="A nice place to relax",
        price=120.0,
        latitude=45.0,
        longitude=-93.0,
        owner=user,
    )
    assert place.title == "Cozy Cabin"
    assert place.price == 120.0
    assert place.owner == user
