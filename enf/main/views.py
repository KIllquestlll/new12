from django.shortcuts import render,get_object_or_404,redirect
from . models import Post,Comment
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.models import User

# Create your views here.

def index(request):
    # Вывод всех постов
    # (На главную страницу)

    posts = Post.objects.all()
    return render(request, 'main/index.html',{'posts':posts})


def post_detail(request,pk):
    # Вывод постов
    post = get_object_or_404(Post,pk=pk)
    comments = post.comments.all()
    return render(request,'main/post_detail.html',{'post':post,'comments':comments})


def logout_view(request):
    # Выход с аккаунта
    logout(request)
    return redirect('index')

def register_view(request):
    # Форма для регистрации
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
    # форма для авторизации
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
