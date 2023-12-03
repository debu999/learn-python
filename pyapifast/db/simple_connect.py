from pathlib import Path
import certifi
from pydantic import Field
from mongoengine import connect  # type: ignore

from pydantic_settings import BaseSettings, SettingsConfigDict

env_path = Path(Path(__file__).parent.parent.parent, "env", ".env.local").as_posix()


class Settings(BaseSettings):
    mongodb_uri: str = Field(alias="MONGODB_URI")
    mongodb_credential: str = Field(alias="MONGODB_CREDENTIAL")
    mongodb_user: str = Field(alias="MONGODB_USERNAME")
    model_config = SettingsConfigDict(env_file=env_path, extra="ignore")


settings = Settings().model_dump()  # type: ignore


def connect_mongodb():
    return connect(
        db="mongodb",
        host=settings.get("mongodb_uri"),
        username=settings.get("mongodb_user"),
        password=settings.get("mongodb_credential"),
        authentication_source="admin",
        alias="mongodb",
        tls=True,
        tlsCAFile=certifi.where(),
    )
