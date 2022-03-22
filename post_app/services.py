from datetime import datetime, timedelta

import jwt
from django.conf import settings
from rest_framework.exceptions import AuthenticationFailed

from post_app.models import User, Like


def encode_token(pk):
    dt = datetime.now() + timedelta(days=1)

    return jwt.encode(
        {
            'id': pk,
            'exp': int(dt.strftime('%m%d%Y%H%M%S'))
        },
        settings.SECRET_KEY,
        algorithm='HS256'
    )


def decode_token(token):
    if not token:
        raise AuthenticationFailed('Unauthenticated!')
    try:
        return jwt.decode(
            token,
            settings.SECRET_KEY,
            algorithms='HS256'
        )
    except jwt.ExpiredSignatureError:
        raise AuthenticationFailed('Token is expired')
    except jwt.exceptions.DecodeError:
        raise AuthenticationFailed('Token is incorrect')


def get_user(user_token):
    payload = decode_token(user_token)
    user = User.objects.filter(id=payload['id']).first()
    return user


def set_like(user, post):
    Like.objects.create(user=user, post=post).save()


def set_dislike(user, post):
    like = get_or_none(Like, user=user, post=post)
    like.delete()


def get_or_none(model, **kwargs):
    try:
        return model.objects.get(**kwargs)
    except model.DoesNotExist:
        return None


def has_user_liked(user, post):
    result = get_or_none(Like, user=user, post=post)
    return result is not None