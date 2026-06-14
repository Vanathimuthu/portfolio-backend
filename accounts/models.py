from django.db import models


class Profile(models.Model):
    name = models.CharField(max_length=255)

    designation = models.CharField(max_length=255)

    email = models.EmailField()

    phone = models.CharField(max_length=20)

    location = models.CharField(max_length=255)

    linkedin = models.URLField()

    github = models.URLField(
        blank=True,
        null=True
    )

    summary = models.TextField()

    resume = models.FileField(
        upload_to="resume/",
        blank=True,
        null=True
    )

    profile_image = models.ImageField(
        upload_to="profile/",
        blank=True,
        null=True
    )

    def __str__(self):
        return self.name