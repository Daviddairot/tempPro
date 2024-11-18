from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from .models import Temperatures

def updateTemperature(request):
    date = request.GET.get('date')

    temp1 = request.GET.get('temp1')
    humidity1 = request.GET.get('humidity1')

    temp2 = request.GET.get('temp2')
    humidity2 = request.GET.get('humidity2')

    temp3 = request.GET.get('temp3')
    humidity3 = request.GET.get('humidity3')

    temp4 = request.GET.get('temp4')
    humidity4 = request.GET.get('humidity4')

    temp5 = request.GET.get('temp5')
    humidity5 = request.GET.get('humidity5')

    # Try to get the object, or create it if it doesn't exist
    temperature_record, created = Temperatures.objects.get_or_create(date=date)

    # Update or set the values
    if temp1 and humidity1:
        temperature_record.temperature1 = temp1
        temperature_record.humidity1 = humidity1

    if temp2 and humidity2:
        temperature_record.temperature2 = temp2
        temperature_record.humidity2 = humidity2

    if temp3 and humidity3:
        temperature_record.temperature3 = temp3
        temperature_record.humidity3 = humidity3

    if temp4 and humidity4:
        temperature_record.temperature4 = temp4
        temperature_record.humidity4 = humidity4

    if temp5 and humidity5:
        temperature_record.temperature5 = temp5
        temperature_record.humidity5 = humidity5

    temperature_record.save()

    return JsonResponse({'success': True, 'created': created})
