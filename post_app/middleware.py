from post_app.models import User
from post_app.services import decode_token


class UpdateUserMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        token = request.COOKIES.get('token')
        if token:
            payload = decode_token(token)
            user = User.objects.filter(id=payload['id']).first()
            user.update_last_request()
            request.user = user
        response = self.get_response(request)
        return response