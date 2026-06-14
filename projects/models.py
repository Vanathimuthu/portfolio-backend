from django.db import models

# Create your models here.
from django.db import models


class Project(models.Model):
    title = models.CharField(max_length=255)

    description = models.TextField()

    github_url = models.URLField(
        blank=True,
        null=True
    )

    demo_url = models.URLField(
        blank=True,
        null=True
    )

    technologies = models.TextField()

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.title