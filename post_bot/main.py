import random

from post_bot.generator import get_data, generate_user, generate_post, generate_number_of_posts_for_user, \
    generate_number_of_likes_for_user, get_number_of_users
from post_bot.requester import get_session, signup_user, login_user, create_post, get_posts, like_post


def run_one_bot_user():
    sentences = get_data('sentences')
    user_names = get_data('names')
    user = generate_user(user_names)
    username = user['username']
    email = user['email']
    password = user['password']

    session = get_session()
    signup_user(
        username,
        email,
        password,
        session,
    )

    login_user(
        email,
        password,
        session,
    )
    number_posts_to_create = generate_number_of_posts_for_user()

    for _ in range(number_posts_to_create):
        post = generate_post(sentences)
        create_post(session, post, username)
    number_of_likes_for_user = generate_number_of_likes_for_user()
    posts_on_server = get_posts(session)

    if len(posts_on_server) < number_of_likes_for_user:
        number_of_likes_for_user = len(posts_on_server)

    posts_liked = []

    for _ in range(number_of_likes_for_user):
        duplicates_checked = False
        while not duplicates_checked:
            post = random.choice(posts_on_server)
            if post['id'] not in posts_liked:
                duplicates_checked = True
        like_post(session, post['id'])
        posts_liked.append(post['id'])


def run_bot_users():
    number_of_users = get_number_of_users()
    for _ in range(number_of_users):
        run_one_bot_user()


def main():
    run_bot_users()


if __name__ == '__main__':
    main()
