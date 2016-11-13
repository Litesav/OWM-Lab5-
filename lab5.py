# coding: utf8
#Лазченко Влад. ВИС22. Лабораторная работа #5
 
import pyowm
from datetime import datetime
owm = pyowm.OWM('54da908969546080ba5c49b35dba176f')  #получаем доступ к бд, используя API ключ
observation = owm.weather_at_place('Rostov-on-Don, RU')
weather = observation.get_weather()
location = observation.get_location()
translate_city = {'Rostov-na-Donu': 'Ростов-на-Дону', 'Moscow': 'Москва',
                  'New York': 'Нью-Йорк', 'London': 'Лодон', 'Toronto': 'Торонто'}
translate_country = {'RU': 'Россия', 'GB': 'Великобритания', 'CA': 'Канада', 'US': 'Соединённые Штаты Америки'}
 
 
def temperature(string): #функция выводит результат string - погода днём и ночью
    f_observation = owm.daily_forecast('Rostov-on-Don, RU')
    f_weather = f_observation.get_weather_at(datetime.now())
    return str(round(f_weather.get_temperature('celsius')[string]))
 
 
def cloudiness(): #соответствие числовых значений содержанию вывода
    if 0 <= weather.get_clouds() <= 10:
        return 'север'
 
    if 10 < weather.get_clouds() <= 30:
        return 'немного облачная'
 
    if 30 < weather.get_clouds() <= 60:
        return 'облачная'
 
    if 60 < weather.get_clouds() <= 100:
        return 'мрачная'
 
 
def status(x):   #интерпретация значений переменных
    return {
        '10d' or '10n': ', дождь',
        '09d' or '09n': ', ливень',
        '11d' or '11n': ', гроза',
        '13d' or '13n': ', снег',
        '50d' or '50n': ', туман'
    }.get(x, '')
 
 
def direction_wind(): #Определение интервалов значений для типа ветра
    if 337.5 < weather.get_wind()['deg'] <= 22.5:
        return 'северный'
    if 157.5 < weather.get_wind()['deg'] <= 202.5:
        return 'южный'
    if 67.5 < weather.get_wind()['deg'] <= 112.5:
        return 'восточный'
    if 247.5 < weather.get_wind()['deg'] <= 292.5:
        return 'западный'
    if 22.5 < weather.get_wind()['deg'] <= 67.5:
        return 'северо-восточный'
    if 112.5 < weather.get_wind()['deg'] <= 157.5:
        return 'юго-восточный'
    if 202.5 < weather.get_wind()['deg'] <= 247.5:
        return 'юго-западный'
    if 292.5 < weather.get_wind()['deg'] <= 337.5:
        return 'северо-западный'
 
 
#Вывод текстового варианта описания погоды
    print('\nПогода в городе ' + translate_city[location.get_name()] + ' (' + translate_country[location.get_country()] +
      ') ' + 'на сегодня ' + str(datetime.now().strftime("%H:%M")) + ' ' + cloudiness() + ', \nоблачность составляет ' +
      str(weather.get_clouds()) + ' %, давление ' + str(round(weather.get_pressure()['press'] * 0.750062)) +
      ' мм рт. ст.,\nтемпература ' + str(round(weather.get_temperature('celsius')['temp'])) + ' градусов Цельция' +
      ', днём ' + temperature('day') + ', ночью ' + temperature('night') + ', ветер ' + direction_wind() + ', ' +
      str(round(weather.get_wind()['speed'])) + ' м/c' + status(weather.get_weather_icon_name()) + '.')
