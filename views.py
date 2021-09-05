from django.shortcuts import render
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.template import loader
from .models import Contact_Form
from .form import Con_Form
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,logout
from django.contrib.auth import login

from django.contrib import messages


#from .functions import handle_uploades_file
# Create your views here.

def detail(request):
    electronic=Contact_Form.objects.all()
    return render(request,'show.html',{'electronic': electronic})



def web(request):
    temp=loader.get_template('index.html')
    return HttpResponse(temp.render())


def about(request):
   return render(request, 'about.html')


def services(request):
   return render(request, 'services.html')

def tv(request):
   messages.success(request,'hello user')
   return render(request, 'tv.html')

def home_a(request):
   return render(request, 'home_a.html')

def tv1(request):
   messages.success(request,'hello user')
   return render(request, 'tv1.html')
def tv2(request):
   return render(request, 'tv2.html')
def tv3(request):
   return render(request, 'tv3.html')
def htv1(request):
   return render(request, 'htv1.html')
def hf1(request):
   return render(request, 'hf1.html')
def hd1(request):
   return render(request, 'hd1.html')
def logobg(request):
   return render(request, 'logobg.html')
def decorative(request):
   return render(request, 'decorative.html')
def register(request):
   return render(request, 'register.html')
def search_m(request):
   return render(request, 'search_m.html')



def contact_f(request):

   if request.method == "POST":
      first_name=request.POST.get("first_name")
      last_name=request.POST.get("last_name")
      Mobile_no=request.POST.get("Mobile_no")
      email_id=request.POST.get("email_id")
      address=request.POST.get("address")
      city_area=request.POST.get("city_area")
      zip_no=request.POST.get("zip_no")
      contact_f=Contact_Form(first_name=first_name ,last_name=last_name , Mobile_no=Mobile_no, email_id=email_id ,address=address ,city_area=city_area ,zip_no=zip_no)
      contact_f.save()
      messages.success(request , "Your Detail Has Been Submitted Successfully")
   
   
   return render(request, 'bform.html',)
      
   


def signup(request):
   
   if request.method =='POST':
      Username=request.POST.get("Username")
      Firstname=request.POST.get("Firstname")
      Lastname=request.POST.get("Lastname")
      email =request.POST.get("email")
      pass1=request.POST.get("pass1") 
      pass2=request.POST.get("pass2")
      
      if pass1==pass2:
       if User.objects.filter(username=Username).exists():
          messages.success(request,"Username Already Taken... Choose another")
       elif User.objects.filter(email=email).exists():
          messages.success(request,'Email address already used')
       else:
            myuser =User.objects.create_user(username=Username ,email=email,password=pass1)
            myuser.first_name=Firstname
            myuser.last_name=Lastname
               
            myuser.save()
            messages.success(request , "your Account has been creates Successfully")
         
      else:
         messages.success(request,'password is incorrect')

   return render(request, 'index.html')

   


def A_login(request):
   if request.method =='POST':
      LoginUsername=request.POST['LoginUsername']
      Loginpass=request.POST['Loginpass']

      user =authenticate(username=LoginUsername,  password=Loginpass)
      if user is not None:
         login(request,user)
         messages.success(request,'Logged in Successfully')
         return redirect('/contact_f')
      else:
         messages.success(request,'plzz give valid input')
         return redirect('/')
   return HttpResponse('login')
  



def handlelogout(request):
   logout(request)
   messages.success(request,'Succsessfully logout')
   return redirect('/')




def thank_you(request):
   return render(request, 'thank_you.html')






# def contact_ff(request):
#     if request.method == "POST":
#         stu=Con_Form(request.POST)
#         if stu.is_valid():
#             try:
#                stu.save()
#             except:
#                 pass
#     else:
#         stu=Con_Form()

#     return render(request,'contact_f.html',{'form':stu})







# from django.contrib.auth.decorators import login_required
# from django.contrib.auth import login, authenticate
# from django.contrib.auth.forms import UserCreationForm



# @login_required
# def home(request):
#     return render(request, 'home.html')


# def signup(request):
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             username = form.cleaned_data.get('username')
#             raw_password = form.cleaned_data.get('password1')
#             user = authenticate(username=username, password=raw_password)
#             login(request, user)
#             return redirect('/')
#     else:
#         form = UserCreationForm()
#     return render(request, 'su.html', {'form': form})
