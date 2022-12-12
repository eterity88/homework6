# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние
# между ними в 2D пространстве.


# x1=int(input("введите x1 : "))
#
# x2=int(input("введите x2 : "))
#
# y1=int(input("введите y1 : "))
#
# y2=int(input("введите y2 : "))
#
# S = round(((x2 - x1)**2 + (y2 - y1)**2)**(1/2), 2)
#
# print('Расстояние между точками в 2D пространстве', S)



from math import sqrt

square_lambda = lambda x, y:(y-x)**2

def distance(x1, y1, x2, y2):
    return sqrt(square_lambda(x1, x2)+ square_lambda(y1, y2))

x1 = int(input("Введите координату x1 "))
y1 = int(input("Введите координату y1 "))
x2 = int(input("Введите координату x2 "))
y2 = int(input("Введите координату y2 "))
print('Расстояние между точками в 2D пространстве:', distance(x1, y1, x2, y2))