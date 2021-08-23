from django.conf import settings
from django.db import models


class Baby(models.Model):
    "Generated Model"
    babyname = models.BigIntegerField()
