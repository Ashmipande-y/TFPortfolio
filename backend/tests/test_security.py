from app.core.security import (
    create_access_token,
    hash_password,
    verify_password,
)


def test_password_hashing():
    password = "TestPassword123!"

    hashed = hash_password(password)

    assert hashed != password
    assert verify_password(password, hashed)
    assert not verify_password("WrongPassword", hashed)


def test_create_access_token():
    token = create_access_token("test-user-id")

    assert isinstance(token, str)
    assert len(token) > 0