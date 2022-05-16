from userapi.src.controllers.user import User


def test_user_class():
    """User class must function as expected"""
    test_user = User("Albert", "Konrad", "test@email.com")
    assert test_user.first_name == "Albert"
    assert test_user.last_name == "Konrad"
    assert test_user.email == "test@email.com"
    assert isinstance(test_user.details, dict) is True
    assert isinstance(test_user.hash_id, bytes) is True


def test_user_hash_equality():
    """Two identical users must have the same hash_id"""
    test_user_a = User("Albert", "Konrad", "test@email.com")
    test_user_b = User("Albert", "Konrad", "test@email.com")
    assert test_user_a.hash_id == test_user_b.hash_id


def test_user_hash_inequality():
    """Two different users must have different hash_ids"""
    test_user_a = User("Albert", "Konrad", "test@email.com")
    test_user_b = User("Konrad", "Albert", "test@email.com")
    assert test_user_a.hash_id != test_user_b.hash_id
