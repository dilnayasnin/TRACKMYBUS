
from django.urls import include, path
from .views import  *  

urlpatterns = [
    path('', Login.as_view(), name='login'),
    path('addBS', addBS.as_view(), name='addBS'),
    path('busroute', busroute.as_view(), name='busroute'),
    path('dash', dash.as_view(), name='dash'),
    path('driverRE', driverRE.as_view(), name='driverRE'),
    path('feedback', feedback.as_view(), name='feedback'),
    path('ownerlist', ownerlist.as_view(), name='ownerlist'),
    path('ownerRE', ownerRE.as_view(), name='ownerRE'),
    path('rating', rating.as_view(), name='rating'),
    path('stopdetails', stopdetails.as_view(), name='stopdetails'),
    path('trip', trip.as_view(), name='trip'),
    path('VBD.,', VBD.as_view(), name='VBD'),
    path('viewapproveowner', viewapproveowner.as_view(), name='viewapproveowner'),
    path('viewbusdetails', viewbusdetails.as_view(), name='viewbusdetails'),
    path('viewdriver', viewdriver.as_view(), name='viewdriver'),
    path('viewowner', viewowner.as_view(), name='viewowner'),
    path('ownerph', ownerph.as_view(), name='ownerph'),
    path('delete/<int:id>', Delete.as_view(), name='deletedriver'),
    path('edit/<int:id>', edit.as_view(), name='editdriver'),
    path('viewbusroute', viewbusroute.as_view(), name='viewbusroute'),
    path('deleteroute/<int:id>', deleteroute.as_view(), name='deleteviewbusroute'),
    path('editroute/<int:id>', editroute.as_view(), name='editviewbusroute'),
    path('viewapproveowner/', viewapproveowner.as_view(), name='viewapproveowner'),
    path('approve/<int:id>/', approve.as_view(), name='approve'),
    path('bus', bus.as_view(), name='bus'),
    path('viewbus', viewbus.as_view(), name='viewbus'),
    path('viewstopdetails', viewstopdetails.as_view(), name='viewstopdetails'),
    path('addBS', addBS.as_view(), name='addBS'),
    path('acceptowner/<int:id>',Accept_Owner.as_view(),name='acceptowner'),
    path('rejectowner/<int:id>',Reject_Owner.as_view(),name='rejectowner'),
    # path('viewbusblockunblock', viewbusblockunblock.as_view(), name='viewbusblockunblock'),
    path('blockbus/<int:id>', blockbus.as_view(), name='blockbus'),
    path('unblockbus/<int:id>', unblockbus.as_view(), name='unblockbus'),
    path('deletebus/<int:id>', deletebus.as_view(), name='deletebus'),
    path('editbus/<int:id>', editbus.as_view(), name='editbus'),   
    
]




