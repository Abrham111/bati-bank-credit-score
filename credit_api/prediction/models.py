from django.db import models

# Create your models here.
class Prediction(models.Model):
  input_data = models.JSONField()
  prediction = models.IntegerField()
  timestamp = models.DateTimeField(auto_now_add=True)
