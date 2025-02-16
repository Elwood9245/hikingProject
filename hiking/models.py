from django.db import models
from django.contrib.auth.models import User


class Route(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    location = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Event(models.Model):
    route = models.ForeignKey(Route, on_delete=models.CASCADE)
    organizer = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    details = models.TextField()

    def __str__(self):
        return f"{self.route.name} - {self.date}"


class Comment(models.Model):
    route = models.ForeignKey(Route, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username}: {self.content[:20]}"