from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from . forms import CustomeRegistrationForms,ProfileUpdateForm,UserUpdateForm
from django.contrib.auth.decorators import login_required


# Create your views here.
# This is ready to use register form
'''def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)  
        if form.is_valid():
            username = form.cleaned_data.get('username')
            form.save()
            messages.success(request,f'Account Created Successfully for user {username} !!!')
            return redirect('blog-home')     
    else:
        form = UserCreationForm() 
    return render(request,'register.html',{'form':form})'''

# custom register form

def register(request):
    if request.method == "POST":
        form = CustomeRegistrationForms(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            form.save()
            messages.success(request,f"Account Created Successfully for user {username} !!!")
            return redirect("login")
    else:
        form = CustomeRegistrationForms()  
    return render(request,'register.html',{'form':form})

# For make changes in profile
@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
         
    
    context = {
        'u_form': u_form,
        'p_form': p_form
        }   
    return render(request,'profile.html',context)
