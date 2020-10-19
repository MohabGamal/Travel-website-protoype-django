from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from . models import Profile



class SignupForm(UserCreationForm,):    # must be 'UserCreationForm' to eyncrpt password
    class Meta:
        model=User
        fields=['username','email','password1','password2',]
                        #defult cloumns for users in django
                        
    email=forms.EmailField(required=True)

    def clean_email(self):
        # Get the email
        email = self.cleaned_data.get('email')
    
        # Check to see if any users already exist with this email as a username.
        try:
            match = User.objects.get(email=email)   # if written email == another user.email in db
        except User.DoesNotExist:
            # Unable to find a user with, this is fine
            return email

        # A user was found with this as a username, raise an error.
        raise forms.ValidationError(
            ('Email address: %(email)s is already in use.'),
            params={'email': email},    # to give the message the written email 
        )
    
    

#two froms to edit profile

class UserForm(forms.ModelForm):        #built in user data (users)  
    class Meta:
        model= User
        fields=['username','first_name','last_name',]




class ProfileForm(forms.ModelForm):      #my user data       (profiles)
    class Meta:
        model = Profile
        fields= '__all__'
        exclude=('user',)




