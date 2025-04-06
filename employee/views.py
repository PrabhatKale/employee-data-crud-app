from django.shortcuts import render, redirect
from .models import Employee

def home(request):
    employees = Employee.objects.all()
    return render(request, 'home.html', {'employees': employees})

def add_employee(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        position = request.POST['position']
        Employee.objects.create(name=name, email=email, phone=phone, position=position)
        return redirect('home')
    return render(request, 'add.html')

def update_employee(request, id):
    employee = Employee.objects.get(id=id)
    if request.method == 'POST':
        employee.name = request.POST['name']
        employee.email = request.POST['email']
        employee.phone = request.POST['phone']
        employee.position = request.POST['position']
        employee.save()
        return redirect('home')
    return render(request, 'update.html', {'employee': employee})

def delete_employee(request, id):
    employee = Employee.objects.get(id=id)
    employee.delete()
    return redirect('home')
