from fastapi_users.authentication import CookieTransport, JWTStrategy, AuthenticationBackend
from todo.config import settings

cookie_transport = CookieTransport(cookie_name='ToDo', cookie_max_age=3600)

SECRET_KEY = settings.secret_key


def get_jwt_strategy() -> JWTStrategy:
    return JWTStrategy(secret=SECRET_KEY, lifetime_seconds=3600)


auth_backend = AuthenticationBackend(name="jwt",
                                     transport=cookie_transport,
                                     get_strategy=get_jwt_strategy)
