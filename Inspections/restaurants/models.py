from django.db import models

# Create your models here.
# class Restaurant(models.Model):
#     inspection_id = models.IntegerField()
#     dba_name = models.TextField()
#     aka_name = models.TextField()
#     license = models.IntegerField()
#     facility_type = models.TextField()
#     risk = models.TextField()
#     address = models.TextField()
#     city = models.TextField()
#     state = models.TextField()
#     zip = models.CharField(max_length=255)
#     inspection_date = models.TextField()
#     inspection_type = models.TextField()
#     results = models.TextField()
#     violations = models.TextField()
#     lattitude = models.FloatField(null=True, blank=True)
#     longitude = models.FloatField(null=True, blank=True)
#     location = models.TextField()    

#     class Meta:
#         indexes = [
#             models.Index(fields=['aka_name'], name='aka_name_idx'),
#             models.Index(fields=['address'], name='address_idx'),
#         ]


# Create your models here.
class Restaurant(models.Model):
    inspection_id = models.IntegerField()
    dba_name = models.TextField()
    aka_name = models.TextField()
    license = models.IntegerField()
    facility_type = models.TextField()
    risk = models.TextField()
    address = models.TextField()
    city = models.TextField()
    state = models.TextField()
    zip = models.CharField(max_length=255)
    inspection_date = models.DateField(null=True, blank=True)
    inspection_type = models.TextField()
    results = models.TextField()
    violations = models.TextField()
    lattitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)
    location = models.TextField()  
