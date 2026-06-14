from django.db import models


class Experience(models.Model):

    company = models.CharField(
        max_length=255
    )

    role = models.CharField(
        max_length=255
    )

    duration = models.CharField(
        max_length=255
    )

    description = models.TextField()

    def __str__(self):
        return self.company