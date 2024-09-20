from django.db import models

# Create your models here.


class MessageModel(models.Model):
    topic = models.ForeignKey('topic.TopicModel', on_delete=models.CASCADE)
    content = models.TextField()
    create_at = models.DateField(auto_now_add=True)
