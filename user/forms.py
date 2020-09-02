from django import forms #import froms
from django.contrib.auth.models import User #import user
from django.contrib.auth.forms import UserCreationForm #import UserCreationForm

class UserRegisterForm(UserCreationForm): # create UserRegisterForm inhert from UserCreationForm
    email = forms.EmailField() # default ( required = True) , wanna make it optional (required = False)


    class Meta :
        # class Meta : gives us nested name space for Configuration , and keeps these Configuration in one place
        #  and within Configuration that models effect( Users ) going to save these in Users model
        model = User # specify the model we want to interact with (here its User)
        fields = ['username', 'email', 'password1' , 'password2', ] #field going to shown in forms (in order as written )

        #import  these UserRegisterForm to user/views.py
