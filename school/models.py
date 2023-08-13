from django.db import models


class Student(models.Model):
    objects = models.Manager()
    name = models.CharField(max_length=50)
    rg = models.CharField(max_length=9)
    cpf = models.CharField(max_length=11)
    birth_date = models.DateField()

    def __str__(self):
        return self.name


class Course(models.Model):
    objects = models.Manager()
    LEVEL = {
        ('B', 'Basic'),
        ('I', 'Intermediate'),
        ('A', 'Advanced'),
    }
    course_code = models.CharField(max_length=10)
    description = models.CharField(max_length=100)
    level = models.CharField(max_length=1, choices=LEVEL, blank=False, null=False, default='B')

    def __str__(self):
        return self.description


class Enrollment(models.Model):
    objects = models.Manager()
    PERIOD = {
        ('M', 'Matutinal'),
        ('V', 'Vespertine'),
        ('N', 'Nocturnal'),
    }
    student = models.ForeignKey(to=Student, on_delete=models.CASCADE)
    course = models.ForeignKey(to=Course, on_delete=models.CASCADE)
    period = models.CharField(max_length=1, choices=PERIOD, blank=False, null=False, default='M')


# python manage.py makemigrations
# python manage.py migrate
