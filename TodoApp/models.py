from django.db import models

# Create your models here.
class Todo(models.Model): # migrate 완료
    title = models.CharField(max_length=100)
    description = models.TextField()
    important = models.BooleanField(default=False)
    complete = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title