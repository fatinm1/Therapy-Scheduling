import pytest
from settings import load_settings

def test_production_rejects_missing_secrets():
    with pytest.raises(RuntimeError):
        load_settings({"FLASK_ENV": "production"})

def test_configuration_uses_environment():
    value = load_settings({"FLASK_ENV": "production", "JWT_SECRET_KEY": "x" * 32, "DB_PASSWORD": "test-only", "DB_USER": "app"})
    assert value["database"]["password"] == "test-only"
    assert value["database"]["user"] == "app"
    assert value["jwt_secret"] == "x" * 32

def test_development_has_no_shared_signing_secret():
    assert load_settings({})["jwt_secret"] != load_settings({})["jwt_secret"]
