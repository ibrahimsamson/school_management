from django import forms
from allauth.account.forms import SignupForm
from django.utils.translation import ugettext_lazy as _


class CustomSignupForm(SignupForm):
    username = forms.CharField(max_length=30)
    first_name = forms.CharField(max_length=30, label='First Name')
    last_name = forms.CharField(max_length=30, label='Last Name')
    #joined = forms.DateField(auto_now=True)


    def signup(self): 
        user.username = self.cleaned_data['username']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.save()
        return user

    def save(self, request):

        # Ensure you call the parent class's save.
        # .save() returns a User object.
        user = super(CustomSignupForm, self).save(request)

        # Add your own processing here.
        # You must return the original result.
        return 