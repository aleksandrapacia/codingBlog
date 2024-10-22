from django.db import models

# Place for my models
class Topic(models.Model):
    """A topic about coding that user gets to learn about."""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Return a string representation of the model."""
        return self.text