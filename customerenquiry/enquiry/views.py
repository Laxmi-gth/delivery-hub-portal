from django.shortcuts import render,redirect
from .models import CustomerEnquiry
from .forms import CustomerEnquiryForm

# Create your views here.
def submit_enquiry(request):
    if request.method == 'POST':
        form = CustomerEnquiryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('enquiry-list')
    else:
        form = CustomerEnquiryForm()
    return render(request,'submit_enquiry.html',{'form':form})
def enquiry_list(request):
    enquiries=CustomerEnquiry.objects.all().order_by('-query_id')
    count = CustomerEnquiry.objects.all().count()
    return render(request,'enquiry_list.html',{'enquiries':enquiries,'count': count})



