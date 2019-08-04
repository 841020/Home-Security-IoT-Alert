import requests
import time
import json

import spidev
import RPi.GPIO as GPIO


spi = spidev.SpiDev()
spi.open(0, 0)

GPIO.setmode(GPIO.BOARD)
GPIO.setup(35, GPIO.OUT)
GPIO.setup(37, GPIO.OUT)
GPIO.setup(38, GPIO.OUT)


def ReadADC(ch):
    if (ch > 7) or (ch < 0):
        return -1
    adc = spi.xfer2([1, (8+ch) << 4, 0])
    data = ((adc[1] & 3) << 8)+adc[2]
    return data


pir_ch = 0
ky024_ch = 1
switch_ch = 2
gas_ch = 3
fire_ch = 4

delay = 1

while True:
    try:
        pir = ReadADC(pir_ch)
        ky024 = ReadADC(ky024_ch)
        switch = ReadADC(switch_ch)
        gas = ReadADC(gas_ch)
        fire = ReadADC(fire_ch)

        print('pir:{}, ky024:{}, switch:{}, gas:{}, fire:{}'.format(pir, ky024,
                                                                    switch, gas,
                                                                    fire))
        url = 'https://maker.ifttt.com/trigger/home_iot/with/key'
        payload = {}

        if switch < 500:
            GPIO.output(37, True)
            if pir > 500:
                GPIO.output(38, True)
                GPIO.output(35, False)
            else:
                GPIO.output(38, False)
                GPIO.output(35, True)
                payload['value1'] = 'Fall_detection: Someone may fall in the bathroom '
        else:
            GPIO.output(37, False)

        if ky024 > 500:
            GPIO.output(35, True)
            payload['value2'] = 'Security_system: The window is opened'
        else:
            GPIO.output(35, False)

        if gas > 150:
            GPIO.output(35, True)
            payload['value3'] = 'Gas_detection: Indoor detection of gas'
        else:
            GPIO.output(35, False)

        if fire < 500:
            GPIO.output(35, True)
            msg = {'fire_detection': 'Indoor detection of fire '}
            payload['value3'] = '{}{}'.format(payload.get('value3', ''), msg)
        else:
            GPIO.output(35, False)

        payload = json.dumps(payload)
        res = requests.post(url, params=payload)
        time.sleep(delay)

    except IOError:
        print("Error")