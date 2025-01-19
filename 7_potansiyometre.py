import machine
import utime

pot = machine.ADC(27)

while True:
    deger=pot.read_u16()
    print(deger)
    utime.sleep(0.5)

