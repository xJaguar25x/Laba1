# -*- coding: utf-8 -*- #коментарий
import pyowm #подключаем библиотеку Pyown
import time

print ("OpenWeatherMapppppp") # выводим на экран "OpenWeatherMapppppp"
owm = pyowm.OWM("0d904a7dd5e39203f16585503df7505f") # инициализируем библиотеку ключем
observation = owm.weather_at_place("Rostov-on-Don,ru") # получаем данные из Ростова на дону
weather = observation.get_weather() # Получаем погодные данные
location = observation.get_location() # Получаем данные местоположения
translate = {"Rostov-na-Donu": "Ростов-на-Дону", "Moscow":"Москва"} # создаем словарь для перевода текста

print(owm)

print ("Страна: " + location.get_country())
print ("Город: " + location.get_name())
print ("Долгота: " + str(location.get_lon()))
print ("Широта: " +str(location.get_lat()))
print ("Облачность: " + str(weather.get_clouds()))
print ("Статус: " + str(weather.get_detailed_status()))
print ("Давление: " + str(weather.get_pressure()))
print ("Дождь: " + str(weather.get_rain()))
print ("Снег: " + str(weather.get_snow()))
print ("Время: " + str(observation.get_reception_time('iso')))
print ("Статус: " + str(weather.get_status()))
print ("Восход: " + str(weather.get_sunrise_time("iso")))
print ("Закат: " + str(weather.get_sunset_time("iso")))
print ("Температура: " + str(weather.get_temperature("celsius")))
print ("Видимость: " + str(weather.get_visibility_distance()))
#print ("Изображение: " + weather.get_weather_icon_name())
print ("Ветер: " + str(weather.get_wind()))

# Создадим функцию которая определяет статус
def what_status():
    if ('Rain') == str(weather.get_status()):
        return 'дождь'
    if ('Snow') == str(weather.get_status()):
        return 'снег'
    if ('Snow') == str(weather.get_status()):
        return 'туман'

# Создадим функцию которая определяет облачность
def what_cloudness():
    if 0 <= weather.get_clouds() <= 10:
        return 'ясная'
    if 10 <= weather.get_clouds() <= 30:
        return 'немного облачная'
    if 30 <= weather.get_clouds() <= 70:
        return 'пасмурная'
    if 70 <= weather.get_clouds() <= 100:
        return 'мрачная'

def convert_pressure():
    mbar = float(weather.get_pressure()['press']) # преобразование типа к вещественному, без этого нет возможности производить арифметические действия
    mmrtst = 0.75 * mbar
    return mmrtst


def what_time():
    a=time.strftime("%a, %d %b %Y %H:%M:%S +0000", time.localtime(int(observation.get_reception_time('unix'))))
    return  str(a)[17] + str(a)[18] + str(a)[19] + str(a)[20] + str(a)[21]

# Выводим на экран данные в дружелюбном формате
print ('Погода в городе ' + translate[location.get_name()] + ' на сегодня в ' + what_time() + ' ' + what_cloudness()
       + ', облачность составляет ' + str(weather.get_clouds()) + '%, давление ' + str(convert_pressure())
       + ' мм рт.ст., температура ' + str(weather.get_temperature('celsius')['temp']) + ' градусов цельсия, '
       + 'скорость ветра ' + str(weather.get_wind()['speed']) + ' м/с, ' + str(what_status()))

"""
print ('Погода в городе ' + translate[location.get_name()] + ' на сегодня в ' + what_time() + ' '
       + WhatIsCloudness() + ', облачность составляет ' + str(weather.get_clouds()) + ', давление ' \
      + str(convert_pressure()) + ' мм рт.ст., температура ' + str(weather.get_temperature('celsius')['temp']) \
      + ' градусов цельсия ' + 'скорость ветра ' + str(weather.get_wind()['speed']) + ' м/с.')
"""
