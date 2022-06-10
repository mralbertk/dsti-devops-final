from fastapi.testclient import TestClient
from pytest_redis import factories
from userapi.src.api import app, db

redis_external = factories.redisdb('redis_nooproc')

app.dependency_overrides[db] = redis_external
client = TestClient(app)

dummy_user_1 = "?fname=firstname_1&lname=lastname_1&email=email1@test.com"
dummy_user_2 = "?fname=firstname_2&lname=lastname_2&email=email2@test.com"
dummy_user_3 = "?fname=firstname_3&email=email3@test.com"
dummy_user_1_update = "?old_fname=firstname_1&old_lname=lastname_1&old_email=email1@test.com"
dummy_user_2_update = "&new_fname=firstname_2&new_lname=lastname_2&&new_email=email2@test.com"
dummy_user_update = f"{dummy_user_1_update}{dummy_user_2_update}"


def test_main_responds():
    """Default response by root should be 'Hello, World!'"""
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello, World!"}


def test_health_check():
    """Confirm health check is working"""
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"message": "OK"}


def test_user_create():
    """A correctly provided, not pre-existing user can be created"""
    client.delete(f"/user{dummy_user_1}")
    response = client.post(f"/user{dummy_user_1}")
    client.delete(f"/user{dummy_user_1}")
    assert response.status_code == 200


def test_user_create_fails():
    """An existing user cannot be created again"""
    client.delete(f"/user{dummy_user_1}")
    client.post(f"/user{dummy_user_1}")
    response = client.post(f"/user{dummy_user_1}")
    client.delete(f"/user{dummy_user_1}")
    assert response.status_code == 400


def test_user_read():
    """An existing user can be found in the database"""
    client.delete(f"/user{dummy_user_1}")
    client.post(f"/user{dummy_user_1}")
    response = client.get(f"/user{dummy_user_1}")
    client.delete(f"/user{dummy_user_1}")
    assert response.status_code == 200


def test_user_read_fails():
    """An attempt to find a non-existing user will fail"""
    client.delete(f"/user{dummy_user_1}")
    response = client.get(f"/user{dummy_user_1}")
    assert response.status_code == 404


def test_user_update():
    """An existing user can be updated"""
    client.delete(f"/user{dummy_user_1}")
    client.delete(f"/user{dummy_user_2}")
    client.post(f"/user{dummy_user_1}")
    response = client.put(f"/user{dummy_user_update}")
    response_2 = client.delete(f"/user{dummy_user_2}")
    assert response.status_code == 200
    assert response_2.status_code == 200


def test_user_update_fails():
    """A non-existing user cannot be updated"""
    client.delete(f"/user{dummy_user_1}")
    response = client.put(f"/user{dummy_user_1}")
    assert response.status_code == 400


def test_user_delete():
    """An existing user can be deleted"""
    client.delete(f"/user{dummy_user_1}")
    client.post(f"/user{dummy_user_1}")
    response = client.delete(f"/user{dummy_user_1}")
    assert response.status_code == 200


def test_user_delete_fails():
    """A non-existing user cannot be deleted"""
    client.delete(f"/user{dummy_user_1}")
    response = client.delete(f"/user{dummy_user_1}")
    assert response.status_code == 404


def test_user_function_validations():
    """Any user-function will fail if input is incomplete"""
    create_failure = client.post(f"/user{dummy_user_3}")
    read_failure = client.get(f"/user{dummy_user_3}")
    update_failure = client.put(f"/user{dummy_user_3}")
    delete_failure = client.delete(f"/user{dummy_user_3}")
    assert create_failure.status_code == 400
    assert read_failure.status_code == 400
    assert update_failure.status_code == 400
    assert delete_failure.status_code == 400
