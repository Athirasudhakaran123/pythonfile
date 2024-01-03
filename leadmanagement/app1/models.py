from django.db import models
from django.contrib.admin import AdminSite
from django.contrib.auth.models import User
from smart_selects.db_fields import ChainedForeignKey

# Create your models here.
class Master(models.Model):
  created_date=models.DateTimeField(auto_now_add=True)
  isactive=models.BooleanField(default=True,verbose_name="active")
  created_user=models.ForeignKey(User,null=True,blank=True,on_delete=models.CASCADE)
  class Meta:
    abstract=True
    ordering=['-isactive']


class State(Master):
  statename=models.CharField(max_length=100, unique=True)

  class Meta:
    verbose_name_plural="states"
    ordering=['-isactive']
  
  def __str__(self):
      return self.statename

class District(Master):
  state=models.ForeignKey(State,on_delete=models.CASCADE,limit_choices_to={"isactive":True})
  districtname=models.CharField(max_length=100,unique=True)
  # district = ChainedForeignKey(State, chained_field="state", chained_model_field="state_name",related_name="district_name", show_all=False, auto_choose=True, sort=True, limit_choices_to={"isactive":True})
  
  class Meta:
     verbose_name_plural="district"

  def __str__(self):
     return self.districtname


class Branch(Master):
  branch=models.CharField(max_length=200)
  Branch_code=models.CharField(max_length=50,unique=True,null=True)
  adress=models.CharField(max_length=500,blank=True)
  street=models.CharField(max_length=200,blank=True)
  state = models.ForeignKey(State, on_delete=models.CASCADE, limit_choices_to={"isactive": True})
  district = ChainedForeignKey(District, chained_field="state", chained_model_field="state", show_all=False, auto_choose=True, sort=True, limit_choices_to={"isactive":True})
  pincode=models.PositiveIntegerField(blank=True,null=True)
  mobile=models.CharField(max_length=12)
  email=models.EmailField(max_length=200,blank=True)


  class Meta:
   verbose_name_plural="Branches"
   ordering=("state","district")

  def __str__(self):
    return self.branch
   


class Enquirysources(Master):
    enquirysourcename=models.CharField(max_length=200,unique=True)

    class Meta:
      verbose_name_plural="Enquiry sources"


    def __str__(self):
      return self.enquirysourcename


class Followupstatus(Master):
    followupstatusname=models.CharField(max_length=200,unique=True)
    BOOL_CHOICES=((True,'Yes'),(False,'No'))
    followupstatus=models.BooleanField(choices=BOOL_CHOICES)





    class Meta:
      verbose_name_plural="followupstatuses"


    def __str__(self):
      return self.followupstatusname
      

class Qualification(Master):
  Qualificationname=models.CharField(max_length=200,unique=True)

  
  
  class Meta:
    verbose_name_plural="Qualifications"

  def __str__(self):
    return self.Qualificationname
    
class course(Master):
  course=models.CharField(max_length=200,unique=True)
  coursecode=models.CharField(max_length=200,unique=True,null=True)
  trainers=models.ManyToManyField(User,related_name="userTrainers",blank=True)

  
  class Meta:
    verbose_name_plural="course"
  def __str__(self):
    return self.course
    
class Batch(Master):
   Branch=models.ForeignKey(Branch,on_delete=models.CASCADE,verbose_name="Branch",
                            null=True,blank=False,limit_choices_to={"isactive":True})
   
   course=models.ForeignKey(course,on_delete=models.CASCADE,verbose_name="course",
                            null=True,blank=False,limit_choices_to={"isactive":True})
  #  course = ChainedForeignKey(course, chained_field="course", chained_model_field="course", show_all=False, auto_choose=True, sort=True, limit_choices_to={"isactive":True})

   Trainer=models.ForeignKey(User,on_delete=models.CASCADE,verbose_name="Trainer",null=True,related_name='trainer')


   start_date=models.DateField()
   start_time=models.TimeField(auto_now=False, auto_now_add=False,null=True)
   end_date=models.DateField()
   end_time=models.TimeField(auto_now=False, auto_now_add=False,null=True)
   isclosed=models.BooleanField(default=False,verbose_name="closed")
   batch=models.CharField(max_length=200,null=True)

   class Meta:
      verbose_name_plural="Batch"
   
   def save(self, *args,**kwargs):
        self.batch = f"{self.start_date.strftime('%Y')}_{self.course}_{self.start_date.strftime('%dth %B')}_{self.start_time.strftime('%I:%M %p')}_{self.end_time.strftime('%I:%M %p')}_{self.Branch}_{self.created_user}"
        super().save(*args,**kwargs)



   def __str__(self):
     return self.batch
