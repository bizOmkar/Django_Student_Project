from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=20)
    standerd = models.IntegerField()
    email = models.EmailField(null=True, blank=True)
    
    def __str__(self):
        return str(self.id)+' '+self.name
    
class Mark(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    maths = models.IntegerField(null=True, blank=True)
    science = models.IntegerField(null=True, blank=True)
    history = models.IntegerField(null=True, blank=True)
    pt =  models.IntegerField(null=True, blank=True)
    
    def __str__(self):
        return str(self.student)
    


