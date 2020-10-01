from django.shortcuts import redirect, render
from . form import *
from django.contrib.auth import authenticate, login
from . models import Profile
from django.urls import reverse
from django.contrib.auth.decorators import login_required
# Create your views here.


def signup(request):
    if request.method=="POST":
        form=SignupForm(request.POST)
        if form.is_valid():
            form.save()  #to log in automaticly after signing up 
            username= form.cleaned_data['username']
            password= form.cleaned_data['password1']
            user= authenticate(username=username, password=password)
            login(request,user)
            return redirect(reverse('accounts:profile'))

    else:
        form = SignupForm()


    return render(request, 'registration/signup.html',{'form':form})  


@login_required
def profile(request):
    profile= Profile.objects.get(user=request.user)
    return render(request, 'profiles/profile.html',{'profile': profile})



@login_required
def profile_edit(request):
    profile= Profile.objects.get(user=request.user)

    if request.method=='POST':
        userform=UserForm(request.POST,instance=request.user)
        profileform= ProfileForm(request.POST, request.FILES, instance=profile )
        if userform.is_valid() and profileform.is_valid():
            userform.save()
            myprofile= profileform.save(commit=False)
            myprofile.save()
            return redirect(reverse('accounts:profile'))

                                      #to give the page the logged in user data 
    else:                             #↑
        userform = UserForm(instance=request.user)     
        profileform = ProfileForm(instance=profile)


    return render(request,'profiles/profile_edit.html',{'userform': userform ,'profileform':profileform})










