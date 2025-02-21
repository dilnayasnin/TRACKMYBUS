from django.forms import ModelForm

from .models import ownerRE_model
from .models import  *
 
class  ownerRE_form(ModelForm):
    class Meta:
        model = ownerRE_model
        fields = ['name', 'age', 'email', 'contact', 'address','gender']

class  driver_form(ModelForm):
    class Meta:
        model = Driver_model
        fields = ['name', 'age','gender', 'email', 'contact','address','license','experience']

class  busroute_form(ModelForm):
    class Meta:
        model = busroute_model
        fields = ['source', 'destination']

class  stop_form(ModelForm):
    class Meta:
        model = stop_model
        fields = ['stop_name', 'route_id']

class  bus_form(ModelForm):
    class Meta:
        model = bus_model
        fields = ['bus_name', 'bus_number']

class  feedback_form(ModelForm):
    class Meta:
        model = feedback_model
        fields = ['feedback', 'rating']