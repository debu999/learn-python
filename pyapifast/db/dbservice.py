from typing import Any
from pyapifast.db.user import User

from pyapifast.db.simple_connect import connect_mongodb

database_client: Any = None


def check_connection():
    global database_client
    if not database_client:
        database_client = connect_mongodb()


def get_users():
    check_connection()

    return list(User.objects)


def create_user(user: User) -> User:
    check_connection()
    user.save()
    return user


if __name__ == "__main__":
    user = User(
        email="debabrata_patnaik@live.com", first_name="Debabrata", last_name="Patnaik"
    )

    u: User = create_user(user)
    print(u)
