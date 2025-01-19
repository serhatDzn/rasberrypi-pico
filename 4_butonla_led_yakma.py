import machine

led = machine.Pin(20,machine.Pin.OUT)
# buton = machine.Pin(22,machine.Pin.IN,machine.Pin.PULL_DOWN)

while True:
#    if buton.value() == 1:
        led.value(1)
#    else:
#        led.value(0)

