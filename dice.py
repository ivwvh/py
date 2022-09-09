#импорт функции
import random
#получаем два числа
user=random.randint(1,6)
cpu=random.randint(1,6)
#выводим два числа
print("Пользователь выбросил:",user)
print("ПК выбросил:",cpu)
#результаты
if cpu>user:
    print("Компьютер победил")
elif user==cpu:
    print("Ничья")
else:
    print("Пользователь победил")