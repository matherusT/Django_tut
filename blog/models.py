from django.db import models
from django.utils import timezone

class Post(models.Model):
    autor = models.ForeignKey('auth.User', on_delete = models.CASCADE)
    tytul = models.CharField(max_length = 200)
    tekst = models.TextField()
    czas_utworzenia = models.DateTimeField(default = timezone.now)
    data_publikacji = models.DateTimeField(blank = True, null = True)

    def publikuj(self):
        self.data_publikacji = timezone.now()
        self.save()

    def __str__(self):
        return self.tytul