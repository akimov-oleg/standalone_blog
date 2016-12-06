from django.shortcuts import render, HttpResponseRedirect, render_to_response as rtr
from django.contrib import auth
from django.http import Http404
from .forms import MyRegistrationForm


# Create your views here.
def index_page(request):
    dic_info = {
        "intro": "", 
    }

    return render(request, "index.html", dic_info)

def login_page(request):
    dic_info = {
        "login": True, 
    }

    return render(request, "login.html", dic_info)

def registration_page(request):
    dic_info = {
        "login": False, 
    }

    return render(request, "registration.html", dic_info)


def login(request):
    if request.method == 'POST':
        print("POST data =", request.POST)
        username = request.POST.get('login')
        password = request.POST.get('password')
        user = auth.authenticate(username=username, password=password)
        print('login -> user =', user)
        if user is not None:
            auth.login(request, user)            
            return HttpResponseRedirect("/login/")            
        else:            
            return render(request, 'login.html', {'username': username, 'errors': True})
            
    raise Http404


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect("/login/")

    
def registration(request):
    if request.method == 'POST':        
        form = MyRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/login/')
        context = {'form': form,}
        return render(request, 'registration.html', context)
    context = {'form': MyRegistrationForm()}
    return render(request, 'registration.html', context)
    

