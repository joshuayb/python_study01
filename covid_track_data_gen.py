'''from random import *
a = 0
for i in range(1,51):
    place = randint(1,10)
    if 9<= place <=10:
        print ("{0}H{1}" . format(i, place))
        a += 1
    else:
        print ("{0}W{1}" . format(i, place))
print ("total at home: {0}". format(a))'''

from random import *
a = 0
for i in range(1,51):
    place = randint(1,10)
    if 9 <= place <= 10:
        geo = str(i) + 'H' + str(place)
        a += 1
        print (geo)
    else:
        geo = str(i) + 'W' + str(place)
        print (geo)
        
print ("total at home: {0}". format(a))