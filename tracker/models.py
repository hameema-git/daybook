from django.db import models
from datetime import date
class Entry(models.Model):
    TYPE_CHOICES = [('income', 'Income'), ('expense', 'Expense')]
    # date = models.DateField(auto_now_add=True)
    date = models.DateField(default=date.today)  # Use today's date as default if not provided
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=100)
    type = models.CharField(max_length=10, choices=TYPE_CHOICES)
    note = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.date} - {self.type} - ₹{self.amount}"
