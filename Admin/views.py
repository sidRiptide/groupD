from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect

from Admin.models import Info


# Create your views here.
def admin(request):
    people=Info.objects.all()
    return render(request,'admin.html',{'people':people})

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
def edit(request,id):
    person = get_object_or_404(Info,id=id)
    if request.method == "POST":
        person.name = request.POST.get('name')
        person.course = request.POST.get('course')
        person.email = request.POST.get('email')
        person.save()
        return redirect('Admin')
    return render(request, 'edit.html' ,{'person':person})
def delete(request,id):
    person = get_object_or_404(Info,id=id)
    try:
        person.delete()
        messages.success(request,'Person has been deleted successfully')
    except Exception as e:
        messages.error(request,"Person has not been deleted ")
    return redirect('Admin')