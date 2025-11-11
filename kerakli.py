# vaqtlar
import datetime as dt
hozir = dt.datetime.now()
print(hozir)
# sanani ajratib olish
print(hozir.date())
# vaqtni ajratib olish
print(hozir.time())
# soatni ajratib olish
print(hozir.hour)
# minutni ajratib olish
print(hozir.minute)
# sekundni ajratib olish
print(hozir.second)
hozir = dt.datetime.now()
futbol = dt.datetime(2021, 3, 10, 23, 45, 00)
farq= futbol-hozir
sekundlar = farq.seconds
minutlar = int(sekundlar/60)
soatlar = int(minutlar/60)
print(f"Futbol boshlanishiga {sekundlar} sekund qoldi")
print(f"Futbol boshlanishiga {minutlar} minut qoldi")
print(f"Futbol boshlanishiga {soatlar} soat qoldi")