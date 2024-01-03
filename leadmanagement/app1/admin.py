# from django.contrib import admin

# # Register your models here.
# from app1.models import State,District,Branch,Enquirysources,Followupstatus,Qualification,course,Batch


# admin.site.register(State)
# admin.site.register(District)
# admin.site.register(Branch)
# admin.site.register(Enquirysources)
# admin.site.register(Followupstatus)
# admin.site.register(Qualification)
# admin.site.register(course)
# admin.site.register(Batch)

from django.contrib import admin

from.models import *

# Register your models here.

class MasterAdmin(admin.ModelAdmin) :

    list_display = ['created_user','created_date','isactive']
    def save_model(self, request, obj, form, change):
        # Set the created_user field to the currently logged-in user
        obj.created_user = request.user
        super().save_model(request, obj, form, change)

class StateAdmin(MasterAdmin) :

    list_display = ['statename']
    exclude = ['created_user']

admin.site.register(State,StateAdmin)


class DistrictAdmin(MasterAdmin) :
    
    list_display = ['districtname','state']
    exclude = ['created_user']

admin.site.register(District,DistrictAdmin)


class BranchAdmin(MasterAdmin) :
    
    list_display = ['branch','Branch_code','adress','street','state','district','pincode','mobile','email']
    exclude = ['created_user']

admin.site.register(Branch,BranchAdmin)


class EnquirysourcesAdmin(MasterAdmin) :
    
    list_display = ['enquirysourcename']
    exclude = ['created_user']

admin.site.register(Enquirysources,EnquirysourcesAdmin)


class FollowupstatusAdmin(MasterAdmin) :
    
    list_display = ['followupstatusname','BOOL_CHOICES','followupstatus']
    exclude = ['created_user']

admin.site.register(Followupstatus,FollowupstatusAdmin)


class QualificationAdmin(MasterAdmin) :
    
    list_display = ['Qualificationname']
    exclude = ['created_user']

admin.site.register(Qualification,QualificationAdmin)


class courseAdmin(MasterAdmin) :
    
    exclude = ['created_user']

admin.site.register(course,courseAdmin)


class BatchAdmin(MasterAdmin) :
    
    list_display = ['Branch','course','Trainer','start_date','start_time','end_date','end_time','batch','isclosed']
    exclude = ['created_user']

admin.site.register(Batch,BatchAdmin)



