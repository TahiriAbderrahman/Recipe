from django.db import models

class Recette(models.Model):
    categorie= models.CharField(max_length=50)

    def __str__(self):
        return self.categorie