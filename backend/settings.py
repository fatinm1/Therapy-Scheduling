"""Environment configuration with no committed database or signing credentials."""
import os
import secrets


def load_settings(environ=None):
    env = os.environ if environ is None else environ
    production = env.get("FLASK_ENV") == "production"
    secret = env.get("JWT_SECRET_KEY", "")
    if production and len(secret) < 32:
        raise RuntimeError("Production requires JWT_SECRET_KEY of at least 32 characters")
    if production and not env.get("DB_PASSWORD"):
        raise RuntimeError("Production requires DB_PASSWORD")
    return {
        "database": {
            "host": env.get("DB_HOST", "localhost"),
            "user": env.get("DB_USER", "root"),
            "password": env.get("DB_PASSWORD", ""),
            "database": env.get("DB_NAME", "therapy_clinic"),
            "port": int(env.get("DB_PORT", "3306")),
        },
        "jwt_secret": secret or secrets.token_urlsafe(32),
    }
