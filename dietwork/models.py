#models.py/dietwork

from django.db import models
from accounts.models import Account  # Import your custom user model

class DietPlan(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='diet_plans')
    date = models.DateField()
    meal_details = models.TextField()  # You can also use JSONField for structured data
    excel_link = models.URLField(blank=True, null=True)

    def __str__(self):
        return f'Diet Plan for {self.user.full_name()} on {self.date}'

class WorkoutPlan(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='workout_plans')
    date = models.DateField()
    workout_details = models.TextField()  # You can also use JSONField for structured data
    excel_link = models.URLField(blank=True, null=True)

    def __str__(self):
        return f'Workout Plan for {self.user.full_name()} on {self.date}'
