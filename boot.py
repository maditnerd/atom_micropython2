# This file is executed on every boot (including wake-boot from deepsleep)
#import esp
#esp.osdebug(None)
import network
import machine
import utime
import secrets

def connect_wifi():
    wifi = network.WLAN(network.STA_IF)
    wifi.active(True)
    wifi.connect(secrets.ssid, secrets.password)
    while not wifi.isconnected():
        utime.sleep(1)
        print('WiFi connect retry ...')
    print('WiFi IP:', wifi.ifconfig()[0])
    print('WiFi cfg:', wifi.ifconfig())
    return wifi.ifconfig()

connect_wifi()

import http_text

