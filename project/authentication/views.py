from typing import Any
from django.shortcuts import render, redirect
from . import forms
from django.urls import reverse_lazy
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.views import LoginView , LogoutView
from django.contrib.auth.decorators import login_required
# Create your views here.


def register(request):
    if request.method == 'POST':
        form = forms.registerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = forms.registerForm()
    return render(request, 'auth.html',{'form' : form ,'type':'Registration'})

def userlogin(request):
    if request.method == 'POST':
        form = AuthenticationForm(request,request.POST)
        print('form')
        if form.is_valid():
            name = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username = name, password = password)

            print('form')
            if user is not None :
                login(request, user)
                return redirect('profile')
    else:
        form = AuthenticationForm()
    return render(request, 'auth.html',{'form' : form ,'type':'Login'})

class userLoginView(LoginView):
    template_name = 'auth.html'
    def form_valid(self, form):
        return super().form_valid(form)

    def form_invalid(self, form):
        return super().form_invalid(form)
    def get_context_data(self, **kwargs) :
        context = super().get_context_data(**kwargs)
        context['type'] = 'Login'
        return context
    def get_success_url(self):
        return reverse_lazy('profile')
    


def userLogout(request):
    logout(request)
    return redirect('home')

@login_required
def changeuser(request):
    if request.method == 'POST':
        form = forms.changeUser(request.POST, instance = request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = forms.changeUser(instance = request.user)
    return render(request, 'auth.html',{'form' : form ,'type':'Edit'})
