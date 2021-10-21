import random, math
import winsound
from datetime import datetime
import sys
import locale
locale.setlocale(locale.LC_ALL, 'pl_PL')

def factorial(n):
    if n==0:
        return 1
    else:
        return n*factorial(n-1)

def combi(n, k):
    product = n-k+1
    for x in range((n-k+2), n+1):
        product = product*x
    return product/factorial(k)

def brine(water, concentration):
    salt = (water*concentration/100.)/(1-concentration/100.)
    return round(salt)

def lotto():
    #Optymalizacja
    tablica_liczb = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49]
    result = [0,0,0,0,0,0]
    result[0] = tablica_liczb.pop(int(random.random()*49))
    result[1] = tablica_liczb.pop(int(random.random()*48))
    result[2] = tablica_liczb.pop(int(random.random()*47))
    result[3] = tablica_liczb.pop(int(random.random()*46))
    result[4] = tablica_liczb.pop(int(random.random()*45))
    result[5] = tablica_liczb[int(random.random()*44)]
    result.sort()
    return result

def losuj():
    timestamp_start = datetime.now()
    print("Czas rozpoczęcia:",timestamp_start)    
    # Obstawiany zakład lotto to 'b'
    b = lotto()
    print("Pierwszy zakład:\t",b)
    # Wyniki losowania lotto to 'a'
    #a = [2, 3, 32, 33, 42, 44]
    a = [7, 10, 18, 19, 35, 39] #lotto()
    print("Pierwszy wynik:\t\t",a)
    # Tyle zakładów już obstawiliśmy
    licznik_zakladow = 1
    print("Czekaj...")
    # Drukowanie na ekran zajmuje czas, dlatego aktualizuję stempel czasowy startu
    timestamp_start = datetime.now()
    while a!=b:
        # Losuj nowy zakład
        b = lotto()
        #print(b)
        # Losuj nowy wynik
        #a = lotto()
        licznik_zakladow += 1
    timestamp_end = datetime.now()
    print("Trafiono szóstkę.")
    print("Wytypowane liczby:\t",b)
    print("Wynik losowania:\t",a)
    print("Czas zakończenia:",timestamp_end)
    print("Obstawiono łącznie:",locale.format("%d", licznik_zakladow, grouping=True),"zakładów.")
    czas_losowania = timestamp_end-timestamp_start
    print("Prędkość losowania:",locale.format("%d",(licznik_zakladow-1)/(czas_losowania).total_seconds(),grouping=True),"zakł/s")
    print("Czas losowania [HH:MM:SS]:",str(czas_losowania))
    print("Czas losowania [s]:",locale.format("%d",(czas_losowania).total_seconds(), grouping=True),"\n")
    frequency = 1500
    duration1 = 100
    winsound.Beep(frequency, duration1)
    #winsound.Beep(frequency, duration1)
    #winsound.Beep(frequency, duration1)
    return [licznik_zakladow, czas_losowania, timestamp_start, timestamp_end]

def monteCarlo():
    sum = 0
    quantity = 100000000
    R=1.0
    for i in range(0,quantity):
        x1 = (random.random()*2)-1
        y1 = (random.random()*2)-1
        while (x1**2+y1**2)**0.5>R:
            x1 = (random.random()*2)-1
            y1 = (random.random()*2)-1
        x2 = (random.random()*2)-1
        y2 = (random.random()*2)-1
        while (x2**2+y2**2)**0.5>R:
            x2 = (random.random()*2)-1
            y2 = (random.random()*2)-1
        d=((x2-x1)**2+(y2-y1)**2)**0.5
        sum += d

    average = sum/quantity
    print("sum:",sum)
    print("Średnia odległość:",average)


quantity = 5
stats = []
for i in range(0,quantity):
    print("\n"+str(i+1)+"/"+str(quantity),str(round((i+1)/quantity*100,2))+"%")
    stats.append(losuj())
"""
stats.append(losuj())
stats.append(losuj())
stats.append(losuj())
stats.append(losuj())
stats.append(losuj())
stats.append(losuj())
stats.append(losuj())
stats.append(losuj())
stats.append(losuj())
stats.append(losuj())
stats.append(losuj())
stats.append(losuj())
stats.append(losuj())
stats.append(losuj())
"""
"""

    
"""
# Wyświetla końcowe statystyki
quantity = len(stats)
sum = 0
for i in stats:
    sum += i[0]
average = sum/quantity

for i in range(0,quantity):
    print(str(i+1)+":",locale.format("%d", stats[i][0], grouping=True),",",stats[i][1])

ticket_counter = []
for i in range(0,quantity):
    ticket_counter.append(stats[i][0])
ticket_counter.sort()

print("\nMin. zakładów do trafienia szóstki:",locale.format("%d",ticket_counter[0], grouping=True))
print("Max. zakładów do trafienia szóstki:",locale.format("%d",ticket_counter[-1], grouping=True))

print("Średnia ilość zakładów na trafienie:",locale.format("%d", average, grouping=True))
calkowity_czas_losowania = stats[quantity-1][3]-stats[0][2]
print("Całkowity czas losowania",calkowity_czas_losowania,"\n")

frequency = 1500
duration1 = 100
winsound.Beep(frequency, duration1)
winsound.Beep(frequency, duration1)
winsound.Beep(frequency, duration1)
winsound.Beep(frequency, duration1)
winsound.Beep(frequency, duration1)
winsound.Beep(frequency, duration1)




