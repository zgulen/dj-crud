from django.db import models

class Student(models.Model):
    first_name = models.CharField('Full Name', max_length=50)
    phone = models.CharField(max_length=50, unique=True, blank=True, null=True)
    email = models.EmailField(max_length=154, unique=True, blank=True, null=True)
    GENDER =(
        ("1", "Female"),
        ("2", "Male"),
        ("3", "Other"),
        ("4", "Prefer Not Say"),
    )
    PATH =(
        ("1", "Front-end"),
        ("2", "Back-end"),
        ("3", "AWS-DevOps"),
        ("4", "Data-Science"),
    )

    gender = models.CharField(max_length=50, choices=GENDER)
    number = models.IntegerField(unique=True, blank=True, null=True)
    path = models.CharField(max_length=20, choices=PATH)
    
    def __str__(self):
        return f"{self.number} {self.first_name} {self.last_name}"