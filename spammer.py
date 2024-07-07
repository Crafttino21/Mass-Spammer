import pyautogui as auto
from time import sleep
from colorama import Fore
import os
import ctypes
import requests

banner = '''
███╗   ███╗ █████╗ ███████╗███████╗    ███████╗██████╗  █████╗ ███╗   ███╗███╗   ███╗███████╗██████╗ 
████╗ ████║██╔══██╗██╔════╝██╔════╝    ██╔════╝██╔══██╗██╔══██╗████╗ ████║████╗ ████║██╔════╝██╔══██╗
██╔████╔██║███████║███████╗███████╗    ███████╗██████╔╝███████║██╔████╔██║██╔████╔██║█████╗  ██████╔╝
██║╚██╔╝██║██╔══██║╚════██║╚════██║    ╚════██║██╔═══╝ ██╔══██║██║╚██╔╝██║██║╚██╔╝██║██╔══╝  ██╔══██╗
██║ ╚═╝ ██║██║  ██║███████║███████║    ███████║██║     ██║  ██║██║ ╚═╝ ██║██║ ╚═╝ ██║███████╗██║  ██║
╚═╝     ╚═╝╚═╝  ╚═╝╚══════╝╚══════╝    ╚══════╝╚═╝     ╚═╝  ╚═╝╚═╝     ╚═╝╚═╝     ╚═╝╚══════╝╚═╝  ╚═╝
            * Mass Spammer by WeepingAngel | GitHub: https://github.com/Crafttino21 *                                                                                        
        Discord: weepingangeliv | For Education Purpose | Suck my Balls lol | Unleshed
'''

menu = '''
Select your Spam Mode:
[1] Discord (Bypassed, raw)
[2] Discord (Bypassed, Network) [WIP]
[3] RAW (WHatsApp, Telegram, etc)

More Soon!
'''
class colors:
    mangenta = Fore.LIGHTMAGENTA_EX
    blau = Fore.LIGHTBLUE_EX
    red = Fore.LIGHTRED_EX
    green = Fore.LIGHTGREEN_EX



class functions:
    # Message Box
    def Mbox(title, text, style):
        return ctypes.windll.user32.MessageBoxW(0, text, title, style)

    # Clears console
    def clearConsole():
        clr = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')
        return clr

class module:  # Modules for Spammer :)
    def discord():
        print("DISCORD SPAMBOT BY WEEPINGANEGL; FOR EDUCATION ONLY!")
        print("GitHub: https://github.com/Crafttino21 | Discord: weepingangeliv")
        print(colors.blau + "DISCORD RAW MODE LOADED!")

        text = input("Type Message: ")
        print("WARNING!: You have 5 seconds to before start!")
        sleep(5)
        print("Spam in Progress, Close or stop Program with STRG+C")

        while True:
            print(colors.blau + "[+] Spam Generated!")
            auto.write(text)
            auto.press('enter')
            sleep(0.08)

    def raw():
        print(colors.green + "RAW MODE (WhatsApp Mode) LOADED!")

        text2 = input("Type Message: ")
        print(colors.red + "[WARNING!] You have 5 Seconds before Start!")
        sleep(5)
        print(colors.green + "Spam in Progress, Close or Stop with STRG+C")

        while True:
            print("[+] Spam Generated!")
            auto.write(text2)
            auto.press('enter')
            sleep(0.01)

    def discord_network():
        print(colors.mangenta + "NETWORK DISCORD BYPASS LOADED!")
        print("Warning this is Work in progress!")
        text3 = input("Enter text to Spam > ")
        at = input("Enter number of Spam > ")
        message_token = input("Enter Message Token > ")
        channel_id = input("Enter channel ID > ")

        payload = {
            'content': text3
        }

        header = {
            'authorization': message_token
        }

        for i in range (1000):
            r = requests.post(f'https://discord.com/api/v9/channels/{channel_id}/messages')
            print(f"{colors.mangenta} [+] Message Send!")




os.system("title Mass Spammer by WeepingAngel")
print(colors.mangenta + banner)
functions.Mbox('Mass Spammer by WeepingAngel',
               'Welcome! You are Using Version: 1.0, Thanks for Download!', 1)
print(menu)
xsf = input(" > ")

if xsf == '1':
    module.discord()

if xsf == '2':
    module.discord_network()

if xsf == '3':
    module.raw()





