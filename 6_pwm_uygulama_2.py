import machine
import utime

led = machine.Pin(20,machine.Pin.OUT)

pwm = machine.PWM(led)
pwm.freq(25000)
buton = machine.Pin(22,machine.Pin.IN,machine.Pin.PULL_DOWN)

x= 0

while True:
    if buton.value()==1:
        x+=1
        print(x)
        utime.sleep(2)
    if x==1:
        pwm.duty_u16(20000)
    elif( x==2):
        pwm.duty_u16(35000)
    elif( x==3):
        pwm.duty_u16(65000)
    elif( x==4):
        pwm.duty_u16(0)
        x = 0