#спросить 2 ЧЕТНЫХ числа
#первое число это начало второе конец
start= int(input("Первое число:"))
stop = int(input("Второе число:"))
x = 0
if start %2 == 0 and stop %2 == 0:
    for x in range (start, stop + 2 , 2):
        print (x)
        x += 2
else:
    for x in range (start, stop , 2 ):
        x += 2
        print (x)