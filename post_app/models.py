from datetime import datetime, timedelta

from django.conf import settings
from django.contrib.auth.models import (
    BaseUserManager,
    AbstractBaseUser,
    PermissionsMixin
)
from django.db import models
import jwt


class Post(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    created_by = models.ForeignKey('User', on_delete=models.CASCADE, db_index=True)


class Like(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE, db_index=True)
    post = models.ForeignKey('Post', on_delete=models.CASCADE, db_index=True)


class UserManager(BaseUserManager):
    def create_user(self, username, email, password=None):
        if username is None:
            raise TypeError('Users must have a username')

        if email is None:
            raise TypeError('Users must have an email')

        user = self.model(username=username, email=self.normalize_email(email))
        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, username, email, password):
        if password is None:
            raise TypeError('Superusers must have a password')

        user = self.create_user(username, email, password)
        user.is_superuser = True
        user.is_staff = True
        user.save()

        return user


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(db_index=True, max_length=255, unique=True)
    email = models.EmailField(db_index=True, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    last_request = models.DateTimeField(auto_now_add=True)

    # USERNAME_FIELD determines what field is used for login. We use email.
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    # UserManager controls the object of this type (User)
    objects = UserManager()

    def __str__(self):
        return self.email

    @property
    def token(self):
        return self._generate_jwt_token()

    def update_last_request(self):
        dt = datetime.now()
        self.last_request = dt
        self.save()

    def get_full_name(self):
        return self.username

    def _generate_jwt_token(self):
        dt = datetime.now() + timedelta(days=1)

        token = jwt.encode({
            'id': self.pk,
            'exp': int(dt.strftime('%m%d%Y%H%M%S'))
        }, settings.SECRET_KEY, algorithm='HS256')

        return token
