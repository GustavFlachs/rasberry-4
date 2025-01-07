from machine import Pin
import time

Button = Pin(0 , Pin.IN, Pin.PULL_DOWN)
led1 = Pin(1, Pin.OUT)
led2 = Pin(2, Pin.OUT)
led3 = Pin(3, Pin.OUT)

x = 0
loop = 0
y = 0

while True:
    if Button.value() == 1 and x == 0:
        time.sleep(0.3)
        led1.value(1)
        led2.value(1)
        led3.value(1)
        x += 1
        print(x)
    if Button.value() == 1 and x == 1:
        time.sleep(0.3)
        loop += 1
        while loop == 1 and x == 1:
                led1.value(1)
                led2.value(1)
                led3.value(1)
                time.sleep(0.1)
                led1.value(0)
                led2.value(0)
                led3.value(0)
                time.sleep(0.1)
                print("blik")
                if Button.value() == 1:
                        time.sleep(0.3)
                        x -= 1
                        loop -= 1



