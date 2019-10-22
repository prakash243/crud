from django.shortcuts import render,redirect
from .forms import StudentForm, Subscribe
from .models import Student,Contact
# smtp
from django.shortcuts import render
from cruds.settings import EMAIL_HOST_USER
from . import forms
from django.core.mail import send_mail

# Create your views here.


def createform(request):
    create_form = StudentForm()
    if request.method=='POST':
        create_form = StudentForm(request.POST)
        if create_form.is_valid():
            create_form.save()
            return redirect('formdata')
    return render(request,'create_a_new.html', {'create_form':create_form})

def formdata(request):
    data = Student.objects.all()
    return render(request,'formdatabase.html', {'formdata':data})

def updateform(request, student_id):
    student_id=int(student_id)
    students = Student.objects.get(id=student_id)
    update_form = StudentForm()
    if students:
        update_form = StudentForm(request.POST or None, instance=students)
        if update_form.is_valid():
            update_form.save()
            return redirect('formdata')
    return render(request,'update.html', {'update_form':update_form})

def delete(request, student_id):
    student_id=int(student_id)
    student_name = Student.objects.get(id=student_id)
    if student_name:
        student_name.delete()
        return redirect('formdata')
    return render('formdata')

def submit(request):
    return render(request,'submit.html')

def contact(request):
    data = request.POST
    contact_object = Contact.objects.all()
    a = Contact()
    a.c_name = data['name']
    a.email = data['email']
    a.phone_no = data['number']
    a.company = data['company']
    a.message = data['message']
    a.save()

    return render(request,'submit.html', {'contact_object':contact_object})

#SMTP

# Create your views here.
#DataFlair #Send Email
def subscribe(request):
    sub = Subscribe()
    if request.method == 'POST':
        sub = Subscribe(request.POST)
        subject = 'Welcome to Areon Mobility Tech. Pvt. Ltd'
        message = 'Hope you are enjoying your Django Tutorials'
        recepient = str(sub['Email'].value())
        send_mail(subject,message, EMAIL_HOST_USER, [recepient], fail_silently = False)
        return render(request, 'success.html', )
    return render(request, 'subscribe.html', {'form':sub,})