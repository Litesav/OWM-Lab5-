# coding: utf8 
#�������� ����. ���22. ������������ ������ #5 

import pyowm 
from datetime import datetime 
owm = pyowm.OWM('54da908969546080ba5c49b35dba176f') #�������� ������ � ��, ��������� API ���� 
observation = owm.weather_at_place('Rostov-on-Don, RU') 
weather = observation.get_weather() 
location = observation.get_location() 
translate_city = {'Rostov-na-Donu': '������-��-����', 'Moscow': '������', 
'New York': '���-����', 'London': '�����', 'Toronto': '�������'} 
translate_country = {'RU': '������', 'GB': '��������������', 'CA': '������', 'US': '���������� ����� �������'} 


def temperature(string): #������� ������� ��������� string - ������ ��� � ����� 
f_observation = owm.daily_forecast('Rostov-on-Don, RU') 
f_weather = f_observation.get_weather_at(datetime.now()) 
return str(round(f_weather.get_temperature('celsius')[string])) 


def cloudiness(): #������������ �������� �������� ���������� ������ 
if 0 <= weather.get_clouds() <= 10: 
return '�����' 

if 10 < weather.get_clouds() <= 30: 
return '������� ��������' 

if 30 < weather.get_clouds() <= 60: 
return '��������' 

if 60 < weather.get_clouds() <= 100: 
return '�������' 


def status(x): #������������� �������� ���������� 
return { 
'10d' or '10n': ', �����', 
'09d' or '09n': ', ������', 
'11d' or '11n': ', �����', 
'13d' or '13n': ', ����', 
'50d' or '50n': ', �����' 
}.get(x, '') 


def direction_wind(): #����������� ���������� �������� ��� ���� ����� 
if 337.5 < weather.get_wind()['deg'] <= 22.5: 
return '��������' 
if 157.5 < weather.get_wind()['deg'] <= 202.5: 
return '�����' 
if 67.5 < weather.get_wind()['deg'] <= 112.5: 
return '���������' 
if 247.5 < weather.get_wind()['deg'] <= 292.5: 
return '��������' 
if 22.5 < weather.get_wind()['deg'] <= 67.5: 
return '������-���������' 
if 112.5 < weather.get_wind()['deg'] <= 157.5: 
return '���-���������' 
if 202.5 < weather.get_wind()['deg'] <= 247.5: 
return '���-��������' 
if 292.5 < weather.get_wind()['deg'] <= 337.5: 
return '������-��������' 


#����� ���������� �������� �������� ������ 
print('\n������ � ������ ' + translate_city[location.get_name()] + ' (' + translate_country[location.get_country()] + 
') ' + '�� ������� ' + str(datetime.now().strftime("%H:%M")) + ' ' + cloudiness() + ', \n���������� ���������� ' + 
str(weather.get_clouds()) + ' %, �������� ' + str(round(weather.get_pressure()['press'] * 0.750062)) + 
' �� ��. ��.,\n����������� ' + str(round(weather.get_temperature('celsius')['temp'])) + ' �������� �������' + 
', ��� ' + temperature('day') + ', ����� ' + temperature('night') + ', ����� ' + direction_wind() + ', ' + 
str(round(weather.get_wind()['speed'])) + ' �/c' + status(weather.get_weather_icon_name()) + '.')