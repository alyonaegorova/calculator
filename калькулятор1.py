name=input("Введите ваше имя") #Пользователь вводит имя
print("Здравствуйте,", name) #Приветсвие пользователя
a=float(input("Введите первое число")) #Ввод первого числа
b=float(input("Введите второе число")) #Ввод второго числа
print("Список действий: +,-,*,/") #Доступные действия
c=str(input("Введите действие")) #Ввод действия
if с=="+":
    print("Рузультат:",a+b) #Результат сложения
elif c=="-":
    print("Результат:",a-b) #Результат вычитания
elif c=="*":
    print("результат:",a*b) #Результат умножения
elif c=="/":
    print("Результат:",a/b) #Результат деления
else:
    print("Выбрана неверная команда!")
s=(input("Продолжить?(Y/N)"))
if s=="Y":
    print()
elif s=="N":
    print("Программа завершена!")
