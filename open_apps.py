import os
import subprocess
import psutil
import webbrowser

from voice import *




#sites
def open_search(text):
    webbrowser.open('https://yandex.com/')

def open_ege(text):
    webbrowser.open('https://ege.sdamgia.ru/')

def open_sdam(text):
    webbrowser.open('https://sdamgia.ru/')

def open_mesh(text):
    webbrowser.open('https://dnevnik.mos.ru/diary/schedules/schedule')

def open_youtube(text):
    webbrowser.open('https://www.youtube.com/')

def open_translator(text):
    webbrowser.open('https://translate.yandex.ru/')


#apps
def open_discord(text):
    try:
        subprocess.Popen(['D:/My Projects/programming/python/expo v-2/apps/Discord.lnk'], shell=True, close_fds=True)
    except Exception as e:
        speak('не могу найти такую программу. ознакомьтесь с инструкцией.')
        print(f"Произошла ошибка при запуске ярлыка: {e}")

def close_discord(text):
    process_name = 'Discord.exe'
    try:
        for process in psutil.process_iter(['pid', 'name']):
            if process.info['name'] == process_name:
                process.terminate()
                print(f"Процесс {process_name} успешно завершен.")
                return
        print(f"Процесс {process_name} не найден.")
    except psutil.NoSuchProcess:
        print(f"Процесс {process_name} не существует.")



def open_browser(text):
    try:
        subprocess.Popen(['D:/My Projects/programming/python/expo v-2/apps/Yandex.lnk'], shell=True, close_fds=True)
    except Exception as e:
        speak('не могу найти такую программу. ознакомьтесь с инструкцией.')
        print(f"Произошла ошибка при запуске ярлыка: {e}")
#ФИКСИТЬ ЗАКРЫТИЕ
def close_browser(text):
    process_name = 'browser.exe'
    try:
        for process in psutil.process_iter(['pid', 'name']):
            if process.info['name'] == process_name:
                process.terminate()
                print(f"Процесс {process_name} успешно завершен.")
                return
        print(f"Процесс {process_name} не найден.")
    except psutil.NoSuchProcess:
        print(f"Процесс {process_name} не существует.")



def open_valorant(text):
    try:
        subprocess.Popen(['D:/My Projects/programming/python/expo v-2/apps/VALORANT.lnk'], shell=True, close_fds=True)
    except Exception as e:
        speak('не могу найти такую программу. ознакомьтесь с инструкцией.')
        print(f"Произошла ошибка при запуске ярлыка: {e}")

def close_valorant(text):
    process_name = 'VALORANT.exe'
    try:
        for process in psutil.process_iter(['pid', 'name']):
            if process.info['name'] == process_name:
                process.terminate()
                print(f"Процесс {process_name} успешно завершен.")
                return
        print(f"Процесс {process_name} не найден.")
    except psutil.NoSuchProcess:
        print(f"Процесс {process_name} не существует.")



def open_minecraft(text):
    try:
        subprocess.Popen(['D:/My Projects/programming/python/expo v-2/apps/Minecraft.lnk'], shell=True, close_fds=True)
    except Exception as e:
        speak('не могу найти такую программу. ознакомьтесь с инструкцией.')
        print(f"Произошла ошибка при запуске ярлыка: {e}")

def close_minecraft(text):
    process_name = 'TLauncher.exe'
    try:
        for process in psutil.process_iter(['pid', 'name']):
            if process.info['name'] == process_name:
                process.terminate()
                print(f"Процесс {process_name} успешно завершен.")
                return
        print(f"Процесс {process_name} не найден.")
    except psutil.NoSuchProcess:
        print(f"Процесс {process_name} не существует.")



def open_steam(text):
    try:
        subprocess.Popen(['D:/My Projects/programming/python/expo v-2/apps/Steam.lnk'], shell=True, close_fds=True)
    except Exception as e:
        speak('не могу найти такую программу. ознакомьтесь с инструкцией.')
        print(f"Произошла ошибка при запуске ярлыка: {e}")

def close_steam(text):
    process_name = 'steam.exe'
    try:
        for process in psutil.process_iter(['pid', 'name']):
            if process.info['name'] == process_name:
                process.terminate()
                print(f"Процесс {process_name} успешно завершен.")
                return
        print(f"Процесс {process_name} не найден.")
    except psutil.NoSuchProcess:
        print(f"Процесс {process_name} не существует.")



def open_telegram(text):
    try:
        subprocess.Popen(['D:/My Projects/programming/python/expo v-2/apps/Telegram.lnk'], shell=True, close_fds=True)
    except Exception as e:
        speak('не могу найти такую программу. ознакомьтесь с инструкцией.')
        print(f"Произошла ошибка при запуске ярлыка: {e}")

def close_telegram(text):
    process_name = 'Telegram Desktop.exe'
    try:
        for process in psutil.process_iter(['pid', 'name']):
            if process.info['name'] == process_name:
                process.terminate()
                print(f"Процесс {process_name} успешно завершен.")
                return
        print(f"Процесс {process_name} не найден.")
    except psutil.NoSuchProcess:
        print(f"Процесс {process_name} не существует.")



def open_vsc(text):
    try:
        subprocess.Popen(['D:/My Projects/programming/python/expo v-2/apps/VSC.lnk'], shell=True, close_fds=True)
    except Exception as e:
        speak('не могу найти такую программу. ознакомьтесь с инструкцией.')
        print(f"Произошла ошибка при запуске ярлыка: {e}")



# def open_browser(text):
#     try:
#         subprocess.Popen(['D:/My Projects/programming/python/expo v-2/apps/Yandex.lnk'], shell=True, close_fds=True)
#     except Exception as e:
#         speak('не могу найти такую программу. ознакомьтесь с инструкцией.')
#         print(f"Произошла ошибка при запуске ярлыка: {e}")


# def open_browser(text):
#     try:
#         subprocess.Popen(['D:/My Projects/programming/python/expo v-2/apps/Yandex.lnk'], shell=True, close_fds=True)
#     except Exception as e:
#         speak('не могу найти такую программу. ознакомьтесь с инструкцией.')
#         print(f"Произошла ошибка при запуске ярлыка: {e}")


# def open_browser(text):
#     try:
#         subprocess.Popen(['D:/My Projects/programming/python/expo v-2/apps/Yandex.lnk'], shell=True, close_fds=True)
#     except Exception as e:
#         speak('не могу найти такую программу. ознакомьтесь с инструкцией.')
#         print(f"Произошла ошибка при запуске ярлыка: {e}")


# def open_browser(text):
#     try:
#         subprocess.Popen(['D:/My Projects/programming/python/expo v-2/apps/Yandex.lnk'], shell=True, close_fds=True)
#     except Exception as e:
#         speak('не могу найти такую программу. ознакомьтесь с инструкцией.')
#         print(f"Произошла ошибка при запуске ярлыка: {e}")