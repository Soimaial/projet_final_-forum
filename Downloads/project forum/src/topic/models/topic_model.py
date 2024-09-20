from django.db import models

# Create your models here.

class TopicModel(models.Model):
    forum = models.ForeignKey('forum.ForumModel', on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    create_at = models.DateField(auto_now_add=True)