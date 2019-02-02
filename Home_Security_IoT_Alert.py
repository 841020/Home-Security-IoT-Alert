#import module
import spidev
import time
import RPi.GPIO as GPIO
import os
import requests
# open(bus, device) : open(X,Y) will open /dev/spidev-X.Y
spi = spidev.SpiDev()
spi.open(0, 0)
# set up GPIO
GPIO.setmode(GPIO.BOARD)
# Define output
GPIO.setup(38, GPIO.OUT)
GPIO.setup(35, GPIO.OUT)
GPIO.setup(37, GPIO.OUT)
# Read SPI data from MCP3008, Channel must be an integer


def ReadADC(ch):
    if (ch > 7) or (ch < 0):
        return -1
    adc = spi.xfer2([1, (8+ch) << 4, 0])
    data = ((adc[1] & 3) << 8)+adc[2]
    return data


# Define sensor channels
pir_ch = 0
ky_ch = 1
swich_ch = 2
kobe_ch = 3
fire_ch = 4
# Define delay between readings
delay = 1

while True:
    try:
        ky = ReadADC(ky_ch)
        pir = ReadADC(pir_ch)
        kobe = ReadADC(kobe_ch)
        fire = ReadADC(fire_ch)
        swich = ReadADC(swich_ch)

        print("pirmov  : ", pir,
              " ky024 : ", ky,
              "swi:", swich,
              "gas:", kobe,
              "fire:", fire, )
        # If the magnetic sensor detects the bathroom door closing
        if swich < 500:
            # Output voltage to infrared sensor(pin 37 output high voltage)
            GPIO.output(37, True)
            # In-bath infrared sensor detects if there is activity in the bathroom
            if pir > 500:
                # LED warning light is on(pin 38 output high voltage)
                GPIO.output(38, True)
                # Buzzer has no alarm(pin 35 output low voltage)
                GPIO.output(35, False)
            # In-bath infrared sensor detects if there not is activity in the bathroom
            else:
                # LED warning light is close(pin 38 output low voltage)
                GPIO.output(38, False)
                # Buzzer alarm(pin 35 output high voltage)
                GPIO.output(35, True)
                # Send data to ifttt.com by HTTP Post Method, and ifttt sends e-mail to the user.
                payload = {'value1': 'warring '}
                r = requests.post(
                    "https://ifttt.com/applets/Zp6vmhJx-get-an-email-when-webhooks-publishes-a-new-trigger-or-action?term=webhook", params=payload)
        # If KY-024 detects the bathroom door not closing
        else:
            # low voltage to infrared sensor(pin 37 output low voltage)
            GPIO.output(37, False)
        # If the magnetic sensor detects that the door and window are opened
        if ky > 500:
            # Buzzer alarm(pin 35 output high voltage)
            GPIO.output(35, True)
            # Send data to ifttt.com by HTTP Post Method, and ifttt sends e-mail to the user.
            payload = {'value1': 'ky024 on '}
            r = requests.post(
                "https://ifttt.com/applets/Zp6vmhJx-get-an-email-when-webhooks-publishes-a-new-trigger-or-action?term=webhook", params=payload)
        # If the magnetic sensor detects that the door and window are not opened
        else:
            # Buzzer has no alarm(pin 35 output low voltage)
            GPIO.output(35, False)
        # If the gas detector detects a high concentration of gas
        if kobe > 150:
            # Buzzer alarm(pin 35 output high voltage)
            GPIO.output(35, True)
            # Send data to ifttt.com by HTTP Post Method, and ifttt sends e-mail to the user.
            payload = {'value2': 'gas on '}
            r = requests.post(
                "https://ifttt.com/applets/Zp6vmhJx-get-an-email-when-webhooks-publishes-a-new-trigger-or-action?term=webhook", params=payload)
        # If the gas detector not detects a high concentration of gas
        else:
            # Buzzer has no alarm(pin 35 output low voltage)
            GPIO.output(35, False)
        # If the flame detector detects the flame
        if fire < 500:
            # Buzzer alarm(pin 35 output high voltage)
            GPIO.output(35, True)
            # Send data to ifttt.com by HTTP Post Method, and ifttt sends e-mail to the user.
            payload = {'value3': 'fire on '}
            r = requests.post(
                "https://ifttt.com/applets/Zp6vmhJx-get-an-email-when-webhooks-publishes-a-new-trigger-or-action?term=webhook", params=payload)
        # If the flame detector not detects the flame
        else:
            # Buzzer has no alarm(pin 35 output low voltage)
            GPIO.output(35, False)
        time.sleep(delay)
    except IOError:
        print("Error")
