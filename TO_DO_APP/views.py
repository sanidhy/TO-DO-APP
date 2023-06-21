from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponse
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth.models import User
from django.shortcuts import render,HttpResponse,redirect

from TO_DO_APP.forms import TODOForm
from TO_DO_APP.models import TODO

# Create your views here.
def index(request):
    return render(request,'index.html')

def about(request):
    return render(request,'aboutus.html')


def second_page(request):
    if request.user.is_authenticated:
        user = request.user
        form = TODOForm()
        todos = TODO.objects.filter(user = user).order_by('priority')
        return render(request , 'second_page.html' , context={'form' : form , 'todos' : todos})


def login(request):
    if request.method=="POST":
        username=request.POST.get('username')
        pass1=request.POST.get('password')
        # print(username,pass1)
        user=authenticate(request,username=username,password=pass1)
        if user is not None:
            auth_login(request,user)
            return redirect('second_page')
        else:
            return HttpResponse("Username or password is incorrect!!")
    return render(request,'login.html')

def signup(request):
    if request.method=="POST":
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')
        # print(uname,pass1,pass2)
        if pass1!=pass2:
            return HttpResponse("Your PassWord are not same")
        else:
            my_user=User.objects.create_user(uname,email,pass1)
            my_user.save()
            return redirect('login')
        
    return render(request,'signup.html')


def add_todo(request):
    if request.user.is_authenticated:
        user = request.user
        print(user)
        form = TODOForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            print("Y")
            todo = form.save(commit=False)
            print("U")
            todo.user = user
            todo.save()
            print(todo)
            return redirect("second_page")
        else: 
            return render(request , 'second_page.html' , context={'todos' : form})

    

def delete_todo(request , id ):
    print(id)
    TODO.objects.get(pk = id).delete()
    return redirect('second_page')

def change_todo(request , id  , status):
    todo = TODO.objects.get(pk = id)
    todo.status = status
    todo.save()
    return redirect('second_page')

