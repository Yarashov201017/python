# vaqtlar
import datetime as dt
from datetime import datetime
hozir = dt.datetime.now()
print(hozir)
# sanani ajratib olish
print(hozir.date())
# vaqtni ajratib olish
print(hozir.time())
# soatni ajratib olish
print(hozir.hour)
# minutni ajratib olish
# print(hozir.minute)
# sekundni ajratib olish
# print(hozir.second)
# hozir = dt.datetime.now()
# futbol = dt.datetime(2021, 3, 10, 23, 45, 00)
# farq= futbol-hozir
# sekundlar = farq.seconds
# minutlar = int(sekundlar/60)
# soatlar = int(minutlar/60)
# print(f"Futbol boshlanishiga {sekundlar} sekund qoldi")
# print(f"Futbol boshlanishiga {minutlar} minut qoldi")
# print(f"Futbol boshlanishiga {soatlar} soat qoldi")

# Source - https://stackoverflow.com/q
# Posted by user3778327, modified by community. See post 'Timeline' for change history
# Retrieved 2025-11-15, License - CC BY-SA 4.0

datem = datetime.today().strftime("%Y")
# datem = datetime.strptime(datem, "%Y")
print(datem)