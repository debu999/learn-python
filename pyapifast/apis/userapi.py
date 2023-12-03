from typing import List
import traceback
from ..schema.user import User
from pyapifast.db.dbservice import get_users, create_user
from fastapi import APIRouter, HTTPException
from pyapifast import db

router = APIRouter(
    prefix="/items",
    tags=["items"],
    responses={404: {"description": "Not found"}},
)
"""
Summary:
Returns a JSON response with the message "Hello World".

Explanation:
This function is an HTTP GET endpoint that returns a JSON response with the message "Hello World". It is used as the root endpoint ("/") of the API.

Args:
None

Returns:
dict: A dictionary containing the message "Hello World".

Examples:
```python
>>> read_root()
{"Hello": "World"}
"""


@router.get("/", response_model=List[User])
async def get_all_users():
    return get_users()


@router.post("/", response_model=User)
async def add_user(user: User):
    u = user.model_dump()
    try:
        usr = create_user(db.user.User(**u))
    except Exception as e:
        raise HTTPException(
            status_code=500, detail="".join(traceback.format_exception(e))
        ) from e
    return usr
