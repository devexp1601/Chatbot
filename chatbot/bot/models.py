from django.db import models

# Create your models here.
class Message(models.Model):
    text = models.TextField()
    is_user = models.BooleanField(default=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{'User' if self.is_user else 'Bot'}: {self.text[:50]}"
    
class Conversation(models.Model):
    messages = models.ManyToManyField(Message, related_name='conversations')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Conversation {self.id} - {self.created_at.strftime('%Y-%m-%d %H:%M:%S')}"
    

