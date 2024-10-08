"""Cats app models."""

from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Achievement(models.Model):
    """Describes cat achievement."""

    name = models.CharField(max_length=64)

    def __str__(self):
        """Name of model object in admin panel."""
        return self.name


class Cat(models.Model):
    """Represents a cat objects."""

    name = models.CharField(max_length=16)
    color = models.CharField(max_length=16)
    birth_year = models.IntegerField()
    owner = models.ForeignKey(
        User, related_name='cats',
        on_delete=models.CASCADE
    )
    achievements = models.ManyToManyField(
        Achievement,
        through='AchievementCat'
    )
    image = models.ImageField(
        upload_to='cats/images/',
        null=True,
        default=None
    )

    def __str__(self):
        """Name of model object in admin panel."""
        return self.name


class AchievementCat(models.Model):
    """Model to connect Cat and Achievement models."""

    achievement = models.ForeignKey(Achievement, on_delete=models.CASCADE)
    cat = models.ForeignKey(Cat, on_delete=models.CASCADE)

    def __str__(self):
        """Name of model object in admin panel."""
        return f'{self.achievement} {self.cat}'
