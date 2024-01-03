from django.db import models
from app1.models import *
from django.core.validators import RegexValidator

# Create your models here.
#class students(Master):
   # Branch=models.ForeignKey(Branch,on_delete=models.CASCADE,)

   #name=models.charfield(max_length=50)
   #dob=models.datefield()
   #qualification=models.charfield(max_length=50)
   #address=models.textfield(max_lenth=100)
   #phone=models.charfield(
   #   max_length=15,null=true,
       # validators=[
           # RegexValidator(
              #  regex=r'^\+?1?\d{9,15}$',
               # message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed."
           # )
        #]
   # )
   # email=models.EmailField()


    ##class Meta:
      # verbose_name_plural="student"
       #ordering=['-isactive']
  
    #def __str__(self):
      #return self.Name
    

 

GENDER_CHOICES = [
        ('MALE', 'Male'),
        ('FEMALE', 'Female'),
        ('OTHER', 'Other'),
    ]
CALL_CHOICES = [
        ('YES', 'Yes'),
        ('NO', 'No'),
    ]
# Create your models here.
class students(Master):
    EnquirySources = models.ForeignKey(Enquirysources,null=True,blank=True,on_delete=models.CASCADE)
    phone = models.CharField(
        max_length=15,null=True,
        validators=[
            RegexValidator(
                regex=r'^\+?1?\d{9,15}$',
                message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed."
            )
        ]
    )
    Student = models.CharField(max_length=100,unique=True,null=True)
    

    gender = models.CharField(max_length=100, choices=GENDER_CHOICES,null=True)
    Email = models.EmailField(max_length=100,unique=True,null=True)
    AlternativeEmail = models.EmailField(max_length=100,unique=True,blank=True,null=True)
    Address=models.TextField(max_length=500,blank=True,null=True)
    Alternativeaddress= models.TextField(max_length=500,blank=True,null=True)
    Dob=models.DateField(null=True)
    Street=models.CharField(max_length=100,blank=True,null=True)
    City = models.CharField(max_length=100,blank=True,null=True)
    state= models.ForeignKey(State,null=True,on_delete=models.CASCADE)
    District=models.ForeignKey(District,null=True,on_delete=models.CASCADE)
    pincode=models.IntegerField(null=True)
    whatsapp=models.CharField(
        max_length=15,null=True,
        validators=[
            RegexValidator(
                regex=r'^\+?1?\d{9,15}$',
                message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed."
            )
 ]
    )


    CollegeName=models.CharField(max_length=100,null=True)
    Yearofpass=models.DateField(null=True )
    Qualification=models.ForeignKey(Qualification,null=True,on_delete=models.CASCADE)
    RollNo=models.IntegerField(null=True)
    RegistrationNo=models.IntegerField(null=True)
    course=models.ForeignKey(course,null=True,on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='user_photos/', null=True)
    StudentCallStatus=models.CharField(max_length=100, choices=CALL_CHOICES,null=True)
    NextFollowupDate=models.DateField(null=True)
    Tostaff=models.ForeignKey(User,related_name='to_staff',on_delete=models.CASCADE,null=True)
    Comments=models.TextField(max_length=500,null=True)

    class Meta:
       verbose_name_plural="students"
       ordering=['-isactive']
  
    def _str_(self):
     return self.Student
