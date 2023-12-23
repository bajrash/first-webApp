from django.http import HttpResponse
from django.shortcuts import render



def result (request):
    age = request.Get['usar_age']
    name = request.Get['usar_name']
    massage = f'hi, {name}, your are {age}, years old'
    return render(request, 'index.html',{'age':massage})