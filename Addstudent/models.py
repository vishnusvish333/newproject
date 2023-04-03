from django.db import models

# Create your models here.


class AddStudent(models.Model):
    Enquiry_Source = models.CharField(max_length=10)
    Date_of_Birth = models.DateField()
    Student = models.CharField(max_length=20)
    Gender = models.CharField(max_length=10)
    Phone = models.BigIntegerField()
    Email = models.EmailField(max_length=20)
    Address = models.TextField(max_length=50)
    Alternative_Email = models.CharField(max_length=20)
    Alternative_Address = models.TextField(max_length=50)
    Mobile = models.BigIntegerField()
    Street = models.CharField(max_length=20)
    City = models.CharField(max_length=20, null=True, blank=True)
    State = models.CharField(max_length=20, null=True, blank=True)
    District = models.CharField(max_length=20, null=True, blank=True)
    Qualification = models.CharField(max_length=20, null=True, blank=True)
    Course = models.CharField(max_length=20, null=True, blank=True)
    Pincode = models.CharField(max_length=20)
    Whatsapp = models.CharField(max_length=20)
    RollNo = models.CharField(max_length=20)
    Registration_No = models.CharField(max_length=20)
    College_Name = models.CharField(max_length=20)
    Year_of_Pass = models.IntegerField()
    Photo = models.ImageField(upload_to="images/")
    Active = models.BooleanField()

    def __str__(self):
        return self.Student
    
class staff(models.Model):
    staff = models.CharField(max_length=20)
    def __str__(self):
        return self.staff



class student_call_status(models.Model):
    student_call_status=models.ForeignKey(AddStudent,on_delete=models.CASCADE)
    Next_FollowUp_Date=models.DateTimeField()
    To_staff=models.ForeignKey(staff,on_delete=models.CASCADE)
    Comment=models.CharField(max_length=200)
    

class Employee(models.Model):
    Company=models.CharField(max_length=20)
    address=models.CharField(max_length=20)
    Contact_Person=models.CharField(max_length=50)
    Contact=models.IntegerField(max_length=50)
    E_mail=models.EmailField(max_length=50)
    Website=models.CharField(max_length=50)
    Activate = models.BooleanField()

class State(models.Model):
    State_Name = models.CharField(max_length=20)
    Active = models.BooleanField()

    def _str_(self):
        return self.State_Name
    
class District(models.Model):
    State_Name = models.ForeignKey(State, on_delete=models.CASCADE)
    District_Name = models.CharField(max_length=20)
    Active = models.BooleanField()

    def _str_(self):
        return self.District_Name
    
class Batch(models.Model):
    Batch_Name = models.CharField(max_length=20)
    Start_Date=models.DateTimeField()
    End_Date=models.DateTimeField()
    def __str__(self):
        return self.Batch_Name


    
class Branch(models.Model):
    Branch_name = models.CharField(max_length=20,verbose_name="Branch")
    Address = models.CharField(max_length=50, null=True, blank=True)
    Street = models.CharField(max_length=50, null=True, blank=True)
    State = models.ForeignKey(State, on_delete=models.CASCADE)
    District = models.ForeignKey(District, on_delete=models.CASCADE)
    Pincode = models.IntegerField(max_length=10, null=True, blank=True)
    Mobile = models.IntegerField(max_length=13)
    E_mail = models.EmailField(max_length=20, null=True, blank=True) 
    def _str_(self):
        return f"{self.Branch_name} ({self.District}, {self.State})"

    def get_districts(self):
        return District.objects.filter(state=self.State)
    
class Company(models.Model):
    Company = models.CharField(max_length=20)
    Address1 =models.CharField(max_length=20, null=True, blank=True)
    Address2 =models.CharField(max_length=20, null=True, blank=True)
    Address3 =models.CharField(max_length=20, null=True, blank=True)
    Phone = models.IntegerField(max_length=15)
    E_mail = models.EmailField(max_length=20, null=True, blank=True)
    Website = models.CharField(max_length=30)
    Logo =models.ImageField(upload_to="images/")
    Active = models.BooleanField()
    def _str_(self):
        return self.Company
    
class MapStudent(models.Model):
    Student = models.ForeignKey(AddStudent,on_delete=models.CASCADE)
    Batch = models.ForeignKey(Batch,on_delete=models.CASCADE)
    






