""" 
temp.py 
Temperature/Humidity monitor using Raspberry Pi and DHT22.
Data is displayed at https://thingspeak.com/channels/324453/
"""
from __future__ import print_function

import urllib2

import Adafruit_DHT

myAPI = "****"

# connected to GPIO22.
pin = 22


def read_dht_sensor():
    hum = None
    temp = None
    for i in range(2):
        # just take second result
        hum, temp = Adafruit_DHT.read_retry(Adafruit_DHT.DHT22, pin)
    return round(hum, 1), round(temp, 1)


def main():
    baseURL = 'https://api.thingspeak.com/update?api_key=%s' % myAPI
    try:
        hum, temp1 = read_dht_sensor()

        print("t={}\nh={}".format(temp1, hum))

        f = urllib2.urlopen(baseURL + "&field1=%s&field2=%s" % (hum, temp1))
        f.close()
    except Exception as e:
        print('Holy Cow, something Broke!!! exiting.' + str(e))


if __name__ == '__main__':
    main()
