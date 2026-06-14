from django.db import models


class Skill(models.Model):
    name = models.CharField(max_length=100)

    percentage = models.PositiveIntegerField(
        default=80
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.name