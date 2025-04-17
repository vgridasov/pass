from django.db import models

class Employee(models.Model):
    # Подразделение
    department = models.CharField(max_length=100)    
    # Табельный номер
    employee_number = models.CharField(max_length=10)    
    # ФИО
    last_name = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100)
    # Должность
    employee_position = models.CharField(max_length=100)

    
    def __str__(self):
        name = " ".join(
            self.last_name,
            self.first_name,
            self.middle_name,
            self.employee_number
            )
        
        return name    