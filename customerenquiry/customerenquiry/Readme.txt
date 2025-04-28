Project level: customerenquiry

settings.py: Included new Database settings to connect to MariaDB(Mysql), include DB name, user and pwd to connect

            DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',  # Yes, MariaDB uses MySQL backend
        'NAME': 'customer_leads_db',
        'USER': 'leaduser',
        'PASSWORD': 'leadpass123',
        'HOST': 'localhost',        # or your database host
        'PORT': '3306',             # default MariaDB/MySQL port
        'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
        },
    }
}


urls.py: redirected the urls path to  "enquiry.url"-->(application urls)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('enquiry/', include('enquiry.urls')),  # app handles root
]

Application level: enquiry

1)models.py:Django models represent tables in your database

Created CustomerEnquiry class which is equal to Table name in DB. with th einstance fields mapped to column names

===========Input From User==========
    customer_name=models.CharField(max_length=100)
    phone=models.CharField(max_length=10, blank=True)
    email=models.EmailField(max_length=200, blank=True)
    query=models.CharField(max_length=500)

 ========we need to generate======
    status=models.CharField(max_length=20,default='new')
    query_id=models.CharField(primary_key=True,max_length=30,default=getQueryID)

 Note: getQueryID method generates a unique id for the query cal with the method name dont include () to let it invoke everytime



2)urls.py:

from .views import submit_enquiry, enquiry_list ### import both the methods from views
bydefault: http://127.0.0.1:8001/enquiry/   ### As we are calling from application

urlpatterns = [
    path('', enquiry_list, name='home'),  # root of app points to list ## default it will display enquiry list
    path('submit/', submit_enquiry, name='submit-enquiry'),## path('url','view name','name=optional name')
    path('list/', enquiry_list, name='enquiry-list'),
]
 to invoke submit: http://127.0.0.1:8001/enquiry/submit/
 to invoke list of enquiries: http://127.0.0.1:8001/enquiry/list/


3)forms.py:

from .models import CustomerEnquiry ### get the model class from CustomerEnquiry


class CustomerEnquiryForm(forms.ModelForm): ## (This creates a Django form based on the CustomerEnquiry model.
                                                forms.ModelForm is a Django shortcut that automatically generates a form based on a model — no need to manually
                                                define every field.)

    class Meta:    ##Inner class Meta tells Django extra information about the form.

        model=CustomerEnquiry ## create an object reference for the class
        fields=['customer_name','phone','email','query'] ## Specify what fields to show to user from the form

4)views.py:

 from django.shortcuts import render,redirect       # for url redirect and render HTML
 from .models import CustomerEnquiry                # to use the class
 from .forms import CustomerEnquiryForm             # Form to display

 ===================(1) submit_enquiry() method===========
If submitting → validate → save → redirect.

If visiting → show blank form.


 def submit_enquiry(request):                       # when the user requested '/submit' submit_enquiry() method will be called with 'request' as an argument
    if request.method == 'POST':                    #Checks if the form was submitted (i.e., user pressed "Submit" button).
                                                    #In HTML forms, when you submit, the method is usually POST.
        form = CustomerEnquiryForm(request.POST)    #Creates a form instance, filling it with the POSTed data (user's input).

        if form.is_valid():                         #Django validates the form (checks if fields are correctly filled — e.g., email is a valid email, required fields aren't empty, etc.)

            form.save()                             #If form is valid, save the form data into the database by creating a new CustomerEnquiry record.

            return redirect('enquiry-list')         #After saving, redirect(calling another method) the user to another page (to a URL named 'enquiry-list' in your urls.py).This avoids re-submitting the form if the user refreshes.
    else:
        form = CustomerEnquiryForm()                # If it's not a POST (like a normal page visit, GET request), create an empty form to show to the user.
    return render(request,'submit_enquiry.html',{'form':form}) #render the HTML template submit_enquiry.html and pass the form to the template.

    ============================(2)enquiry_list() method==============

    this function shows list of all enquiries

    def enquiry_list(request):

    enquiries=CustomerEnquiry.objects.all().order_by('-query_id') ## Get all customer enquiries from the CustomerEnquiry table in the database ordered by 'qury-id'descending the newest first

    return render(request,'enquiry_list.html',{'enquiries':enquiries}) ##Renders the enquiry_list.html page and passes the list of enquiries to the template.


5)Templates Folder(for HTML files):






