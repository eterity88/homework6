#Задайте список из вещественных чисел. Напишите программу, которая найдёт
# разницу между максимальным и минимальным значением дробной части элементов.
#Пример: [1.1, 1.2, 3.1, 5, 10.01] => 0.19


# list=map(float, input("Введите вещественные числа через пробел:\n").split())
# new_list = [round(i%1,2) for i in list if i%1 != 0]
# print(max(new_list) - min(new_list))


def UserInput(inputText):
    userEnter = input(f"{inputText}")
    return userEnter


def FillList(list):
    userList = [i for i in list]
    return userList


userEnter = map(float, UserInput("Введите вещественные числа через пробел: ").split(" "))
newList = list(FillList(userEnter))
integerList = [(i - int(i)) for i in newList]

differ = max(integerList) - min(integerList)

answer = round(float(int(differ * 1000) / 1000),2)

print(f"Разница между максимальным и минимальным значением дробной части элементов: {answer}")