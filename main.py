from fastapi import FastAPI

from db.fitness_db import create_user, delete_user, read_user, read_all_users, update_user
from model.user import User

app = FastAPI()


@app.get("/")
def root():
    return {"message": "Hello World"}


@app.get("/welcome/{name}")
def say_hello(name: str):
    return {"message": f"Welcome {name}"}


@app.get("/users/{user_id}")
def get_user_name(user_id: int) -> dict:

    user_info = read_user(user_id)

    if user_info:
        return user_cursor_to_user_info(user_info)

    return {"message": "User not found"}


@app.get("/users/")
def get_all_user() -> list[dict]:

    user_info_list = read_all_users()
    if user_info_list:
        return [user_cursor_to_user_info(user_info) for user_info in user_info_list]
    else:
        return []


def user_cursor_to_user_info(user_cursor):

    return {
        "user_id": user_cursor[0],
        "name": user_cursor[1],
        "age": user_cursor[2],
        "height": user_cursor[3],
        "weight": user_cursor[4],
    }



@app.post("/users")
def add_user(user: User) -> dict:
    create_user(
        user_id=user.user_id,
        name=user.name,
        age=user.age,
        height=user.height,
        weight=user.weight,
    )

    return {"message": "New User Created"}


@app.delete("/users/{user_id}")
def delete_user_api(user_id: int) -> dict:
    try:
        delete_user(user_id)
        return {"message": "User deleted successfully"}
    except Exception as e:
        print(f"Error occur: {e}")
        return {"message": "Unable to Delete User"}


@app.put("/users")
def update_user_api(user: User) -> dict:
    update_user(
        user_id=user.user_id,
        name=user.name,
        age=user.age,
        height=user.height,
        weight=user.weight,
    )

    return {"message": "User updated successfully"}

