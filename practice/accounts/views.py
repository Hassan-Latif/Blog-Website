from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
# Create your views here.

def signup_view(request):
    if request.method=='POST':
        form = UserCreationForm(request.POST)
        print('its working till here')
        if form.is_valid():
            print('hello world')
            form.save()
            return redirect('articles:list')
        #Log the user in
    
    else:
        form=UserCreationForm()

    return render(request,'accounts/signup.html',{'form':form})

def login_view(request):
    if request.method == 'POST':
        form=AuthenticationForm(data=request.POST)
        if form.is_valid():

            return redirect('articles:list')

    else:
        form=AuthenticationForm()
    return render(request,'accounts/login.html',{'form':form})