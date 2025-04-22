from django.shortcuts import render, redirect, get_object_or_404
from .models import Employee


def employee_new(request):
    return render(request, 'employees/employee_new.html')

def employee_create(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        Employee.objects.create(name=name, email=email)
        return redirect('employee_index')
    return redirect('employee_new')

def employee_list(request):
    employees = Employee.objects.all()
    return render(request, 'employees/employee_list.html', {'employees':employees})

def employee_edit(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    return render(request, 'employees/employee_edit.html', {'employee': employee})

def employee_update(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    if request.method == 'POST':
        employee.name = request.POST['name']
        employee.email = request.POST['email']
        employee.save()
        return redirect('employee_index')
    return redirect('employee_edit', pk=pk)

def employee_confirm_delete(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    return render(request, 'employees/employee_confirm_delete.html', {'employee': employee})

def employee_delete(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    employee.delete()
    return redirect('employee_index')
