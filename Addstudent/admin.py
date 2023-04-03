from django.contrib import admin
from .models import Employee,student_call_status,AddStudent,State,District,Batch,Branch,Company,MapStudent,staff


# Register your models here.


class AddStudent_Admin(admin.ModelAdmin):
    list_display = ('Enquiry_Source','Student' ,'Gender', 'State', 'District', 'Qualification', 'Course',)
admin.site.register(AddStudent, AddStudent_Admin)


class EmployeeAdmin(admin.ModelAdmin):
    list_display=('Company','address','Contact_Person','Contact','E_mail','Website')
    ordering = ('Company',)
    search_fields = ('company','address','person','contact','email','website')
admin.site.register(Employee,EmployeeAdmin)

class Student_Call_Status_Admin(admin.ModelAdmin):
    list_display = ('student_call_status','Next_FollowUp_Date','To_staff','Comment')
    search_fields = ('student_call_status','To_staff','Next_FollowUp_Date')
admin.site.register(student_call_status,Student_Call_Status_Admin)

class State_Admin(admin.ModelAdmin):
    list_display = ('State_Name', 'Active',)
admin.site.register(State, State_Admin)

class District_Admin(admin.ModelAdmin):
    list_display = ('District_Name', 'Active',)
admin.site.register(District, District_Admin)

class Batch_admin(admin.ModelAdmin):
    list_display=('Batch_Name','Start_Date','End_Date')
admin.site.register(Batch,Batch_admin)

class Branch_admin(admin.ModelAdmin):
    list_display=('Branch_name','State','District','Mobile')
admin.site.register(Branch,Branch_admin)

class Company_admin(admin.ModelAdmin):
    list_display=('Company','Website','Phone')
admin.site.register(Company,Company_admin)

class MapStudent_admin(admin.ModelAdmin):
    list_display=('Student','Batch')
admin.site.register(MapStudent,MapStudent_admin)

class staff_admin(admin.ModelAdmin):
    list_display=('staff',)
admin.site.register(staff,staff_admin)