from django.db import models

class Comment(models.Model):
    CHARACTER_CHOICES = [
        ('denji', 'Denji'),
        ('power', 'Power'),
        ('akita', 'Aki'),
        ('himeno', 'Himeno'),
        # add other characters as needed
    ]

    character = models.CharField(max_length=50, choices=CHARACTER_CHOICES)
    comment_text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.get_character_display()} - {self.created_at.strftime('%Y-%m-%d %H:%M')}"
