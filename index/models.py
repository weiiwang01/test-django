from django.db import models


class Visitor(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    user_agent = models.CharField(max_length=255)
