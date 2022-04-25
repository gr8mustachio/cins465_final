from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from core.forms import JoinForm, LoginForm
# Create your views here.
def main(request):
    return render(request, 'core/home.html')
    #return HttpResponse("Dashboard Home Page")


def about(request):
    return render(request, 'core/about.html')

def user_login(request):
    #return HttpResponse("Login Page")
    if(request.method == 'POST'):
        login_form = LoginForm(request.POST)
        if(login_form.is_valid()):
            #get username and password given
            username = login_form.cleaned_data["username"]
            password = login_form.cleaned_data["password"]
            #django auth function
            user = authenticate(username=username, password=password)
            #if user exists
            if user:
                #check if is_active
                if(user.is_active):
                    #log them in
                    login(request,user)
                    #send to homepage
                    return redirect("/")
                    #return render(request)
                else:
                    #account not active
                    return HttpResponse("Your account is not active.")
            else:
                print("someone tried to login and failed")
                print("they used username: {} and password {}".format(username,password))
                return render(request, 'core/login.html', {"login_form": LoginForm})
    else:
                #nothing provided
        return render(request, 'core/login.html', {'login_form': LoginForm})


@login_required(login_url='/login/')
def user_logout(request):
    #log out user
    logout(request)
    #return to homepage
    return redirect("/")

def join(request):
    #return HttpResponse("Join Page")
    if(request.method == 'POST'):
        join_form = JoinForm(request.POST)
        if(join_form.is_valid()):
            #save the data to DB
            user = join_form.save()
            #encrypt Password
            user.set_password(user.password)
            #save encrypted password to db
            user.save()
            #success, back to homepage
            return redirect("/")
        else:
            #form is invalid, print error to console
            page_data = { "join_form": join_form }
            return render(request, 'core/join.html', page_data)
    else:
        join_form = JoinForm()
        page_data = { "join_form": join_form }
        return render(request, 'core/join.html', page_data)
    