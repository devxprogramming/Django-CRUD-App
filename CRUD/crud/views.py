from django.shortcuts import render, redirect
from .models import Profile
from django.contrib import messages
from .forms import ProfileForm


# Create your views here.

def home(request):
    if request.method == 'POST':
        firstname = request.POST['Firstname']
        lastname = request.POST['Lastname']
        level = request.POST['level']

        if Profile.objects.filter(firstname=firstname).exists():
            messages.info(request,"Name Already Exist")
            return redirect(home)
        else:
            user = Profile(firstname=firstname, lastname=lastname, level=level)
            user.save() 
            return redirect(home)
    
    showuser = Profile.objects.all()
    context = {'user':showuser}
    return render(request,'home.html', context)


def showform(request):
    todo = Profile.objects.all()
    context = {'user':todo}
    return render(request,'form.html', context)

def delete(request, user_id):
    user = Profile.objects.get(pk=user_id)
    user.delete()
    return redirect(home)


def update(request, user_id):
    if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        level = request.POST['level']

        updateprofile = Profile(id=user_id,firstname=firstname, lastname=lastname,level=level)
        updateprofile.save()
        return redirect(home)
    getprofile = Profile.objects.get(pk=user_id)
    context = {'user':getprofile}
    return render(request, 'update.html', context)