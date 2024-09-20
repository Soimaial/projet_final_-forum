from django.db import models

# Create your models here.


class ForumModel(models.Model):
   
    title = models.CharField(max_length=150)
    categorie = models.CharField(max_length=150)
    create_at = models.DateField(auto_now_add=True)