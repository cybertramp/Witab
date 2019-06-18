from flask import Flask,render_template
import telegram
import RPi.GPIO as GPIO
import time
import datetime
from datetime import timedelta
import subprocess

from telegram.ext import Updater, MessageHandler, Filters  # import modules
from telegram.ext.dispatcher import run_async

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

pins = [1,7,8,25]

for i in pins:
    GPIO.setup(i, GPIO.OUT)
    GPIO.output(i, GPIO.LOW)

app = Flask(__name__)

title = 'Witab control page'
tele_token = "INPUT YOUR TTELEGRAM TOKEN"

status_switch = ['','','','']
count_switch = [0,0,0,0]
status_menu = ['','','']
count_switch = 0

print("####################")

@run_async
def get_message(update,context) :
    update.message.reply_text("got text")
    update.message.reply_text(update.message.text)


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
    templateData={
        'title' : title,
        'activation1' : status_menu[0],
        'activation2' : status_menu[1],
        'activation3' : status_menu[2],
        'uptime' : uptime[:-7],
        'count_sw' : count_switch,
    }
    return render_template('stat.html', **templateData)

if __name__ == '__main__':
    bot = telegram.Bot(token = tele_token)
    
    try:
        chat_id = bot.getUpdates()[-1].message.chat.id
    except:
        chat_id = 533544252

    updater = Updater(tele_token)
    
    message_handler = MessageHandler(Filters.text, get_message)
    updater.dispatcher.add_handler(message_handler)

    #updater.start_polling(poll_interval=5, timeout=10)
    updater.start_polling(timeout=3, clean=True)
    updater.idle()

    bot.send_message(chat_id, text="Witab 서버 시작")
    app.run(debug=True, port=80, host='0.0.0.0')
    GPIO.cleanup()
    print("GPIO cleaned!")

