import machine
import utime

led = machine.Pin(20, machine.Pin.OUT)

pwm = machine.PWM(led)

x = 0

while (x < 65535):
    pwm.duty_u16(x)
    utime.sleep(0.005)
    x += 10
    print(x)


# led.value(1)
# utime.sleep(5)
# led.value(0)