from django.shortcuts import render, redirect
from datetime import datetime
from eduxationmain.models import Contacts, emailsub
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.
def index(request):
    if request.method == "POST":
        emailss = request.POST.get('emailnew')
        index = emailsub(email=emailss)
        index.save()
    return render(request, 'index.html')

def about(request):
    count = User.objects.count()
    return render(request, 'about.html', {
        'count': count
    })

def videos(request):
    return render(request, 'videos.html')

def quizes(request):
    return render(request, 'quizes.html')

def papers(request):
    return render(request, 'papers.html')
    
def social(request):
    return render(request, 'social.html')
    
def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        subject = request.POST.get('subject')
        contact = Contacts(name=name, email=email, message=message, subject=subject, date = datetime.today())
        contact.save()
        messages.success(request, 'Your message has been sent!')
    return render(request, 'contact.html')
 
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {
        'form': form
    })


#playlists
def cplus(request):
    return render(request, 'playlists/cplus.html')

def dbms(request):
    return render(request, 'playlists/dbms.html')

def dsalgo(request):
    return render(request, 'playlists/dsalgo.html')

def java(request):
    return render(request, 'playlists/java.html')

def php(request):
    return render(request, 'playlists/php.html')



#QUIZeS

def clang(request):
    return render(request, 'quiz/clang.html')

def quiz(request):
    return render(request, 'quiz.html')



@login_required
def secret_page(request):
    return render(request, 'secret_page.html')


class SecretPage(LoginRequiredMixin, TemplateView):
    template_name = 'secret_page.html'