# Créé par Yanis Boulogne, le 04/01/2022 en Python 3.7

import psutil
import time

def core_temp(t):
    while True:
        temp = psutil.sensors_temperatures()
        print(temp)
        time.sleep(t)