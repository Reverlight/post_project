from django.http import HttpResponse
from django.shortcuts import render

from ..forms import UserForm, UserLoginForm
from ..models import Like
from ..services import parse_date


def analytics(request):
    _from = request.GET.get('date_from')
    _to = request.GET.get('date_to')

    if not _from or not _to:
        return HttpResponse(f'<h1>Please specify params date_from, date_to</h1>')

    date_from = parse_date(request.GET.get('date_from'))
    date_to = parse_date(request.GET.get('date_to'))

    r = Like.objects.filter(made_at_time__range=(date_from, date_to)).count()
    return HttpResponse(f'<h1>Future Analytics</h1> {r}')


def main(request):
    return HttpResponse('<h1>Future Main</h1>')


def signup(request):
    form = UserForm()
    context = {'form': form}
    return render(request, 'post_app/user_signup.html', context)


def login(request):
    form = UserLoginForm()
    context = {'form': form}
    return render(request, 'post_app/user_login.html', context)
