from django.db import models


class CustomUser(models.Model):
	username=models.CharField(max_length=250)
	password=models.CharField(max_length=250)
	email=models.EmailField()
	age=models.IntegerField()

	def __str__(self):
		return self.username


