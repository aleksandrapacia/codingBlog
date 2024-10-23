from django.db import models

# Place for my models
class Topic(models.Model):
    """A topic about coding that user gets to learn about."""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Return a string representation of the model."""
        return self.text
    
class Entry(models.Model):
    """Info about topic"""
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE) #if delete, delete all 
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entires'
    
    def __str__(self):
        """Returns a string representation of a model as a string"""
        return f"{self.text[:50]}..."
        