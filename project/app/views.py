from django.shortcuts import render
from .models import Student

# Create your views here.
def home(request):
    return render(request,'home.html')

def register(request):
    if request.method=="POST":
        print(request.POST)
        name=request.POST.get('name')
        email=request.POST.get('email')
        contact=request.POST.get('contact')
        password=request.POST.get('password')
        c_password=request.POST.get('cpass')
        print(name,email,contact,password)
        Student.objects.create(stu_name=name,stu_email=email,stu_contact=contact,stu_password=password)
        user=Student.objects.filter(stu_email=email)
        # user=Student.objects.get(stu_email=email)
        if user:
            msg="Email already exist"
            return render(request,'register.html',{'msg':msg})
        else:
            Student.objects.create(stu_name=name,stu_email=email,stu_contact=contact,stu_password=password)
            msg="registration succesful!!"
            return render(request,'login.html',{'msg':msg}) 
    return render(request,'register.html')

def login(request):
    return render(request,'login.html')

    
    
