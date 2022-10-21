from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from .forms import MyUserCreationForm
from .models import User, Topic, Category, Level, Chapter


# Create your views here.

def home(request):
    topics = Topic.objects.all()
    categories = Category.objects.all()
    levels = Level.objects.all()

    context = {'topics': topics, 'categories': categories, 'levels': levels}
    return render(request, 'base/home.html', context)


def topic(request, pk):
    topic = Topic.objects.get(id=pk)

    chapter = topic.start_chapter
    chapters = [topic.start_chapter]
    while chapter.next is not None:
        chapters.append(chapter.next)
        chapter = chapter.next

    chapter = request.GET.get('chapter') if request.GET.get('chapter') != None else ''
    chapter = Chapter.objects.get(id=chapter)

    context = {'topic': topic, 'chapters': chapters, 'chapter': chapter}
    return render(request, 'base/topic.html', context)


def category(request, cat):
    topics = Topic.objects.filter(categories__name=cat)

    context = {'topics': topics}
    return render(request, 'base/category.html', context)


def loginPage(request):
    page = 'login'

    if request.method == 'POST':
        email = request.POST.get('email').lower()
        password = request.POST.get('password')

        try:
            user = User.objects.get(email=email)
        except:
            messages.error(request, 'User does not exist')

        user = authenticate(request, email=email, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Username OR password does not exist')

    context = {'page': page}
    return render(request, 'base/login_register.html', context)


def registerPage(request):
    form = MyUserCreationForm()
    page = 'register'

    if request.method == 'POST':
        form = MyUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.email = user.username.lower()
            user.save()
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Error occured')

    context = {'page': page, 'form': form}
    return render(request, 'base/login_register.html', context)


def logoutPage(request):
    logout(request)
    return redirect('home')
