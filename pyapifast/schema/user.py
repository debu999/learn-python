from typing import Optional
from pydantic import BaseModel, ConfigDict, EmailStr, Field
from pydantic.functional_validators import AfterValidator
from bson.objectid import ObjectId
from typing_extensions import Annotated


def object_id_validate(v: ObjectId | str) -> ObjectId | str:
    assert ObjectId.is_valid(v), f"{v} is not a valid ObjectId"
    return ObjectId(v) if isinstance(v, str) else str(v)


PyObjectId = Annotated[ObjectId | str, AfterValidator(object_id_validate)]


class User(BaseModel):
    email: EmailStr
    first_name: str
    last_name: str
    id: Optional[PyObjectId] = None
    model_config = ConfigDict(arbitrary_types_allowed=True)
