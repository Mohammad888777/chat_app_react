from django.db import models
from django.contrib.auth.models import User

class Message(models.Model):
    author=models.ForeignKey(User,related_name="author_messages",on_delete=models.CASCADE)
    content=models.TextField()
    timestamp=models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.author.username
    
    def lsat_10_messages(self):
        return Message.objects.all().order_by("-timestamp")[:10]
