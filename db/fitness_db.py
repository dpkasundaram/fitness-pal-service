"""
User table :
C: Insert into users (user_id, name, age, height, weight) values (1, 'Ram', 30, 140.2, 70.2)
R: Select * from users where user_id = 1
U: Update users set weight = 50, age = 33 where user_id = 1
D: Delete from users where user_id = 1
"""

import sqlite3

DB_FILE = "db/fitness.db"


def get_connection():
    return sqlite3.connect(DB_FILE)


def create_user(
    user_id: int, name: str, age: int, height: float, weight: float
) -> None:
    connection = get_connection()
    cursor = connection.cursor()
    insert_query = (
        "INSERT into users (user_id, name, age, height, weight) values (?, ?, ?, ?, ?)"
    )
    cursor.execute(insert_query, (user_id, name, age, height, weight))
    connection.commit()
    connection.close()


def read_user(user_id: int):
    connection = get_connection()
    cursor = connection.cursor()
    read_query = "SELECT * FROM users WHERE user_id = ?"
    cursor.execute(read_query, (user_id,))
    user = cursor.fetchone()
    connection.close()
    return user


def read_all_users():
    connection = get_connection()
    cursor = connection.cursor()
    read_query = "SELECT user_id, name, age, height, weight FROM users"
    cursor.execute(read_query)
    users = cursor.fetchall()
    connection.close()
    return users


def update_user(
    user_id: int, name: str, age: int, height: float, weight: float
) -> None:
    connection = get_connection()
    cursor = connection.cursor()
    update_query = (
        "UPDATE users SET name = ?, age = ?, height = ?, weight = ? WHERE user_id = ?"
    )
    cursor.execute(update_query, (name, age, height, weight, user_id))
    connection.commit()
    connection.close()


def delete_user(user_id: int) -> None:
    connection = get_connection()
    cursor = connection.cursor()
    delete_query = "DELETE FROM users WHERE user_id = ?"
    cursor.execute(delete_query, (user_id,))
    connection.commit()
    connection.close()
