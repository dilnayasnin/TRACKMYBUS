from django.db import models

# Create your models here.
class login_model(models.Model):
    username = models.CharField(max_length=100, null=True, blank=True)
    password = models.CharField(max_length=100, null=True, blank=True)
    user_type = models.CharField(max_length=100, null=True, blank=True)
    status = models.CharField(max_length=100, null=True, blank=True)

class ownerRE_model(models.Model):
    owner_id = models.ForeignKey(login_model, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=100, null=True, blank=True)
    age = models.CharField(max_length=100, null=True, blank=True)
    email = models.CharField(max_length=100, null=True, blank=True)
    contact = models.CharField(max_length=100, null=True, blank=True)
    address = models.CharField(max_length=100, null=True, blank=True)
    gender = models.CharField(max_length=100, null=True, blank=True)

class Driver_model(models.Model):
    bus_id = models.ForeignKey(login_model, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=100, null=True, blank=True)
    age = models.CharField(max_length=100, null=True, blank=True)
    email = models.CharField(max_length=100, null=True, blank=True)
    address = models.CharField(max_length=100, null=True, blank=True)
    license = models.CharField(max_length=100, null=True, blank=True)
    experience = models.CharField(max_length=100, null=True, blank=True)
    contact = models.CharField(max_length=100, null=True, blank=True)
    gender = models.CharField(max_length=100, null=True, blank=True)

class busroute_model(models.Model):
    source = models.CharField(max_length=100, null=True, blank=True)
    destination = models.CharField(max_length=100, null=True, blank=True)

class stop_model(models.Model):
    route_id = models.ForeignKey(busroute_model, on_delete=models.CASCADE, null=True, blank=True)
    stop_name = models.CharField(max_length=100, null=True, blank=True)

class bus_model(models.Model):
    OWNERID = models.ForeignKey(login_model, on_delete=models.CASCADE, null=True, blank=True)
    route_id = models.ForeignKey(busroute_model, on_delete=models.CASCADE, null=True, blank=True)
    bus_name = models.CharField(max_length=100, null=True, blank=True)
    bus_number = models.CharField(max_length=100, null=True, blank=True)
    status = models.CharField(max_length=100, null=True, blank=True)

class feedback_model(models.Model):
    LoginID = models.ForeignKey(login_model, on_delete=models.CASCADE, null=True, blank=True)
    feedback = models.CharField(max_length=100, null=True, blank=True)
    rating = models.CharField(max_length=100, null=True, blank=True)
    date_created = models.DateField(auto_now_add=True)
