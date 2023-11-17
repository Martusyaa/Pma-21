from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField(blank=True, null= True)
    is_completed = models.BooleanField(default=False)
    edited = models.BooleanField(default=False)
    time_edited = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "task"
        verbose_name_plural = "tasks"
        ordering = ('is_completed', 'title')