from django.db import models

class Ticket(models.Model):
    PRIORITY_CHOICES = [
        ('low','Low'),
        ('medium','Medium'),
        ('high','High'),
        ('critical','Critical'),
    ]
    STATUS_CHOICES = [
        ('open','Open'),
        ('in_progress','In Progress'),
        ('resolved','Resolved'),
        ('closed','Closed'),
    ]
    
    title = models.CharField(max_length=200)
    description = models.TextField()
    category = models.CharField(max_length=200)
    priority = models.CharField(
        max_length=20,
        choices=PRIORITY_CHOICES,
        default='Medium'
    )
    status = models.CharField(
        max_length=20,
        choices = STATUS_CHOICES,
        default="Open"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title