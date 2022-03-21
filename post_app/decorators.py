from .models import User
from .services import decode_token


def update_last_request(func):
    def wrapper(obj, request):
        user = request.data.get('user', {})
        username = user['username']

        user = User.objects.filter(username=username).first()
        user.update_last_request()
        return func(obj, request)

    return wrapper


def login_required(func):
    def wrapper(obj, request, *args, **kwargs):
        token = request.COOKIES.get('token')
        # Will raise an error if token is not valid
        decode_token(token)
        return func(obj, request, *args, **kwargs)

    return wrapper
