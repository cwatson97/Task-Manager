from django.db import models

# Create your models here.
class Task(models.Model):   # Create a database model named Task  |  Every model must inhert from models.Model
                            # In django, each model equals one table in the database
                            
    title = models.CharField(max_length = 200)  # This defined a column named title in the table
    completed = models.BooleanField(default = False)  # This defined another column named completed in the table | Marked as true for compeleted, false for not

    # When you print a Task object, it will show something human-readable
    def __str__(self):
        return self.title   # Returning self.title means the task will appear by its title (like 'Buy Groceries')