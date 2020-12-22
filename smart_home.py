import time
import datetime
import logging

import requests
import spidev
import RPi.GPIO as GPIO


class smart_home:
    def __init__(self):
        dt = {
            'level': logging.DEBUG,
            'format': '%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
            'datefmt': '%m-%d %H:%M',
            'filename': 'iot.log',
            'filemode': 'w'
        }
        logging.basicConfig(**dt)

        self.spi = spidev.SpiDev()
        self.spi.open(0, 0)

        self.pir_ch = 0
        self.ky024_ch = 1
        self.switch_ch = 2
        self.gas_ch = 3
        self.fire_ch = 4

        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(35, GPIO.OUT)
        GPIO.setup(37, GPIO.OUT)
        GPIO.setup(38, GPIO.OUT)


    def process(self):
        def ReadADC(ch):
            if (ch > 7) or (ch < 0):
                return -1

            adc = self.spi.xfer2([1, (8+ch) << 4, 0])
            data = ((adc[1] & 3) << 8)+adc[2]

            return data
        while True:
            date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
            try:
                pir = ReadADC(self.pir_ch)
                ky024 = ReadADC(self.ky024_ch)
                switch = ReadADC(self.switch_ch)
                gas = ReadADC(self.gas_ch)
                fire = ReadADC(self.fire_ch)

                print('pir:{}, ky024:{}, switch:{}, gas:{}, fire:{}'.format(pir, 
                                                                            ky024,
                                                                            switch, 
                                                                            gas,
                                                                            fire))
                payload = dict()

                if switch < 500:
                    GPIO.output(37, True)
                    if pir > 500:
                        GPIO.output(38, True)
                        GPIO.output(35, False)
                    else:
                        GPIO.output(38, False)
                        GPIO.output(35, True)
                        logging.info('{}-Someone may fall in the bathroom'.format(date))
                        payload['value1'] = 'Fall_detection: Someone may fall in the bathroom'
                else:
                    GPIO.output(37, False)

                if ky024 > 500:
                    GPIO.output(35, True)
                    logging.info('{}-Security_system: The window is opened'.format(date))
                    payload['value2'] = 'Security_system: The window is opened'
                else:
                    GPIO.output(35, False)

                if gas > 150:
                    GPIO.output(35, True)
                    logging.info('{}-Indoor detection of gas'.format(date))
                    payload['value3'] = 'Gas_detection: Indoor detection of gas'
                else:
                    GPIO.output(35, False)

                if fire < 500:
                    GPIO.output(35, True)
                    logging.info('{}-Indoor detection of fire'.format(date))
                    msg = {'fire_detection': 'Indoor detection of fire'}
                    payload['value3'] = '{}{}'.format(payload.get('value3', ''), msg)
                else:
                    GPIO.output(35, False)

                url = 'https://maker.ifttt.com/trigger/smart_home/with/key/'
                res = requests.post(url, json=payload)
                if res.text != "Congratulations! You've fired the smart_home event":
                    raise Exception('http request failed')
                time.sleep(1)

            except Exception as e:
                print("{}".format(e))


if __name__ == "__main__":
    smart_home().process()
