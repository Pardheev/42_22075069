# from django import forms
# from django.contrib.auth.models import User
# from .models import UserProfile

# class Profile_form(forms.ModelForm):
#     class Meta:
#         model = UserProfile
#         fields = ['profile_picture','about', 'Date_of_birth'] 

#     def save(self, commit=True):
#         instance = super(Profile_form, self).save(commit=False)
#         if commit:
#             instance.user = self.user 
#             instance.save()
#         return instance

#     def _init_(self, *args, **kwargs):
#         self.user = kwargs.pop('user', None)  
#         super(Profile_form, self)._init_(*args, **kwargs)