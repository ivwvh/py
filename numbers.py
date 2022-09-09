# задача:
# получить от пользователя три числа и сравнить их
# узнать кол-во равных
# вывести на экран кол-во равных чисел
num1 = int(input())
num2 = int(input())
num3 = int(input())
if num1 == num2 == num3:
    print("3")
elif num1 == num2 or num2 == num3 or num3 == num1:
    print("2")
else:
    print("0")
