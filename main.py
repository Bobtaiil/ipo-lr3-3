day = int(input("Введите день: ")) # требование ввода кол-во дней и месяцев
month = int(input("Введите месяц: ")) # требование ввода кол-во дней и месяцев

if month == 4 or month == 6 or month == 9 or month == 11: # в 4,6,9,11 месяцах кол-во дней = 30
    if day > 30: # в 4,6,9,11 месяцах кол-во дней = 30
        print("Дата введена неверно.")  # в 4,6,9,11 месяцах кол-во дней = 30
        exit(0) #выход
        
if day > 31 or day < 1 or month > 12 or month < 1: #проверка правильности ввода даты
    print("Дата введена неверно.") #проверка правильности ввода даты
elif month == 2 and day > 28: #проверка правильности ввода даты
    print("Дата введена неверно.") #проверка правильности ввода даты
elif 1 <= month <= 2 or month == 12: #проверка сезона 
    print("Зима") #вывод сезона при выполнении соотв. условия
elif 3 <= month <= 5: #проверка сезона 
    print("Весна") #вывод сезона при выполнении соотв. условия
elif 6 <= month <= 8: #проверка сезона 
    print("Лето") #вывод сезона при выполнении соотв. условия
else: #проверка сезона 
    print("Осень") #вывод сезона при выполнении соотв. условия