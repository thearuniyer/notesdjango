'''
Here we specify what we want our database tables and its collumns to look like.
For simplicity:
    Every class represents a TABLE
    Every attribute represents a COLUMN
    Every instance of the class will represent a ROW in the table
'''
from django.db import models

# Create your models here.

class Note(models.Model):
    body    = models.TextField(null=True, blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.body[:50]