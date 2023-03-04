from datetime import datetime, timedelta

import jwt
from django.conf import settings
from rest_framework.exceptions import AuthenticationFailed


def encode_token(pk):
    token_expire_date = datetime.now() + timedelta(days=1)

    return jwt.encode(
        {
            'id': pk,
            'exp': int(token_expire_date.strftime('%m%d%Y%H%M%S'))
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


def parse_date(date_str):
    return datetime.strptime(date_str, '%Y-%m-%d')


def get_or_none(model, **kwargs):
    try:
        return model.objects.get(**kwargs)
    except model.DoesNotExist:
        return None
