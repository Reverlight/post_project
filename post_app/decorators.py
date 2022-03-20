from .models import User


def update_last_request(func):
    def wrapper(obj, request):
        user = request.data.get('user', {})
        username = user['username']

        user = User.objects.filter(username=username).first()
        user.update_last_request()
        return func(obj, request)

    return wrapper
