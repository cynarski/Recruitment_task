from django.db import models
from django.contrib.auth.models import User
from rest_api.common.managers import ActiveObjects
from django.contrib.auth import get_user_model

User = get_user_model()

class System(models.Model):
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=255, blank=True, null=True)
    status = models.CharField(max_length=100, default='active')
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    is_deleted = models.BooleanField(default=False)
    created_time = models.DateTimeField(auto_now_add=True)

    objects = ActiveObjects()
    all_objects = models.Manager()


    def __str__(self):
        return self.name