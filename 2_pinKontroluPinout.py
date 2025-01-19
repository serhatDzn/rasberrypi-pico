import machine
from time import sleep
led_gomulu = machine.Pin("LED", machine.Pin.OUT)
print(led_gomulu)

led_gomulu.on()

sleep(3)
led_gomulu.off()