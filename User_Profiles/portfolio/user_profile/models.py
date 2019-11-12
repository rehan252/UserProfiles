from django.db import models
from django.contrib.auth.models import User


class UserProfileInfo(models.Model):
    """
    This model class has one one to relation with Django Admin's
    Model User. This class is basically used extend User Model
    fields
    """
    # one to one relation with user
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # Extra fields
    portfolio_site = models.URLField(blank=True)
    profile_pic = models.ImageField(upload_to='profile_pics', blank=True)

    def __str__(self):
        return self.user.username
