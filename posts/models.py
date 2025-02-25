from django.db import models
from django.conf import settings

class Post(models.Model):
    titre = models.CharField(max_length=255)
    contenu = models.TextField()
    date_publication = models.DateTimeField(auto_now_add=True)
    auteur = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.titre