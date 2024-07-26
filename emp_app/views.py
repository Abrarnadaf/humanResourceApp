from django.shortcuts import render , HttpResponse , redirect
from .models import Employee, Designation, Department , Attendance
from datetime import datetime , date
import time
from dateutil.relativedelta import relativedelta
from django.db.models import Q , Count
from .forms import *

# Create your views here.

def index(request):
    return render(request, 'index.html' )

def all_emp(request):
    """Renders the page displaying all employees."""
    employee = Employee.objects.all()
    context={
        "employee":employee
    }
    return render(request, 'all_emp.html' , context)

def add_emp(request):
    """Handles the addition of a new employee."""
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        designation = request.POST['designation']
        dept = request.POST['dept']
        phone = int(request.POST['phone'])
        salary = int(request.POST['salary'])
        email = request.POST['email']
        new_emp = Employee(first_name=first_name, last_name=last_name, designation_id = designation, dept_id =dept, phone=phone, salary=salary , email=email)
        new_emp.save()

        employee = Employee.objects.all()
        context={
            "employee":employee
        }
        return render(request, 'all_emp.html' , context)

    elif request.method == 'GET':
        dept = Department.objects.all()
        designation = Designation.objects.all()
        context={
            "dept":dept ,
            "designation": designation
        }
        return render (request, 'add_emp.html', context )  
    
          
    else:    
        return HttpResponse("Exception employee has not been added" )

print(add_emp)


def remove_emp(request, employee_id = 0):
    """Removes an employee with the given ID."""
    if employee_id:
        try:
            selected_emp = Employee.objects.get(id=employee_id)
            selected_emp.delete()
            return HttpResponse('Employee Removed')
        except:
            return HttpResponse('Employee does not exist')
    emps = Employee.objects.all()
    context = {
        "emps" : emps
    }
    return render(request, 'remove_emp.html', context )

def filter_emp(request):
    """Removes an employee with the given ID."""
    if request.method == "POST":
        name = request.POST['name']
        dept = request.POST['dept']
        designation = request.POST['designation']
        employees = Employee.objects.all()
        if name:
            employees = employees.filter(Q(first_name__icontains=name) | Q(last_name__icontains=name))            
        if dept:
            employees = employees.filter(dept__name__icontains = dept)
        if designation:
            employees = employees.filter(designation__name__icontains = designation)

        
        context = {
            "employee" : employees
        }
        return render(request,'all_emp.html', context)

    elif request.method == 'GET':
        return render(request, 'filter_emp.html' )
    else:
        return HttpResponse ("Request method is invalid")



def emp_report(request):        
    """Generates a report displaying the count of employees in each department."""
    departments = Department.objects.all()
    department_counts = []
    for department in departments:
        t = {}
        count = Employee.objects.filter(dept__id=department.id).count()
        t['dept'] = department.name
        t['count'] = count
        department_counts.append(t)

    return render(request, 'emp_report.html' ,{'dept_counts':department_counts})


def add_attendance(request, empid):
    """Handles the addition of attendance for a specific employee."""
    template_name = "add_attendance.html"
    emp = Employee.objects.get(id=empid)

    if request.method == 'POST':

        empdate = request.POST.get('emp_date')
        in_time = request.POST.get('in_time')
        out_time = request.POST.get('out_time')
        status = "P"
        att = Attendance.objects.filter(employee_id=empid, emp_date=empdate)

        if len(att) == 0:
            a = Attendance(employee=emp, emp_date=empdate, in_time=in_time, out_time=out_time, status=status)
            a.save()
        else:
            day_att = att[0]
            day_att.in_time = in_time
            day_att.out_time = out_time
            day_att.save()

        return redirect('all_emp')
    else:
        form = AttendanceForm()
        cur_time = str(time.strftime('%H')) + ":" + str(time.strftime('%M'))
        context = {
            'form': form,
            'emp_name': emp,
            'siv': cur_time,
            'sov': cur_time,
            'today': date.today().strftime("%Y-%m-%d")
        }

        return render(request, template_name, context=context)


def show_employee_details(request, empid):
    """Displays detailed information about a specific employee, including attendance."""
    emp = Employee.objects.get(id=empid)

    # Attendance details
    att = Attendance.objects.filter(employee_id=empid).order_by('emp_date')
   

    attendance = []
    for ed in att:
        t = {}
        t['date'] = ed.emp_date
        t['in_time'] = ed.in_time
        t['out_time'] = ed.out_time
        t['status'] = ed.status

        attendance.append(t)
    print(attendance)

    return render(request, 'employee_details.html', context={'emp': emp, 'attendance': attendance})
