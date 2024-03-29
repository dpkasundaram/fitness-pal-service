from typing import List, Union

from fastapi import FastAPI

from model.user import User

app = FastAPI()

database = {}

@app.get("/")
def root():
    return {"message": "Hello World"}


@app.get("/welcome/{name}")
def say_hello(name: str):
    return {"message": f"Welcome {name}"}

@app.get("/users/{user_id}")
def get_user_name(user_id: int) -> dict:
    """
    get user info from database using user_id
    Args:
        user_id: user's unique id

    Returns: user info dictionary

    """

    if user_id not in database:
        return {"message": "User id not in database"}

    return database[user_id].get_user_info()

@app.post("/users")
def add_user(user_id: int, name: str, age: int, height: float, weight: float) -> dict:
    """
    add new user to database
    Args:
        user_id:
        name:
        age:
        height:
        weight:

    Returns:

    """
    if user_id in database.keys():
        return {"message": "User already exists"}
    # insert into database
    new_user = User(
        user_id=user_id,
        name=name,
        age=age,
        height=height,
        weight=weight
    )
    database[user_id] = new_user
    return new_user.get_user_info()


@app.get("/users")
def get_all_users() -> List[dict]:
    """
    get all users
    Returns:

    """
    #base condition
    if not database:
        return [{"message": "No users found"}]

    return [user.get_user_info() for _, user in database.items()]


