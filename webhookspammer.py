# File: webhookspammer.pyc (Python 3.9)

import requests
from discord import Webhook, RequestsWebhookAdapter
import colorama
from colorama import Fore
import threading
colorama.init()

def WebHook():
    url = input('[>] Webhook URL: ')
    message = input('[>] Message: ')
    threading.Thread(WebHook, **('target',)).start()
    webhook = Webhook.from_url(f'''{url}''', RequestsWebhookAdapter(), **('adapter',))
    webhook.send(f'''{message}''')
    print(f'''{Fore.GREEN}[>] Sent {message}''')
    continue


def Info():
    message = input('')

print(f'''\n                                       {Fore.LIGHTMAGENTA_EX}/$$$$$$   /$$$$$$  /$$   /$$  /$$$$$$\n                                      /$$__  $$ /$$__  $$| $$$ | $$ /$$__  $$\n                                     | $$  \\__/| $$  \\ $$| $$$$| $$| $$  \\__/\n                                     | $$ /$$$$| $$$$$$$$| $$ $$ $$| $$ /$$$$\n                                     | $$|_  $$| $$__  $$| $$  $$$$| $$|_  $$\n                                     | $$  \\ $$| $$  | $$| $$\\  $$$| $$  \\ $$\n                                     |  $$$$$$/| $$  | $$| $$ \\  $$|  $$$$$$/\n                                      {Fore.LIGHTMAGENTA_EX}\\______/ |__/  |__/|__/  \\__/ \\______/\n\n                                                [1] {Fore.WHITE}WebHook Spammer{Fore.RESET}\n                                                {Fore.LIGHTMAGENTA_EX}[2]{Fore.RESET} {Fore.WHITE}Info{Fore.RESET}\n                                                                ''')
allah = input('[>] Select: ')
if allah == '1':
    WebHook()
    if allah == '2':
        print(f'''{Fore.LIGHTMAGENTA_EX}[>]{Fore.RESET} Thanks for Using GANG Nuker / Multi Tool! Make sure to join my discord server @discord.gg/raided n follow my github!\n\nPress Enter...''')
        Info()
        return None
