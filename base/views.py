from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required
# from .forms import Profile_form

chatrooms=[
    {'id':1,'name':'RS1'},
    {'id':2,'name':'RS2'},
    {'id':3,'name':'RS3'},
]




def loginPage(request):
     page='login'
     if request.method =='POST':
          username=request.POST.get('username').lower()
          password=request.POST.get('password')
          
          try:
               user=User.objects.get(username=username)
          except:
               messages.error(request,'User does not exist')

          user=authenticate(request,username=username,password=password)

          if user is not None:
               login(request,user)
               return redirect('chats')
          else:
               messages.error(request,"User name or password are incorrect")
            
          
     context={'page':page}
     return render(request,'base/login_register.html',context)

def logoutUser(request):
     logout(request)
     return redirect('chats')

def registerPage(request):
     page='register'
     form=UserCreationForm()
     
     if request.method=='POST':
          form=UserCreationForm(request.POST)
          if form.is_valid():
               user=form.save(commit=False)
               user.username=user.username.lower()
               user.save()
               login(request,user)
               return redirect('editprofile')
          else:
               messages.error(request,'An error ocurred during registration')

     return render(request,'base/login_register.html',{'form':form})


def chats(request):
#     i need to get all chat rooms of this person where he is invloved 
# then i render them 
    return render(request,'base/chats.html',{'chats':chatrooms})

# @login_required
def chatroom(request,pk):
    room=None

    for i in chatrooms:
        if i['id']==int(pk):
                room=i
    context={'room':room}
    return render(request,'base/chatroom.html',context)

@login_required
def userdetails(request):
    
    user = request.user # Get the currently logged-in user
    context = {'user': user }
    return render(request, 'base/userdetails.html', context)
@login_required
def edit_profile(request):
#     if request.method == 'POST':
#          =request.POST.get()
#          =request.POST.get()
#          =request.POST.get()
    
#      #    form = 
#      #    if form.is_valid():
#      #        form.save()
#      #        return redirect('userdetails')  # Redirect to the user's profile page or any other page
#     else:
#        form = Profile_form(instance=request.user.userprofile, user=request.user)
  # Pass the user to the form

#     context = {'form': form}
    return render(request, 'base/editprofile.html')
