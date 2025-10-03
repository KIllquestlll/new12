from django.shortcuts import render,get_object_or_404,redirect
from . models import Post
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.models import User

# Create your views here.

def index(request):
    posts = Post.objects.all()
    return render(request, 'main/index.html',{'posts':posts})


def post_detail(request,pk):
    post = get_object_or_404(Post,pk=pk)
    return render(request,'main/post_detail.html',{'post':post})


def logout_view(request):
    logout(request)
    return redirect('index')

def register_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if User.objects.filter(username=username).exists():
            return render(request,'main/index.html',{'error':'Имя уже занято!'})
        
        user = User.objects.create_user(username=username,password=password)
        login(request,user)
        return redirect('index')
    return redirect('index')


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request,username=username,password=password)
        if user is not None:
            login (request,user)
            return redirect('index')
        else:
            return render(request,'main/index.html',{'login_error':'Неверный логин или пароль'})
        
    return redirect('index')

