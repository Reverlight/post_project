from requests_html import HTMLSession

from config import (
    USER_SIGNUP,
    USER_LOGIN_API,
    USER_SIGNUP_API,
    POSTS_CREATION,
    POST_LIST_API,
    LIKE_API
)


def get_session():
    return HTMLSession()


def _get_csrf_token(session):
    return session.get(USER_SIGNUP).html.find('input[name="csrfmiddlewaretoken"]')[0].attrs['value']


def signup_user(username, email, password, session):
    csrf_token = _get_csrf_token(session)
    session.headers = {
        'X-CSRFToken': csrf_token,
        'Content-Type': 'application/json',
    }
    user = {
        'username': username,
        'email': email,
        'password': password,
    }
    session.post(USER_SIGNUP_API, json={'user': user})


def login_user(email, password, session):
    user = {
        'email': email,
        'password': password,
    }
    csrf_token = _get_csrf_token(session)
    session.headers = {
        'X-CSRFToken': csrf_token,
        'Content-Type': 'application/json',
    }
    response = session.post(USER_LOGIN_API, json={'user': user})
    session.headers = {
        **session.headers,
        'token': response.cookies['token'],
    }


def get_posts(session):
    response = session.get(POST_LIST_API)
    return response.json()


def create_post(session, post, username):
    csrf_token = _get_csrf_token(session)
    session.headers = {
        **session.headers,
        'X-CSRFToken': csrf_token,
        'Content-Type': 'application/x-www-form-urlencoded',
    }
    data = {
        'title': username,
        'text': post,
    }
    session.post(POSTS_CREATION, data=data)


def like_post(session, post_id):
    csrf_token = _get_csrf_token(session)
    session.headers = {
        **session.headers,
        'X-CSRFToken': csrf_token,
        'Content-Type': 'application/json',
    }
    session.post(LIKE_API.format(id=post_id))
