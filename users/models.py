from django.db import models
import jwt
from datetime import datetime, timedelta
from django.conf import settings

from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager, PermissionsMixin
)
# Create your models here.
class UserManager(BaseUserManager):
    use_in_migrations = True

    def create_user(self, username, name, surname, email, phone, role_id, password=None):
     
        if username is None:
            raise TypeError('Users must have a username.')

        if name is None or surname is None:
        	raise TypeError('Users must have a name')

        if email is None:
            raise TypeError('Users must have an email address.')

        if phone is None:
        	raise TypeError('Users must have a phone number')

        user = self.model(
        	username=username, 
        	name = name,
        	surname = surname,
        	email=self.normalize_email(email),
            phone = phone,
            role_id = role_id
            )
        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, username, name, surname, email, phone, password, role_id):
        admin_role = Role.objects.get(pk=role_id)

        if username is None:
        	raise TypeError('Superusers must have a username.')
        if password is None:
            raise TypeError('Superusers must have a password.')

        user = self.create_user(
        	username = username, 
        	name = name,
        	surname = surname,
        	email = email, 
        	phone = phone,
        	role_id = admin_role,
        	password = password)

        user.is_superuser = True
        user.is_staff = True
        user.set_password(password)
        user.save()

        return user	


class Role(models.Model):
	name =  models.CharField( max_length = 255)
	def __str__(self):
		return self.name

class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField('Username', db_index=True, max_length=255, unique=True)
    name = models.CharField('Name', max_length = 255)
    surname = models.CharField('Surname',max_length = 255)
    role_id = models.ForeignKey(Role, on_delete = models.CASCADE)
    phone = models.CharField('Phone number', max_length = 255)
    email = models.EmailField('Email', db_index=True, unique=True)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_of_add = models.DateTimeField(auto_now_add=True)
    
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['name', 'surname', 'email','phone', 'role_id']

    
    objects = UserManager()

    def __str__(self):
        return self.username

    @property
    def token(self):
        return self._generate_jwt_token()

    def _generate_jwt_token(self):
        dt = datetime.now() + timedelta(days=60)

        token = jwt.encode({
            'id': self.pk,
            'exp': dt.utcfromtimestamp(dt.timestamp())
        }, settings.SECRET_KEY, algorithm='HS256')

        return token.decode('utf-8')