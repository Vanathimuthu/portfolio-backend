from django.db import models

# Create your models here.
from django.db import models


class Visitor(models.Model):

    ip_address = models.CharField(
        max_length=255
    )

    visited_at = models.DateTimeField(
        auto_now_add=True
    )

    page = models.CharField(
        max_length=255
    )

    def __str__(self):
        return self.ip_address