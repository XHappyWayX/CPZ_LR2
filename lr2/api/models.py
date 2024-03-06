from django.db import models


class SavedRequests(models.Model):
    request_url = models.CharField(default=None, null=True)
    request_data = models.CharField(default=None, null=True)
