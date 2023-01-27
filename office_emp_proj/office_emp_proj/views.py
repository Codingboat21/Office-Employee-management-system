from django.shortcuts import render ,HttpResponse
from emp_app.models import Role,Employee,Department
from datetime import datetime

from django.db.models import Q

def index(request):
    return render(request,'index.html')

def view_emp(request):
    emps=Employee.objects.all()
    context={
        'emps':emps
    }
    print(context)

    return render(request,'view_emp.html',context)

def add_emp(request):

    if request.method=="POST":
        first_name=request.POST.get("first_name")
        last_name=request.POST.get("last_name")
        dept=eval(request.POST.get("dept"))
        role=eval(request.POST.get("role"))
        salary=eval(request.POST.get("salary"))
        bonus=eval(request.POST.get("bonus"))
        phone=eval(request.POST.get("phone"))

        # cur.execute("insert into emp_app_employee (first_name,last_name,salary,bonus,phone,hire_date,dept_id,role_id values('"+first_name+"','"+last_name+"','"+salary+"','"+bonus+"','"+phone+"','"+hire_date+"','"+dept+"','"+role+"');")
        # db.commit()
        print("added")
        # db.close()


        new_ep=Employee(first_name=first_name,last_name=last_name,dept_id=dept,role_id=role,salary=salary,bonus=bonus,phone=phone,hire_date=datetime.now())
        new_ep.save()
        return HttpResponse("<h1>Employee Added Successfully</h1>")

    elif request.method=="GET":
        return render(request,'add_emp.html')

    else:
        return HttpResponse("An error occur")

def remove_emp(request,emp_id=0):
    if emp_id:
        try:
            emp_rem=Employee.objects.get(id=emp_id)
            
            emp_rem.delete()
            return HttpResponse("Employee Removed successfully")
        except:
            return HttpResponse("Error")
    emps=Employee.objects.all()
    context={
        "emp":emps
    }


    return render(request,'remove_emp.html',context)

def fil_emp(request):
    if request.method=="POST":
        name=request.POST.get("name")
        dept=request.POST.get("dept")
        role=request.POST.get("role")

        emps=Employee.objects.all()

        if name:
            emps=emps.filter(Q(first_name__icontains = name) | Q(last_name__icontains=name))

        if dept:
            emps=emps.filter(Q(dept__name__icontains=dept))

        if role:
            emps=emps.filter(Q(role__name__icontains=role))

        context={
            "emps":emps
        }
        return render(request,"view_emp.html",context)
    elif request.method=="GET":
        return render(request,'fil_emp.html')

# Create your views here.
