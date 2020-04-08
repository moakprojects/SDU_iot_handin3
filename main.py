import pycom
import machine
import time
from network import WLAN
import urequests
from machine import Pin
from machine import ADC
from pysense import Pysense
from LTR329ALS01 import LTR329ALS01
from SI7006A20 import SI7006A20

pycom.heartbeat(False)

wifi_ssid = '#####'
wifi_pass = '#####'

if machine.reset_cause() != machine.SOFT_RESET:

    wlan = WLAN(mode=WLAN.STA)

    wlan.connect(wifi_ssid, auth=(WLAN.WPA2, wifi_pass), timeout=5000)

    while not wlan.isconnected():
        machine.idle()

print('Connected to Wifi\n')
print(wlan.ifconfig())

p_out = Pin('P19', mode=Pin.OUT)
p_out.value(1)
p_out.value(0)
p_out.toggle()
p_out(True)

adc = ADC(id=0)
apin = adc.channel(pin='P16')

py = Pysense()
lt = LTR329ALS01(py)
tp = SI7006A20(py)

def httpRequest():
    timestamp = time.time()
    temp = tp.temperature()
    light = lt.light()
    volt = apin.voltage()
    try:
        res = urequests.get('https://www.egportfolio.info/al.php?time='+str(timestamp)+'&temp='+str(temp)+'&light0='+str(light[0])+'&light1='+str(light[1])+'&volt='+str(volt))
        res.close()
        time.sleep(1)
        httpRequest()
    except Exception as e:
        time.sleep(1)
        httpRequest()

httpRequest()
