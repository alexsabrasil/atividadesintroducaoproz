andarHotel = 0

for i in range(21):
    andarHotel = andarHotel + 1
    if andarHotel == 13:
        continue
    print (andarHotel)

andarHotel = 21

while andarHotel > 0:
    if andarHotel == 13:
        andarHotel -= 1
        continue
    print(andarHotel)
    andarHotel -= 1