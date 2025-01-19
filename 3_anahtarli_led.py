import machine
import utime

# GP5 pini giriş ve pull-down ile yapilandirildi
buton = machine.Pin(5, machine.Pin.IN, machine.Pin.PULL_DOWN)

print("Pico başlatildi...")

while True:
    try:
        buton_durumu = buton.value()
        print(f"Buton durumu: {buton_durumu}")
        if buton_durumu == 1:
            print("Butona basildi!")
        else:
            print("Butona basilmadi.")
        utime.sleep(1)
    except Exception as e:
        print(f"Hata: {e}")
        break