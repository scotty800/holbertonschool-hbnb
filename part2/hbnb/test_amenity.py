from app.models.amenity import Amenity

def test_amenity_creation():
    """
    Test the creation of an Amenity instance and check that the name is set correctly.
    """
    # Create the Amenity object
    amenity = Amenity(name="Wi-Fi")

    # Check that the amenity name is as expected
    assert amenity.name == "Wi-Fi", "Amenity name did not match"

    # Confirm the test passed
    print("Amenity creation test passed!")


def test_amenity_name_too_long():
    """
    Test that creating an Amenity with a name longer than 50 characters raises an error.
    """
    try:
        # This should raise a ValueError due to the name being too long
        Amenity(name="A" * 51)
    except ValueError as e:
        assert str(e) == "The equipment name cannot exceed 50 characters."
        print("Long name validation test passed!")
    else:
        raise AssertionError("Expected a ValueError for name length exceeding 50 characters.")

# Run both tests
test_amenity_creation()
test_amenity_name_too_long()
