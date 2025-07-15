from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import logout

from Admin.models import Info


# Create your views here.
@login_required()
def admin(request):
    people = Info.objects.all()
    return render(request,'admin.html',{'people':people})


@login_required()
def add_student(request):

    if request.method == "POST":
        name = request.POST.get('name')
        course = request.POST.get('course')
        email = request.POST.get('email')

        Info.objects.create(
            name = name,
            course = course,
            email = email
        )
        return redirect('Admin')
    return render(request, 'add_student.html')


@login_required()
def edit(request,id):
    person = get_object_or_404(Info,id=id)
    if request.method == "POST":
        person.name = request.POST.get('name')
        person.course = request.POST.get('course')
        person.email = request.POST.get('email')
        person.save()
        return redirect('Admin')
    return render(request, 'edit.html' ,{'person':person})


@login_required()
def delete(request,id):
    person = get_object_or_404(Info,id=id)
    try:
        person.delete()
        messages.success(request,'Person has been deleted successfully')
    except Exception as e:
        messages.error(request,"Person has not been deleted ")
    return redirect('Admin')

def login_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('Admin')
        else:
            return render(request, 'login.html')
    return render(request,'login.html')


def logout_view(request):

    logout(request)
    return redirect('login')

