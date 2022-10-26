from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


# Create your models here.
class Profile(models.Model):
    AGE_MIN_VALUE = 12

    MAX_LENGTH_PASS = 30
    MAX_LENGTH_FIRST_NAME = 30
    MAX_LENGTH_LAST_NAME = 30

    email = models.EmailField(
        null=False,
        blank=False,
    )

    age = models.IntegerField(
        validators=(MinValueValidator(AGE_MIN_VALUE),),
    )

    password = models.CharField(
        max_length=MAX_LENGTH_PASS,
    )

    first_name = models.CharField(
        max_length=MAX_LENGTH_FIRST_NAME,
        null=True,
        blank=True,
    )

    last_name = models.CharField(
        max_length=MAX_LENGTH_LAST_NAME,
        null=True,
        blank=True,
    )

    profile_picture = models.URLField(
        null=True,
        blank=True,
    )
    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

class Game(models.Model):
    ACTION = 'Action'
    ADVENTURE = 'Adventure'
    PUZZLE = 'Puzzle'
    STRATEGY = 'Strategy'
    SPORTS = 'Sports'
    BOARD_CARD_GAME = 'Board/Card Game'
    OTHER = 'Other'

    CATEGORIES = [(x, x) for x in (ACTION, ADVENTURE, PUZZLE, STRATEGY, SPORTS, BOARD_CARD_GAME, OTHER)]

    MAX_LENGTH_TITLE = 30
    MAX_LENGTH_CATEGORY = 15
    title = models.CharField(
        max_length=MAX_LENGTH_TITLE,
        unique=True,
    )

    category = models.CharField(
        max_length=15,
        choices=CATEGORIES
    )

    rating = models.FloatField(
        validators=(
            MinValueValidator(0.1),
            MaxValueValidator(5.0),
        )
    )

    max_level = models.IntegerField(
        validators=(
            MinValueValidator(1),
        )
    )

    image_url = models.URLField()

    summary = models.TextField(
        null=True,
        blank=True,
    )
