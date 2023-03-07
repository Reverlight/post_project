import random
from datetime import datetime
from config import (
    SENTENCES_PER_POST,
    PASSWORD_LENGTH,
    PASSWORD_CHARACTERS,
    EMAIL_DOMAINS,
    RANDOM_NAMES_PATH,
    RANDOM_SENTENCES_PATH,
    MAX_LIKES_PER_USER,
    MAX_POSTS_PER_USER,
    NUMBER_OF_USERS
)

TYPE_PATH_MAPPING = {
    'names': RANDOM_NAMES_PATH,
    'sentences': RANDOM_SENTENCES_PATH,
}


def get_data(type):
    return _read_lines_from_file(TYPE_PATH_MAPPING[type])


def _read_lines_from_file(file_path):
    result = []
    with open(file_path, 'r', encoding='UTF-8') as file:
        for line in file:
            result.append(line.replace('\n', ''))
    return result


def _generate_username(users):
    return f'bot-user-{random.choice(users)}-{datetime.utcnow().second}'


def _generate_password():
    password = ''
    for _ in range(PASSWORD_LENGTH):
        password += random.choice(PASSWORD_CHARACTERS)
    return password


def _generate_email(username):
    return username + random.choice(EMAIL_DOMAINS)


def generate_user(users):
    username = _generate_username(users)
    email = _generate_email(username)
    password = _generate_password()
    return {
        'username': username,
        'email': email,
        'password': password,
    }


def generate_post(sentences):
    random_post = random.choices(sentences, k=SENTENCES_PER_POST)
    return ''.join(random_post)


def generate_number_of_posts_for_user():
    return random.randint(1, MAX_POSTS_PER_USER)


def generate_number_of_likes_for_user():
    return random.randint(1, MAX_LIKES_PER_USER)


def get_number_of_users():
    return NUMBER_OF_USERS
