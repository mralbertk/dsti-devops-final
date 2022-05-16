import os
import sys

# Weird import 'hack' to enable sibling import
sys.path.append(os.path.join(os.path.dirname(__file__), '..\\\\..'))

from fastapi import FastAPI, HTTPException
import src.api.db_redis as db_redis
import src.models.user as user
from src.api.decorators import validate_inputs

description = """
userapi, created for the 'DevOps with Adaltas' class at DSTI in Spring 2022. 🖳

## Users 

You can do all these things with users:

- Create users 
- Read users
- Update users
- Delete users
"""

app = FastAPI(title="FastUserApi",
              description=description,
              version="0.0.1",
              contact={
                  "name": "Albert KONRAD",
                  "email": "albert.konrad@edu.dsti.institute"
              })
db = db_redis.r


@app.get("/")
async def read_main() -> dict:
    """Root"""
    return {"msg": "Hello, World!"}


@app.get("/health")
async def health_check() -> dict:
    """API health check"""
    return {"msg": "OK"}


@app.post("/user")
@validate_inputs
async def add_user(fname: str = None,
                   lname: str = None,
                   email: str = None) -> dict:
    """Creates a new user entry in the database.

    Tests if the user already exists in the DB before creating a new one.

    :returns:
    status.code 200 if new user is successfully created
    status.code 400 if new user creation failed
    """

    # Create user object
    new_user = user.User(first_name=fname,
                         last_name=lname,
                         email=email)

    # Validate user does not exist
    user_check = db.hgetall(new_user.hash_id)
    if user_check:
        raise HTTPException(status_code=400, detail="User already exists")

    # Write new user to DB
    db_redis.r.hmset(new_user.hash_id, new_user.details)
    return {'msg': 'User created', 'values': new_user.details}


@app.get("/user")
@validate_inputs
async def get_user(fname: str = None,
                   lname: str = None,
                   email: str = None) -> dict:

    lookup_user = user.User(first_name=fname,
                            last_name=lname,
                            email=email)
    db_entry = db.hgetall(lookup_user.hash_id)
    if not db_entry:
        raise HTTPException(status_code=404, detail="User does not exist")
    return db_entry


@app.put("/user")
@validate_inputs
async def update_user(old_fname: str = None,
                      old_lname: str = None,
                      old_email: str = None,
                      new_fname: str = None,
                      new_lname: str = None,
                      new_email: str = None) -> dict:

    old_user = user.User(first_name=old_fname,
                         last_name=old_lname,
                         email=old_email)

    old_db_entry = db.hgetall(old_user.hash_id)
    if not old_db_entry:
        raise HTTPException(status_code=404, detail="User does not exist")

    new_user = user.User(first_name=new_fname,
                         last_name=new_lname,
                         email=new_email)

    new_db_entry = db.hgetall(new_user.hash_id)
    if new_db_entry:
        raise HTTPException(status_code=404, detail="Update failed. A user with these details already exists")

    db.delete(old_user.hash_id)
    db.hmset(new_user.hash_id, new_user.details)
    return {'msg': 'User updated',
            'old': old_user.details,
            'new': new_user.details}


@app.delete("/user")
@validate_inputs
async def delete_user(fname: str = None,
                      lname: str = None,
                      email: str = None) -> dict:

    del_user = user.User(first_name=fname,
                         last_name=lname,
                         email=email)

    # Validate user exists
    db_entry = db.hgetall(del_user.hash_id)
    if not db_entry:
        raise HTTPException(status_code=404, detail="User not found")

    # Delete user
    db.delete(del_user.hash_id)
    return {'msg': 'User deleted'}
