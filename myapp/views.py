from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from .models import *
from .forms import *
from .views import *
from .forms import busroute_form


# Create your views here.
class Login(View):
    def get(self, request):
        return render(request, 'administrator/login.html')
    def post(self, request):
         username = request.POST['username']
         password = request.POST['password']
         login_obj=login_model.objects.get(username=username,password=password)
         request.session['loginid']=login_obj.id

         if login_obj.user_type=="admin":
            return HttpResponse('''<script>alert("login successfully");window.location.href="/dash"</script>''')
         elif login_obj.user_type=="owner":
            if login_obj.status=="approved":
                return HttpResponse('''<script>alert("login successfully");window.location.href="/ownerph"</script>''')
            else:
                return HttpResponse('''<script>alert("verification underprocess");window.location.href="/"</script>''')

class addBS(View):
    def get(self, request):
        return render(request, 'administrator/addBS.html')

class busroute(View):
    def get(self, request):
        return render(request, 'administrator/busroute.html')
    def post(self,request):
        c=busroute_form(request.POST)
        if c.is_valid():
            c.save()
            return HttpResponse('''<script>alert("Bus route added successfully");window.location.href="/viewbusroute"</script>''')
class deleteroute(View):
    def get(self, request, id):
        c=busroute_model.objects.get(id=id)
        c.delete()
        return HttpResponse('''<script>alert("Bus route deleted successfully");window.location.href="/viewbusroute"</script>''')
class editroute(View):
    def get(self, request, id):
        c=busroute_model.objects.get(id=id)
        return render(request, 'administrator/editbusroute.html', {'data':c})
    def post(self, request, id):
            obj=busroute_model.objects.get(id=id)
            c=busroute_form(request.POST,instance=obj)
            if c.is_valid():
                c.save()
                return HttpResponse('''<script>alert("Bus route updated successfully");window.location.href="/viewbusroute"</script>''')
            
class dash(View):
    def get(self, request):
        return render(request, 'administrator/dash.html')
class driverRE(View):
    def get(self, request):
        return render(request, 'administrator/driverRE.html')
    def post(self,request):
        c=driver_form(request.POST)
        if c.is_valid():
            reg = c.save(commit = False)
            driver = login_model.objects.create(username = reg.email, password = request.POST['password'], user_type = "driver", status = "pending")
            reg.bus_id = driver
            reg.save()
            return HttpResponse('''<script>alert("Driver added successfully");window.location.href="/"</script>''')
class Delete(View):
    def get(self, request, id):
        c=Driver_model.objects.get(id=id)
        print(c)
        c.delete()
        return HttpResponse('''<script>alert("Driver deleted successfully");window.location="/viewdriver"</script>''')
class edit(View):
    def get(self, request, id):
        c=Driver_model.objects.get(id=id)
        return render(request, 'administrator/editdriver.html', {'data':c})
    def post(self, request, id):
         obj=Driver_model.objects.get(id=id)
         c=driver_form(request.POST,instance=obj)
         if c.is_valid():
            c.save(commit = False)
            driver = login_model.objects.get(id = obj.bus_id.id)
            driver.username = request.POST['email']
            driver.save()
            c.save()
            return HttpResponse('''<script>alert("Driver updated successfully");window.location="/viewdriver"</script>''')
class feedback(View):
    def get(self, request):
        return render(request, 'administrator/feedback.html')
class ownerlist(View):
    def get(self, request):
        return render(request, 'administrator/ownerlist.html')

class ownerRE(View):
    def get(self, request):
        return render(request, 'owner/ownerRE.html')
    def post(self,request):
        c=ownerRE_form(request.POST)
        if c.is_valid():
            reg = c.save(commit = False)
            owner = login_model.objects.create(username = reg.email, password = request.POST['password'], user_type = "owner")
            reg.owner_id = owner
            reg.save()
            return HttpResponse('''<script>alert("Owner added successfully");window.location.href="/viewowner"</script>''')

class rating(View):
    def get(self, request):
        return render(request, 'administrator/rating.html')
class stopdetails(View):
    def get(self, request):
        return render(request, 'administrator/stopdetails.html')
class trip(View):
    def get(self, request):
        return render(request, 'administrator/trip.html')
class VBD(View):
    def get(self, request):
        return render(request, 'administrator/VBD.html')
class viewapproveowner(View):
    def get(self, request):
        c = ownerRE_model.objects.all()
        return render(request, 'administrator/viewapproveowner.html', {'data': c})
class approve(View):
    def get(self, request, id):
        c = get_object_or_404(ownerRE_model, id=id)
        c.status = "approved"
        c.save()
        return HttpResponse('''<script>alert("Owner approved successfully");window.location.href="/viewapproveowner"</script>''')
        
class bus(View):
    def get(self, request):
        return render(request, 'owner/bus.html')
    def post(self,request):
        c=bus_form(request.POST)
        if c.is_valid():
            c.save()
            return HttpResponse('''<script>alert("Bus added successfully");window.location.href="/viewbus"</script>''')
class viewbus(View):
    def get(self, request):
        c = bus_model.objects.all()   
        return render(request, 'administrator/viewbus.html', {'data': c})
class viewbusdetails(View):
    def get(self, request):
        return render(request, 'administrator/viewbusdetails.html',)
class viewdriver(View):
    def get(self, request):
        c=Driver_model.objects.all()
        return render(request, 'administrator/viewdriver.html', {'data':c})
class viewowner(View):
    def get(self, request):
        c=ownerRE_model.objects.all()
        return render(request, 'owner/viewowner.html', {"data":c})
class ownerph(View):
    def get(self, request):
        return render(request, 'owner/ownerhp.html')
class viewbusroute(View):
    def get(self, request):
        c=busroute_model.objects.all()
        return render(request, 'owner/viewbusroute.html', {"data":c})
class viewstopdetails(View):
    def get(self, request):
        c=stop_model.objects.all()
        return render(request, 'owner/viewstopdetails.html', {"data":c})
class addBS(View):
    def get(self, request):
        c = busroute_model.objects.all()
        return render(request, 'administrator/addBS.html', {'data':c})
    def post(self,request):
        c=stop_form(request.POST)
        if c.is_valid():
            c.save()
            return HttpResponse('''<script>alert("Bus stop added successfully");window.location.href="/viewstopdetails"</script>''')


class Accept_Owner(View):
    def get(self, request, id):
        c = ownerRE_model.objects.get(id=id)
        c.owner_id.status = "approved"
        c.owner_id.save()
        return HttpResponse('''<script>alert("Owner approved successfully");window.location.href="/viewowner"</script>''')
class Reject_Owner(View):
    def get(self, request, id):
        c = ownerRE_model.objects.get(id=id)
        c.owner_id.status = "rejected"
        c.owner_id.save()
        return HttpResponse('''<script>alert("Owner rejected successfully");window.location.href="/viewowner"</script>''')

class blockbus(View):
    def get(self, request, id):
        c = bus_model.objects.get(id=id)
        c.status = "blocked"
        c.save()
        return HttpResponse('''<script>alert("Bus blocked successfully");window.location.href="/viewbus"</script>''')
class unblockbus(View):
    def get(self, request, id):
        c = bus_model.objects.get(id=id)
        c.status = "unblocked"
        c.save()
        return HttpResponse('''<script>alert("Bus unblocked successfully");window.location.href="/viewbus"</script>''')