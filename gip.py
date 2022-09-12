# вычисление гипотенузы
# в геометрии сумма квадрата гипотенузы равна сумме квадратов катетов
# задача:
# получить от пользователя катеты и найти гипотенузу по формуле
kat1=int(input())
kat2=int(input())
gipsqr=kat1**2 + kat2**2
import math
from math import (sqrt)
gip= sqrt(gipsqr)
print(gip)