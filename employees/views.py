from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from employees.models import Employee, Country, City
from employees.serializers import EmployeeSerializer, CitySerializer, CountrySerializer


@api_view(['GET'])
def country_list(request):
    if request.method == 'GET': #Take a list of employees
        country = Country.objects.all()
        serializer = CountrySerializer(country, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def city_list(request):
    if request.method == 'GET': #Take a list of employees
        city = City.objects.all()
        serializer = CitySerializer(city, many=True)
        return Response(serializer.data)

@api_view(['GET']) #We can take details / change empolyee's details / delete employee by id
def country_detail(request, pk):
    try:
        country = Country.objects.get(pk=pk)
    except Country.DoesNotExist:
        return Response(status=status.HTTP_400_NOT_FOUND)

    if request.method == 'GET': #Take details about Country by id
        serializer = CountrySerializer(country)
        return Response(serializer.data)

@api_view(['GET', 'POST'])
def employee_list(request): #We can take a list of employees or add a new one
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET': #Take a list of employees
        employee = Employee.objects.all()
        serializer = EmployeeSerializer(employee, many=True)
        return Response(serializer.data)

    elif request.method == 'POST': #Add a new employee
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE']) #We can take details / change empolyee's details / delete employee by id
def employee_detail(request, pk):
    try:
        employee = Employee.objects.get(pk=pk)
    except Employee.DoesNotExist:
        return Response(status=status.HTTP_400_NOT_FOUND)

    if request.method == 'GET': #Take details about employee by id
        serializer = EmployeeSerializer(employee)
        return Response(serializer.data)

    elif request.method == 'PUT': #Change some fields of specific employee by id
        serializer = EmployeeSerializer(employee, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE': #Delete an employee by id
        employee.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

def index(request):
    return render(request, 'index.html')