#Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.

#Пример:

#- 6 -> да
#- 7 -> да
#- 1 -> нет

day = int (input ("введите номер дня недели"))
if day ==6 or day == 7:
    print("да")
elif   0 < day < 6:
    print ("нет")
else:
    print("число не соответствует дню недели")
