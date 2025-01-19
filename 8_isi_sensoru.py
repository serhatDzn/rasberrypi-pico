import machine
import utime

sicaklik_sensoru = machine.ADC(4)

birim_donusum = 3.3 / (65535)

while True:
    okuma = sicaklik_sensoru.read_u16()*birim_donusum

    formul = 27 - (okuma-0.706)/0.01721

    print("Temparature :",formul)
    utime.sleep(2)