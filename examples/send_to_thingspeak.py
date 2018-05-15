#!/usr/bin/python

"""
temp.py 
Temperature/Humidity monitor using Raspberry Pi and DHT22.
Data is displayed at https://thingspeak.com/channels/324453/
"""
from __future__ import print_function

import os

import urllib2

import Adafruit_DHT

myAPI = "****"

# connected to GPIO22.
pin = 22


def read_dht_sensor():
    hum = None
    temp = None
    for i in range(3):
        # just take second result
        hum, temp = Adafruit_DHT.read_retry(Adafruit_DHT.DHT22, pin)
        print("{})t={} *C, h={} %".format(str(i), temp, hum))
    return round(hum, 1), round(temp, 1)


# Get CPU temperature using 'vcgencmd measure_temp'
def get_cpu_temp():
    temp = os.popen('vcgencmd measure_temp').readline()
    return temp.replace("temp=", "").replace("'C\n", "")


def main():
    baseURL = 'https://api.thingspeak.com/update?api_key=%s' % myAPI
    try:
        hum, temp1 = read_dht_sensor()
        temp2 = get_cpu_temp()

        print("t1={}\nt2={}\nh={}".format(temp1, temp2, hum))

        f = urllib2.urlopen(baseURL + "&field1=%s&field2=%s&field3=%s" % (hum, temp1, temp2))
        f.close()
    except Exception as e:
        print('Holy Cow, something Broke!!! exiting.' + str(e))


if __name__ == '__main__':
    main()
