from django.urls import path
from .views import submit_enquiry, enquiry_list

urlpatterns = [
    path('', enquiry_list, name='home'),  # root of app points to list
    path('submit/', submit_enquiry, name='submit-enquiry'),
    path('list/', enquiry_list, name='enquiry-list'),
]
