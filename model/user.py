class User:
    def __init__(self, user_id: int, name: str, age: int, height: float, weight: float):
        self.user_id = user_id
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight

    def get_user_info(self) -> dict:
        return {
            'user_id': self.user_id,
            'name': self.name,
            'age': self.age,
            'height': self.height,
            'weight': self.weight
        }
