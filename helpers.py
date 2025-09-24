import string
import random

from faker import Faker


def generate_user_data():
    faker=Faker()
    user_data = {
        "firstname": faker.first_name(),
        "lastname": faker.last_name(),
        "username": faker.user_name(),
        "email": generate_random_string(10)+"@yandex.ru",
        "password": faker.password(length=10, special_chars=True)
    }
    return user_data


def generate_random_string(length):
    letters = string.ascii_lowercase
    random_string = ''.join(random.choice(letters) for _ in range(length))
    return random_string
