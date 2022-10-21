from django.db import models
from django.contrib.auth.models import AbstractUser


# Custom User Model
class User(AbstractUser):
    name = models.CharField(max_length=100, null=True)
    email = models.EmailField(unique=True, null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']


class MultipleChoice(models.Model):

    CORRECT_ANSWER = (
        ("1", "1. answer"),
        ("2", "2. answer"),
        ("3", "3. answer"),
        ("4", "4. answer"),
    )

    question = models.CharField(max_length=50)
    answer_1 = models.CharField(max_length=50, null=True)
    answer_2 = models.CharField(max_length=50, null=True)
    answer_3 = models.CharField(max_length=50, null=True)
    answer_4 = models.CharField(max_length=50, null=True)

    correct_answer = models.CharField(max_length=10, choices=CORRECT_ANSWER, null=True)

class Level(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Chapter(models.Model):
    headline = models.CharField(max_length=150)
    body = models.TextField(null=True, blank=True)
    next = models.ForeignKey('self', related_name="next_chapter", on_delete=models.CASCADE, blank=True, null=True)
    prev = models.ForeignKey('self', related_name="prev_chapter", on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.headline


class Topic(models.Model):
    headline = models.CharField(max_length=150)
    description = models.TextField(null=True, blank=True)
    start_chapter = models.ForeignKey(Chapter, on_delete=models.CASCADE)
    categories = models.ForeignKey(Category, on_delete=models.CASCADE)
    level = models.ForeignKey(Level, on_delete=models.CASCADE, null=True, blank=True)

    creator = models.ManyToManyField(User)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.headline

    def short_description(self):
        return self.description[:150]