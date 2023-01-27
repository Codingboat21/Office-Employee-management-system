from django.db import models

class Department(models.Model):
    name=models.CharField(max_length=100,null=False)
    location=models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Role(models.Model):
    name=models.CharField(max_length=70,null=False)

    def __str__(self):
        return self.name

class Employee(models.Model):
    first_name=models.CharField(max_length=30 , null=False,blank=False)
    last_name=models.CharField(max_length=20,null=True,blank=True)
    dept=models.ForeignKey(Department,on_delete=models.CASCADE)
    role=models.ForeignKey(Role,on_delete=models.CASCADE)
    salary=models.IntegerField(default=0)
    bonus=models.IntegerField(default=0)
    phone=models.IntegerField(max_length=15)
    hire_date=models.DateField()

    def __str__(self):
        return '%s %s %s' %(self.first_name,self.last_name,self.phone)
# Create your models here.
