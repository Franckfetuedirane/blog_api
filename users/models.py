from django.db import models

class User(models.Model):
    nom = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    date_inscription = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email