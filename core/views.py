from django.shortcuts import render, HttpResponse

# Create your views here.

def hello(requests, nome, idade):
    return HttpResponse('<h1>Hello {} de {} anos<h1>'.format(nome, idade))

def soma(requests, number1, number2):
    resp = number1 + number2
    return HttpResponse('<h1>Soma = {}<h1>'.format(resp))

def sub(requests, number1, number2):
    resp = number1 - number2
    return HttpResponse('<h1>Subtraction = {}<h1>'.format(resp))

def mult(requests, number1, number2):
    resp = number1 * number2
    return HttpResponse('<h1>Multiplication = {}<h1>'.format(resp))

def div(requests, number1, number2):
    resp = number1 / number2
    return HttpResponse('<h1>Division = {}<h1>'.format(resp))