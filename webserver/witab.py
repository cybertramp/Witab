# FLASK
from flask import Flask,render_template

# GPIO
import RPi.GPIO as GPIO

# SSD1306 OLED
import Adafruit_GPIO.SPI as SPI
import Adafruit_SSD1306

# PIL
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

import time
import datetime
from datetime import timedelta
import subprocess

import telepot
from telepot.loop import MessageLoop

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

pins = [1,7,8,25]

for i in pins:
    GPIO.setup(i, GPIO.OUT)
    GPIO.output(i, GPIO.LOW)

RST = None
DC = 23
SPI_PORT = 0
SPI_DEVICE = 0

disp = Adafruit_SSD1306.SSD1306_128_32(rst=RST)
disp.begin()
disp.clear()
disp.display()

width = disp.width
height = disp.height

image = Image.new('1', (width, height))
draw = ImageDraw.Draw(image)

#font = ImageFont.load_default()
font_text = ImageFont.truetype('/usr/share/fonts/truetype/nanum/NanumGothic.ttf',12)
font_big = ImageFont.truetype('/usr/share/fonts/truetype/nanum/NanumGothic.ttf',18)
font_small = ImageFont.truetype('/usr/share/fonts/truetype/nanum/NanumGothic.ttf',10)
app = Flask(__name__)

title = 'Witab control page'
tele_token = "INPUT YOUR TTELEGRAM TOKEN"

status_switch = ['','','','']
count_switch = [0,0,0,0]
status_menu = ['','','']
count_switch = 0

print("####################")

def action(msg):
    global count_switch
    chat_id = msg['chat']['id']
    command = msg['text']
    print ('Received: ',command)
    if 'sw1' in command:
        if status_switch[0] == '':
            GPIO.output(pins[0],GPIO.HIGH)
            print('switch1: ON')
            status_switch[0] = "checked"
            message = "SWITCH1 ON"
        else:
            GPIO.output(pins[0],GPIO.LOW)
            print('switch1: OFF')
            status_switch[0] = ""
            message = "SWITCH1 OFF"
        count_switch = count_switch+1
        telegram_bot.sendMessage (chat_id, message)
    elif 'sw2' in command:
        message = "SWITCH2 ON"
        if status_switch[1] == '':
            GPIO.output(pins[1],GPIO.HIGH)
            print('switch2: ON')
            status_switch[1] = "checked"
            message = "SWITCH2 ON"
        else:
            GPIO.output(pins[1],GPIO.LOW)
            print('switch2: OFF')
            status_switch[1] = ""
            message = "SWITCH2 OFF"
        count_switch = count_switch+1
        telegram_bot.sendMessage (chat_id, message)
    elif 'sw3' in command:
        message = "SWITCH3 ON"
        if status_switch[2] == '':
            GPIO.output(pins[2],GPIO.HIGH)
            print('switch3: ON')
            status_switch[2] = "checked"
            message = "SWITCH3 ON"
        else:
            GPIO.output(pins[2],GPIO.LOW)
            print('switch3: OFF')
            status_switch[2] = ""
            message = "SWITCH3 OFF"
        count_switch = count_switch+1
        telegram_bot.sendMessage (chat_id, message)
    elif 'sw4' in command:
        message = "SWITCH4 ON"
        if status_switch[3] == '':
            GPIO.output(pins[3],GPIO.HIGH)
            print('switch4: ON')
            status_switch[3] = "checked"
            message = "SWITCH4 ON"
        else:
            GPIO.output(pins[3],GPIO.LOW)
            print('switch4: OFF')
            status_switch[3] = ""
            message = "SWITCH4 OFF"
        count_switch = count_switch+1
        telegram_bot.sendMessage (chat_id, message)

@app.route('/')
def index():
    status_menu[0] = 'active'
    status_menu[1] = ''
    status_menu[2] = ''
    templateData={
        'title' : title,
        'activation1' : status_menu[0],
        'activation2' : status_menu[1],
        'activation3' : status_menu[2],
    }
    return render_template('index.html', **templateData)

@app.route('/sw1')
def switch1():
    if status_switch[0] == '':
        GPIO.output(pins[0],GPIO.HIGH)
        print('switch1: ON')
        status_switch[0] = "checked"
    else:
        GPIO.output(pins[0],GPIO.LOW)
        print('switch1: OFF')
        status_switch[0] = ""
        global count_switch
        count_switch = count_switch+1
    templateData={
        'title' : title,
        'activation1' : status_menu[0],
        'activation2' : status_menu[1],
        'activation3' : status_menu[2],
        'checked1': status_switch[0],
        'checked2': status_switch[1],
        'checked3': status_switch[2],
        'checked4': status_switch[3],
    }
    print(status_switch)
    return render_template('index.html', **templateData)
@app.route('/sw2')
def switch2():
    if status_switch[1] == '':
        GPIO.output(pins[1],GPIO.HIGH)
        print('switch2: ON')
        status_switch[1] = "checked"
    else:
        GPIO.output(pins[1],GPIO.LOW)
        print('switch2: OFF')
        status_switch[1] = ""
        global count_switch
        count_switch = count_switch+1
    templateData={
        'title' : title,
        'activation1' : status_menu[0],
        'activation2' : status_menu[1],
        'activation3' : status_menu[2],
        'checked1': status_switch[0],
        'checked2': status_switch[1],
        'checked3': status_switch[2],
        'checked4': status_switch[3],
    }
    print(status_switch)
    return render_template('index.html', **templateData)

@app.route('/sw3')
def switch3():
    if status_switch[2] == '':
        GPIO.output(pins[2],GPIO.HIGH)
        print('switch3: ON')
        status_switch[2] = "checked"
    else:
        GPIO.output(pins[2],GPIO.LOW)
        print('switch3: OFF')
        status_switch[2] = ""
        global count_switch
        count_switch = count_switch+1
    templateData={
        'title' : title,
        'activation1' : status_menu[0],
        'activation2' : status_menu[1],
        'activation3' : status_menu[2],
        'checked1': status_switch[0],
        'checked2': status_switch[1],
        'checked3': status_switch[2],
        'checked4': status_switch[3],
    }
    print(status_switch)
    return render_template('index.html', **templateData)

@app.route('/sw4')
def switch4():
    if status_switch[3] == '':
        GPIO.output(pins[3],GPIO.HIGH)
        print('switch4: ON')
        status_switch[3] = "checked"
    else:
        GPIO.output(pins[3],GPIO.LOW)
        print('switch4: OFF')
        status_switch[3] = ""
        global count_switch
        count_switch = count_switch+1
    templateData={
        'title' : title,
        'activation1' : status_menu[0],
        'activation2' : status_menu[1],
        'activation3' : status_menu[2],
        'checked1': status_switch[0],
        'checked2': status_switch[1],
        'checked3': status_switch[2],
        'checked4': status_switch[3],
    }
    print(status_switch)
    return render_template('index.html', **templateData)

@app.route('/time')
def control_time():
    status_menu[0] = ''
    status_menu[1] = 'active'
    status_menu[2] = ''

    now = datetime.datetime.now()
    now = str(now)
    now = now[:-7]
    templateData={
        'title' : title,
        'activation1' : status_menu[0],
        'activation2' : status_menu[1],
        'activation3' : status_menu[2],
        'now' : now,
    }
    return render_template('time.html', **templateData)

@app.route('/stat')
def info():
    status_menu[0] = ''
    status_menu[1] = ''
    status_menu[2] = 'active'

    with open('/proc/uptime', 'r') as f:
        usec = float(f.readline().split()[0])
        uptime = str(timedelta(seconds = usec))
    temp = subprocess.check_output('vcgencmd measure_temp',shell=True)
    temp=temp.decode('utf-8')
    temp = temp[5:-1]
    templateData={
        'title' : title,
        'activation1' : status_menu[0],
        'activation2' : status_menu[1],
        'activation3' : status_menu[2],
        'uptime' : uptime[:-7],
        'count_sw' : count_switch,
        'temp' : temp,
    }
    return render_template('stat.html', **templateData)

if __name__ == '__main__':
    draw.text((0,0),"Witab 0.1",font=font_text,fill=255)
    draw.text((0,15),"부팅중..",font=font_text,fill=255)
    disp.image(image)
    disp.display()
    
    time.sleep(1)

    telegram_bot = telepot.Bot(tele_token)
    print (telegram_bot.getMe())
    MessageLoop(telegram_bot, action).run_as_thread()
    
    draw.rectangle((0,13,width,height), outline=0, fill=0)
    draw.text((0,15),"텔레그램 OK",font=font_text,fill=255)
    disp.image(image)
    disp.display()

    time.sleep(1)
    ips=subprocess.check_output('hostname --all-ip-addresses | tr " " "\n"',shell=True)
    ips = ips.decode('utf-8')
    ips = str(ips[:-1])
    print(ips, width,height)
    draw.rectangle((0,0,width,height), outline=0, fill=0)
    draw.text((110,10),"IP" ,font=font_big,fill=255)
    draw.text((0,8),ips ,font=font_small,fill=255)
    disp.image(image)
    disp.display()

    app.run(debug=False, port=80, host='0.0.0.0',use_reloader=False)

    GPIO.cleanup()
    print("GPIO cleaned!")
    disp.clear()
    disp.display()

