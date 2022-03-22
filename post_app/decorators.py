from .services import decode_token


def login_required(func):
    def wrapper(obj, request, *args, **kwargs):
        token = request.COOKIES.get('token')
        # Will raise an error if token is not valid
        decode_token(token)
        return func(obj, request, *args, **kwargs)

    return wrapper
