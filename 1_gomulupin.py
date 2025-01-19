from machine import Pin
from time import sleep

led = Pin("LED", Pin.OUT)  # Gömülü LED'i kontrol etmek için "LED" alias'ı kullanılır
sayac = 5
while sayac!=0:
    led.value(1)  # LED'i aç
    sleep(1)  # 1 saniye bekle
    led.value(0)  # LED'i kapat
    sleep(1)  # 1 saniye bekle
    print(sayac)
    sayac-=1
