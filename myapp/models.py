# myapp/models.py

from django.db import models

class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    rating = models.FloatField()

    class Meta:
        db_table = 'students'  # Set the table name
        verbose_name_plural = 'students'  # Set the plural name
        ordering = ['last_name', 'first_name']  # Default sorting

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Rating(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='ratings')
    value = models.FloatField()

    class Meta:
        db_table = 'ratings'  # Set the table name
        verbose_name_plural = 'ratings'  # Set the plural name
        ordering = ['-value']  # Default sorting in descending order of value

    def __str__(self):
        return f"Rating {self.value} for {self.student}"



