from django.db import models

class Details(models.Model):
    address = models.CharField(max_length=512, null=True, blank=True)
    permanent_address = models.CharField(max_length=512, null=True, blank=True)
    office_address = models.CharField(max_length=512, null=True, blank=True)
    contact_number = models.CharField(max_length=512, null=True, blank=True)
    pan = models.CharField(max_length=512, null=True, blank=True)
    passport = models.CharField(max_length=512, null=True, blank=True) 
