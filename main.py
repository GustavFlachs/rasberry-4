from machine import Pin
import time

Button = Pin(1 , Pin.IN)
led1 = Pin(0, Pin.OUT)
led2 = Pin(2, Pin.OUT)
led3 = Pin(3, Pin.OUT)
led4 = Pin(4, Pin.OUT)

while True:
    if Button.value() == 1 and led1.value() == 0:
        led1.value(1)

    if led1.value() == 1 and Button.value() == 1:
        led2.value(1)

    if led1.value() == 1 and led2.value() == 1 and Button.value() == 1:
        led3.value(1)

    if led1.value == 1 and led2.value() == 1 and led3.value() == 1 and Button.value() == 1:
        led4.value(1)

    if led1.value() == 1 and led2.value() == 1 and led3.value() == 1 and led4.value() == 1 and Button.value() == 1:
        led1.value(0)
        led2.value(0)
        led3.value(0)
        led4.value(0)


#kod nefunguje protože může být jen jeden if který je true v cyklu
#"pass" byl přidán after ale nevím jestli funguje ale teoryticky by mělo... snad
    ##Kod dle mistra gpt idk if funguje bo ne nejspíš ne jak to koukam
#from machine import Pin
#import time

# Definice tlačítka a LEDek
#Button = Pin(1, Pin.IN)
#led1 = Pin(0, Pin.OUT)
#led2 = Pin(2, Pin.OUT)
#led3 = Pin(3, Pin.OUT)
#led4 = Pin(4, Pin.OUT)

# Stav pro sledování pokroku
#state = 0

#while True:
    # Kontrola, zda je tlačítko stisknuté
  #  if Button.value() == 1:
  #      time.sleep(0.2)  # Debounce, aby se zabránilo falešným stiskům
 #       
#        if state == 0:
            #led1.value(1)  # Zapne LED1
            #state = 1
        #elif state == 1:
            #led2.value(1)  # Zapne LED2
            #state = 2
        #elif state == 2:
            #led3.value(1)  # Zapne LED3
            #state = 3
        #elif state == 3:
            #led4.value(1)  # Zapne LED4
            #state = 4
        #elif state == 4:
            # Vypne všechny LEDky a resetuje stav
            #led1.value(0)
            #led2.value(0)
            #led3.value(0)
            #led4.value(0)
            #state = 0
            