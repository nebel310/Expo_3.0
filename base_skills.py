import os, webbrowser, sys, requests, subprocess, psutil, pyautogui
import config, words
from num2words import num2words
from voice import *
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
from ru_word2number import w2n




def full_weather(text):
    city = config.CITY
    open_weather_token=config.open_weather_token
    #city = data["name"] <-- если не лень то это надо пофиксить
    code_to_status = {
        "Clear" : 'ясная',
        "Clouds" : 'облачная',
        "Rain" : 'дождь',
        "Drizzle" : 'ливень',
        "Thunderstorm" : 'гроза',
        "Snow" : 'снег',
        "Mist" : 'туманно'
    }

    try:
        r = requests.get(
            f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={open_weather_token}&units=metric"
        )

        data = r.json()

        cur_weather = data["main"]["temp"]
        pressure = data["main"]["pressure"]
        feels_like = data["main"]["feels_like"]
        wind = data["wind"]["speed"]
        

        weather_status = data["weather"][0]["main"]

        if weather_status in code_to_status:
            ws = code_to_status[weather_status]
        else:
            ws = "я не могу понять погоду. посмотрите в окно."
        
        print('cheked: weather')
        to_say = f"В москве сейчас:, {num2words(int(cur_weather), lang='ru')} градусов по ц+е+льсию, но ощущается как {num2words(int(feels_like), lang='ru')}."

        if ws == code_to_status["Clouds"] or ws == code_to_status["Clear"]:
            to_say += f' Погода {ws}.'
        elif code_to_status["Rain"] or code_to_status["Drizzle"] or code_to_status["Thunderstorm"]:
            to_say += f' На улице {ws}.'

        to_say += f" Скорость ве+тра {num2words(int(wind), lang='ru')} метров в секунду. Давление {num2words(int(pressure), lang='ru')} паскаль."
        speak(to_say)


    except Exception as ex:
        print(ex)
        print('Ошибка в погоде')


def gradus_weather(text):
    city = config.CITY
    open_weather_token=config.open_weather_token
    code_to_status = {
        "Clear" : 'ясная',
        "Clouds" : 'облачная',
        "Rain" : 'дождь',
        "Drizzle" : 'ливень',
        "Thunderstorm" : 'гроза',
        "Snow" : 'снег',
        "Mist" : 'туманно'
    }

    try:
        r = requests.get(
            f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={open_weather_token}&units=metric"
        )

        data = r.json()

        cur_weather = data["main"]["temp"]
        feels_like = data["main"]["feels_like"]
        

        weather_status = data["weather"][0]["main"]

        if weather_status in code_to_status:
            ws = code_to_status[weather_status]
        else:
            ws = "я не могу понять погоду. посмотрите в окно."
        
        print('cheked: weather')
        to_say = f"В москве сейчас:, {num2words(int(cur_weather), lang='ru')} градусов по ц+е+льсию, но ощущается как {num2words(int(feels_like), lang='ru')}."

        if ws == code_to_status["Clouds"] or ws == code_to_status["Clear"]:
            to_say += f' Погода {ws}.'
        elif code_to_status["Rain"] or code_to_status["Drizzle"] or code_to_status["Thunderstorm"]:
            to_say += f' На улице {ws}.'

        speak(to_say)


    except Exception as ex:
        print(ex)
        print('Ошибка в погоде')


def web_search(text):
    #Wolfram Alpha

    ban_words = ['экспо', 'найди', 'винтернете', 'загугли', 'загугле', 'гугле']

    words = text.split()
    c_words = [word for word in words if word.lower() not in ban_words]
    text = ' '.join(c_words)
    text = text.replace('в интернете', '', 1)

    url = f'https://yandex.ru/search/?text={text}'
    webbrowser.open_new_tab(url)


def calc(text):
    speak('команда в разработке.')


def convert(text):
    speak('команда в разработке.')


def translate(text):
    speak('команда в разработке.')


def crypt(text):
    ban_words = ['текст', 'сообщение', 'строка', 'строку', 'зашифруй', 'расшифруй', 'слово']

    if 'зашифруй' in text.split():
        b = 'З'
    elif 'расшифруй' in text.split():
        b = 'Р'
    else:
        speak('Упс... Кажется я в тупике. Попробуйте вызвать команду заново.')
        return 0

    a = text

    for trig in words.TRIGGERS:
        if trig in a:
            a = a.replace(trig, '', 1)
    
    for ban in ban_words:
        if ban in a:
            a = a.replace(ban, '', 1)


    def Z(a):
        s = ''
        for i in a:
            if i in alfabet:
                s += alfabet[i]
            else:
                s += i
        print('Полученнный текст:',s)

    def P(a):
        if ('предприм' in a) or ('инж' in a) or ('юр' in a) or ('лек' in a) or ('медиа' in a) or ('гж' in a) or ('академ' in a) or ('ит' in a) or ('акиб' in a) or ('АКАДЕМ' in a) or ('ИНЖ' in a) or ('ЮР' in a) or ('ЛЕК' in a) or ('МЕДИА' in a) or ('ГЖ' in a) or ('АКАДЕМ' in a) or ('ИТ' in a) or ('АКИБ' in a):
            while ('предприм' in a) or ('инж' in a) or ('юр' in a) or ('лек' in a) or ('медиа' in a) or ('гж' in a) or ('академ' in a) or ('ит' in a) or ('акиб' in a) or ('АКАДЕМ' in a) or ('ИНЖ' in a) or ('ЮР' in a) or ('ЛЕК' in a) or ('МЕДИА' in a) or ('ГЖ' in a) or ('АКАДЕМ' in a) or ('ИТ' in a) or ('АКИБ' in a):
                if ('предприм' in a):
                    a = a.replace('предприм', 'a', 1)
                if ('инж' in a):
                    a = a.replace('инж', 'б', 1)
                if ('юр' in a):
                    a = a.replace('юр', 'в', 1)
                if ('лек' in a):
                    a = a.replace('лек', 'г', 1)
                if ('медиа' in a):
                    a = a.replace('медиа', 'д', 1)
                if ('гж' in a):
                    a = a.replace('гж', 'к', 1)
                if ('академ' in a):
                    a = a.replace('академ', 'е', 1)
                if ('ит' in a):
                    a = a.replace('ит', 'я', 1)
                if ('акиб' in a):
                    a = a.replace('акиб', 'ж', 1)
                if ('ПРЕДПРИМ' in a):
                    a = a.replace('ПРЕДПРИМ', 'А', 1)
                if ('ИНЖ' in a):
                    a = a.replace('ИНЖ', 'Б', 1)
                if ('ЮР' in a):
                    a = a.replace('ЮР', 'В', 1)
                if ('ЛЕК' in a):
                    a = a.replace('ЛЕК', 'Г', 1)
                if ('МЕДИА' in a):
                    a = a.replace('МЕДИА', 'Д', 1)
                if ('ГЖ' in a):
                    a = a.replace('ГЖ', 'К', 1)
                if ('АКАДЕМ' in a):
                    a = a.replace('АКАДЕМ', 'Е', 1)
                if ('ИТ' in a):
                    a = a.replace('ИТ', 'Я', 1)
                if ('АКИБ' in a):
                    a = a.replace('АКИБ', 'Ж', 1)
            print('Полученнный текст:',a)


    alfabet = {
        'а': 'предприм',
        'б': 'инж', 
        'в': 'юр',
        'г': 'лек',
        'д': 'медиа',
        'к': 'гж',
        'е': 'академ', 
        'я': 'ит',
        'ж': 'акиб',
        'А': 'ПРЕДПРИМ',
        'Б': 'ИНЖ', 
        'В': 'ЮР',
        'Г': 'ЛЕК',
        'Д': 'МЕДИА',
        'К': 'ГЖ',
        'Е': 'АКАДЕМ', 
        'Я': 'ИТ',
        'Ж': 'АКИБ',
    }

    if b == 'З':
        Z(a)
        speak('Сообщение зашифровано. Отправил результат в консоль.')
    elif b == 'Р':
        P(a)
        speak('Сообщение расшифровано. Отправил результат в консоль.')


def de_desktop(text):
    pyautogui.hotkey('winleft', 'd')
    time.sleep(1)

def de_volume(text):
    def set_volume(device, volume_level):
        device.SetMasterVolumeLevelScalar(volume_level, None)

    def get_volume(device):
        return device.GetMasterVolumeLevelScalar()

    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(
        IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume = cast(interface, POINTER(IAudioEndpointVolume))

    current_volume = get_volume(volume)
    vol_trans = {
        'ноль' : 0.0,
        'один' : 0.1,
        'два' : 0.2,
        'три' : 0.3,
        'четыре' : 0.4,
        'пять' : 0.5,
        'шесть' : 0.6,
        'семь' : 0.7,
        'восемь' : 0.8,
        'девять' : 0.9,
        'десять' : 1.0,
    }

    count_sovpad = 0
    for s_num, i_num in vol_trans.items():
        if s_num in text.split():
            count_sovpad += 1
            check_var = i_num
    if count_sovpad == 1:
        new_volume = check_var
    elif count_sovpad < 1:
        speak('Я могу выставлять гр+омкость только от одного до десяти.')
        new_volume = current_volume
    else:
        speak('Для изменения гр+омкости на устройстве скажите, экспо, поставь громкость на два.')
        new_volume = current_volume


    # Установка громкости (от 0.0 до 1.0)
    set_volume(volume, new_volume)

    # Получение текущей громкости
    current_volume = get_volume(volume)
    print(f"Текущая громкость: {current_volume}")

def de_louder(text):
    def set_volume(device, volume_level):
        device.SetMasterVolumeLevelScalar(volume_level, None)

    def get_volume(device):
        return device.GetMasterVolumeLevelScalar()
    
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(
        IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume = cast(interface, POINTER(IAudioEndpointVolume))

    current_volume = get_volume(volume)

    if current_volume < 1.0:
        new_volume = current_volume + 0.1
    else:
        speak('Достигнут лимит громкости.')
        new_volume = current_volume

    # Установка громкости (от 0.0 до 1.0)
    set_volume(volume, new_volume)

    # Получение текущей громкости
    current_volume = get_volume(volume)
    print(f"Текущая громкость: {current_volume}")

def de_quieter(text):
    def set_volume(device, volume_level):
        device.SetMasterVolumeLevelScalar(volume_level, None)

    def get_volume(device):
        return device.GetMasterVolumeLevelScalar()
    
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(
        IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume = cast(interface, POINTER(IAudioEndpointVolume))

    current_volume = get_volume(volume)

    if current_volume >= 0.1:
        new_volume = current_volume - 0.1
    elif 0.0 < current_volume < 0.1:
        new_volume = 0
    else:
        print('Достигнут лимит громкости.')
        new_volume = current_volume

    # Установка громкости (от 0.0 до 1.0)
    set_volume(volume, new_volume)

    # Получение текущей громкости
    current_volume = get_volume(volume)
    print(f"Текущая громкость: {current_volume}")




def passive(text):
    pass