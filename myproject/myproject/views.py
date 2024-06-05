from django.http import HttpResponse
from django.shortcuts import render
from datetime import date
import requests

def homePage(request):
    data={
        'title':'Home Page',
        'bdata':'My name is Saugat Kafle',
        'nlist':['Saugat','Bhumika'],
        'name_details':[
            {'name':'pradeep','phone':9876543210},
            {'name':'Astika','phone':9877662435}
        ]

    }
    return render(request,"index.html",data)

def aboutUs(request):
    return HttpResponse("Hello Saugat")

def nameDetails(request,nameid):
    return HttpResponse(nameid)

def calculator(request):
    result = None
    if request.method == 'POST':
        num1 = float(request.POST.get('num1'))
        num2 = float(request.POST.get('num2'))
        operator = request.POST.get('operator')

        if operator == '+':
            result = num1 + num2
        elif operator == '-':
            result = num1 - num2
        elif operator == '*':
            result = num1 * num2
        elif operator == '/':
            if num2 != 0:
                result = num1 / num2
            else:
                result = "Cannot divide by zero"

    return render(request, 'calculator.html', {'result': result})


def distance_converter(request):
    result = None
    if request.method == 'POST':
        distance = float(request.POST.get('distance'))
        from_unit = request.POST.get('from_unit')
        to_unit = request.POST.get('to_unit')

        # Distance conversion factors
        factors = {
            'km': 1000,
            'm': 1,
            'cm': 0.01,
            'mm': 0.001,
            'mi': 1609.34,
            'yd': 0.9144,
            'ft': 0.3048,
            'in': 0.0254
        }

        # Convert to meters
        meters = distance * factors[from_unit]

        # Convert from meters to target unit
        result = meters / factors[to_unit]

    return render(request, 'distance_converter.html', {'result': result})

def currency_converter(request):
    result = None
    if request.method == 'POST':
        amount = float(request.POST.get('amount'))
        from_currency = request.POST.get('from_currency')
        to_currency = request.POST.get('to_currency')

        # Use an API to fetch the latest exchange rates
        api_url = f'https://api.exchangeratesapi.io/latest?base={from_currency}'
        response = requests.get(api_url)
        print(response.text)  # Add this line to check the API response
        exchange_rates = response.json()['rates']

        # Convert the currency
        if to_currency in exchange_rates:
            result = amount * exchange_rates[to_currency]
        else:
            result = "Invalid currency code"

    return render(request, 'currency_converter.html', {'result': result})

def temperature_converter(request):
    result = None
    if request.method == 'POST':
        temperature = float(request.POST.get('temperature'))
        from_unit = request.POST.get('from_unit')
        to_unit = request.POST.get('to_unit')

        # Temperature conversion functions
        def celsius_to_fahrenheit(temp):
            return (temp * 9/5) + 32

        def celsius_to_kelvin(temp):
            return temp + 273.15

        def fahrenheit_to_celsius(temp):
            return (temp - 32) * 5/9

        def fahrenheit_to_kelvin(temp):
            return (temp - 32) * 5/9 + 273.15

        def kelvin_to_celsius(temp):
            return temp - 273.15

        def kelvin_to_fahrenheit(temp):
            return (temp - 273.15) * 9/5 + 32

        # Perform conversion
        if from_unit == 'celsius':
            if to_unit == 'fahrenheit':
                result = celsius_to_fahrenheit(temperature)
            elif to_unit == 'kelvin':
                result = celsius_to_kelvin(temperature)
        elif from_unit == 'fahrenheit':
            if to_unit == 'celsius':
                result = fahrenheit_to_celsius(temperature)
            elif to_unit == 'kelvin':
                result = fahrenheit_to_kelvin(temperature)
        elif from_unit == 'kelvin':
            if to_unit == 'celsius':
                result = kelvin_to_celsius(temperature)
            elif to_unit == 'fahrenheit':
                result = kelvin_to_fahrenheit(temperature)

    return render(request, 'temperature_converter.html', {'result': result})

def weight_converter(request):
    result = None
    if request.method == 'POST':
        weight = float(request.POST.get('weight'))
        from_unit = request.POST.get('from_unit')
        to_unit = request.POST.get('to_unit')

        # Weight conversion factors
        factors = {
            'kg': 1,
            'g': 0.001,
            'mg': 0.000001,
            'lb': 0.453592,
            'oz': 0.0283495
        }

        # Convert to kilograms
        kilograms = weight * factors[from_unit]

        # Convert from kilograms to target unit
        result = kilograms / factors[to_unit]

    return render(request, 'weight_converter.html', {'result': result})

def age_calculator(request):
    age = None
    if request.method == 'POST':
        birth_date = request.POST.get('birth_date')
        birth_date = date.fromisoformat(birth_date)
        today = date.today()

        # Calculate age
        age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))

    return render(request, 'age_calculator.html', {'age': age})