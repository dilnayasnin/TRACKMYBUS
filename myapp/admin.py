from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(login_model)
admin.site.register(ownerRE_model)
admin.site.register(Driver_model)
admin.site.register(busroute_model)
admin.site.register(stop_model)
admin.site.register(bus_model)
admin.site.register(feedback_model)
