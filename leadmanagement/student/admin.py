from django.contrib import admin
from . models import *
from app1.admin import MasterAdmin
from student.models import *

# Register your models here.

#class studentsAdmin(MasterAdmin) :
    
  #  list_display = ['Branch','Name','Qualification','Address','phone']
  #  exclude = ['created_user']

#admin.site.register(students,studentsAdmin)

class studentsAdmin(MasterAdmin) :
    fieldsets = (
        ("General", {
            "fields": (
                'EnquirySources',
            ),
        }),
        ("Phone Verification", {
            "fields": (
                'phone',
            ),
        }),
        ("Personal Info", {
            "fields": (
                'Student','gender','Email','AlternativeEmail','Address','Alternativeaddress','Dob','Street','City','state','District','pincode','whatsapp',
            ),
        }),
        ("Academic Info", {
            "fields": (
                'CollegeName','Yearofpass','Qualification','RollNo','RegistrationNo',
            ),
        }),
        ("Course Info", {
            "fields": (
                'course',
            ),
        }),
        ("Photo", {
            "fields": (
                'photo',
            ),
        }),
        ("Student Call Status", {
            "fields": (
                'StudentCallStatus','NextFollowupDate','Tostaff','Comments',
            ),
        }),
    )
    
    
    list_display = ['EnquirySources','phone','Student','Email','CollegeName','course','StudentCallStatus']
    exclude = ['created_user']

admin.site.register(students,studentsAdmin)
     
        