from django.db import models

class Person(models.Model):
	surname = models.CharField(max_length=200)
	firstname = models.CharField(max_length=200)