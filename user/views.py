from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
#flash message to show we received data
from django.contrib import messages # importing message
from .forms import UserRegisterForm #import UserRegisterForm from forms.py so (additional field can shown )


# Create your views here. (here, in this project this app name is user (previous section have users (remove s before use )))


def register(request):
    # condition checking for form get data to post or not
    # (if not condition pass to else statement )
    if request.method == 'POST':
        form = UserRegisterForm(request.POST) # now we a POST data check for validation now
        # now if condition to check data is valid or not
        if form.is_valid(): #if_valid then submitted
            form.save() #saving form data
            username = form.cleaned_data.get('username')
            #messages.success(request, f' Account Created {{ username }} !, Login Now !!')
            #now redirect user to home page
            return redirect('login')
    else:
        # return empty form
        form = UserRegisterForm()
    return render(request, 'user/register.html' , {'form':form})


"""
When you add additional field in form and create a Form.py file
replace your UserRegisterForm with default UserCreationForm

this is a earlier code block of UserCreationForm
in above code UserCreationForm is replaced by UserRegisterForm :)

def register(request):
    # condition checking for form get data to post or not
    # (if not condition pass to else statement )
    if request.method == 'POST':
        form = UserCreationForm(request.POST) # now we a POST data check for validation now
        # now if condition to check data is valid or not
        if form.is_valid(): #if_valid then submitted
            form.save() #saving form data
            username = form.cleaned_data.get('username')
            messages.success(request, f' Account Created { username } !')
            #now redirect user to home page
            return redirect('blog-home')
    else:
        # return empty form
        form = UserCreationForm()
    return render(request, 'users/register.html' , {'form':form})

"""

#message.info, error, warning, success, warning (kind of option we have to flash messages )
