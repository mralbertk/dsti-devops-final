from functools import wraps
from fastapi import HTTPException


def validate_inputs(func):
    @wraps(func)
    async def validate(**kwargs):
        if None in kwargs.values():
            raise HTTPException(status_code=400, detail="Bad Request: Missing parameter(s)")
        return await func(**kwargs)
    return validate
