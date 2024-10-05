from django.shortcuts import render
from django.http import HttpResponse
from .models import Student
from .models import Query


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
        if password==c_password:
            Student.objects.create(stu_name=name,stu_email=email,stu_contact=contact,stu_password=password)
            user=Student.objects.filter(stu_email=email)
            
            print(user)
            if user:
                
                msg="Data Already Exist"
                return render(request,'register.html',{'msg':msg})
            else:
                # Student.objects.create(stu_name=name,stu_email=email,stu_contact=contact,stu_password=password)
                msg="Data Successfully Submitted"
                return render(request,'login.html', {'msg':msg})
        else:
            msg="Password not matched"
            return render(request,'register.html',{'msg':msg})
        
    return render(request,'register.html')

        # Student.objects.create(stu_name=name,stu_email=email,stu_contact=contact,stu_password=password)
    #     user=Student.objects.filter(stu_email=email)
    #     # user=Student.objects.get(stu_email=email)
    #     if user:
    #         msg="Email already exist"
    #         return render(request,'register.html',{'msg':msg})
    #     else:
    #         Student.objects.create(stu_name=name,stu_email=email,stu_contact=contact,stu_password=password)
    #         msg="registration succesful!!"
    #         return render(request,'login.html',{'msg':msg}) 
    # return render(request,'register.html')

def login(request):
    if request.method=="POST":
        email=request.POST.get('email')
        password=request.POST.get('password')
        user=Student.objects.filter(stu_email=email)
        if user:
            user_data=Student.objects.get(stu_email=email)
            print(user)
            email1=user_data.stu_email
            name1=user_data.stu_name
            contact1=user_data.stu_contact
            password1=user_data.stu_password
            print(name1,email1,contact1,password1)
            if password==password1:
                data={
                    'name':name1,
                    'email':email1,
                    'contact':contact1,
                    'password':password1
                }
                return render(request,'dashboard.html',{'data':data})
            else:
                msg="Email & password not matched"
                return render(request,'login.html',{'msg':msg})
            
        else:
            msg="Email not registered!!"
            return render(request,'register.html',{'msg':msg})
            

    else:
        
        return render(request,'login.html')

def dashboard(request):
    return render(request,'dashboard.html')

    
#single value returm-----------------------    
# def first(request):
#     data=Student.objects.first()
#     print(data)
#     return HttpResponse(data)
    
# def last(request):
#     data=Student.objects.last()
#     print(data)
#     return HttpResponse(data)
    
# def latest(request):
#     data=Student.objects.latest('id')
#     print(data)
#     return HttpResponse(data)
    
# def earliest(request):
#     data=Student.objects.earliest('id')
#     print(data)
#     return HttpResponse(data)

# def exists(request):
#     data=Student.objects.all()
#     print(data)
#     return HttpResponse(data)

# def update(request):
#     data=Student.objects.filter(stu_email="akku@gmail.com").update(stu_name='Akku')

#     print(data)
#     return HttpResponse(data)

#----------------------------------------------------------------------------------
#multiple object return----------------
# def all_details(request):
#     data=Student.objects.all().values_list('stu_name','stu_email','stu_contact','stu_password')
#     print(data.values_list())
#     return HttpResponse(data)
   
# def filter(request):
#     data=Student.objects.filter(stu_name="Akansha Bagde")
#     print(data.values)
#     return HttpResponse(data)

# def exclude(request):
#     data=Student.objects.exclude(stu_email="akanshabagde01@gmail.com")
#     print(data.values)
#     return HttpResponse(data)

# def acending(request):
#     data=Student.objects.order_by('stu_name') #ascending
#     data=Student.objects.order_by('stu_name').reverse()
#     print(data.values)
#     return HttpResponse(data)

# def descending(request):
#     data=Student.objects.order_by('-stu_name') #descending
#     print(data.values)
#     return HttpResponse(data)

# def random(request):
#     data=Student.objects.order_by('?') #random
#     print(data.values)
#     return HttpResponse(data)

# def slice(request):
#     data=Student.objects.all().reverse()
#     # data = Student.objects.all().order_by('-id')[:4] 
#     print(data)
#     return HttpResponse(data)

def query(request):
    if request.method=='POST':
        name1=request.POST.get('name')
        email1=request.POST.get('email')
        query1=request.POST.get('query')
        Query.objects.create(stu_name=name1,stu_email=email1,stu_query=query1)
        data=Student.objects.get(stu_email=email1)
        print(data)
        data1={
            'name':data.stu_name,
            'email':data.stu_email,
            'contact':data.stu_contact,
            'password':data.stu_password
        }
        query_data=Query.objects.filter(stu_email=email1)
        return render(request,'dashboard.html',{'data1':data1,'query_data':query_data})
    
        # return render(request,'dashboard.html',{'data':data})


    

    
