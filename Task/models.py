from django.db import models

# Create your models here.

class Task(models.Model):
    priority_type = {
    ("low","low"),
    ("medium","medium"),
    ("high","high"),
    }
    status_type = {
    ("not started","not started"),
    ("in progress","in progress"),
    ("completed","completed"),
    }
    title = models.CharField(("Title"),max_length=20)
    description = models.CharField(("Description"),max_length=200)
    status = models.CharField(("Status"), max_length=50,choices=status_type)
    priority = models.CharField(("Priority"),max_length=20,choices=priority_type)
    def __str__(self) :
        return self.title

