from django.shortcuts import render
from app.models import *
# Create your views here.
def display_dept(request):
    DO=Dept.objects.all()
    d={'dept':DO}
    return render(request,'display_dept.html',d)


def display_emp(request):
    EO=Emp.objects.all()
    d={'emp':EO}
    return render(request,'display_emp.html',d)

def insert_dept(request):
    no=int(input('Enter department number: '))
    n=input('Enter department name: ')
    l=input('Enter location: ')

    QLDO=Dept.objects.get_or_create(deptno=no,dname=n,loc=l)[0]
    QLDO.save()

    QLD=Dept.objects.all()
    d={'QLD':QLD}
    return render(request,'display_dept.html',d)


def insert_emp(request):
    en=int(input('Enter Employee no: '))
    n=input('Enter Name: ')
    j=input('Enter job: ')
    h=input('Enter hiredate: ')
    s=int(input('Enter salary: '))
    c=int(input('Enter commision: '))
    dno=int(input('Enter department no: '))
    dn=Dept.objects.get(deptno=dno)

    QLEO=Emp.objects.get_or_create(empno=en,ename=n,job=j,hiredate=h,sal=s,comm=c,deptno=dn)[0]
    QLEO.save()

    QLE=Emp.objects.all()
    d={'QLE':QLE}
    return render(request,'display_emp.html',d)

