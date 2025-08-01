# heart_disease/models.py
from django.db import models
from django.contrib.auth.models import User

class UserPrediction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    input_data = models.JSONField()  # Store input data as a JSON object
    prediction = models.CharField(max_length=50)  # Prediction result
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp for prediction

    def __str__(self):
        return f'{self.user.username} - {self.prediction} at {self.created_at}'
