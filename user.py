import functions
import random
import car

logins = []
passwrods = []


def avtoriation_user():
    result = True

    while result:
        login_user_menu = input("Введите логин: ")

        if (len(login_user_menu)) == 1 or (len(login_user_menu) <= 4):
            print("""Ошибка! Минимальное количество символов 5.
Попробуйте еще!""",end="\n\n")
            
        else:
            result = False
            print()
            print('Вы успешно ввели логин!')
            print()

            logins.append(login_user_menu)

            functions.clear()

    while (result != True):
        password_user_menu = input("Введите пароль: ")
        
        if (len(password_user_menu)) == 1 or (len(password_user_menu) <= 4):
            print("""Ошибка! Минимальное количество символов 5.
Попробуйте еще!""",end="\n\n")
            
        else:
            result = True
            print()
            print('Вы успешно ввели пароль!')
            print()
            
            passwrods.append(password_user_menu)

            functions.clear()

            print(f"Ваш логин: {login_user_menu}")
            print(f"Ваш пароль: {password_user_menu}")
            

def car_characteristics(cars):

    print("""Для того, чтобы узнать характеристи авто, необходимо указать его порядок 
в автосалоне!""", end="\n\n")

    

    while True:
        try:
            user = int(input("Введите число: "))
            print()

            if user <= 10 and user > 0:
                for key,value in cars[user - 1].items():
                    print(f"{key} --- {value}")
                
                print()
                print("Вернуться назад.",end=' ')
                functions.clear()

                
                functions.function_user()
                    
                break

                
            else:
                print("Вы указали неверный номер авто!", end='\n\n')
                

        except Exception as error:
            print(F"Ошибка: {error}", end='\n\n')
            print("Попробуйте еще раз.", end='\n\n')

            functions.clear()

            

            


def balance_user():

    balance = float(random.randint(150000,100000000))

    return balance


def buy_car(cars):

    balance = balance_user()
    while True:

        result = True

        try:
            print(f"Ваш баланс: {balance}",end='\n\n')

            print("Какой автомобиль хотите преобрести?")

            user_avto = int(input("Введите номер авто в автосалоне: "))

            print()

            for key, value in car.cars[user_avto - 1].items():

                print(f"{key} --- {value}")

                if key == "Доступна для продажи":
                    if value == False:

                        print()
                        print("Данная машина недоступна для продажи! Выберите другую машину.")
                        result = False

                        functions.clear()

            
            if result == True:

                print(end="\n\n")


                print("Вы уверены в своей покупке?")

                
                user_solution = input("Да или нет, введите ответ:  ")
                if user_solution == "Да" or user_solution == "да":

                    for key, value in cars[user_avto - 1].items():
                        if key == "Цена (РУБ)":
                            price = value
                        
                        if key == "Модель":
                            model = value
                        
                        
                
                    if price <= balance:
                        result_balance = balance - price
                        print(f"Вы преобрели: {model}. Поздравляем вас с покупкой!!!", end="\n\n")
                        print(f"Ваш баланс: {result_balance}")

                        car.cars.pop(user_avto - 1)

                        functions.clear()

                        functions.function_user()
                        
                        break

                    else:
                        print(f"У вас недостаточно средств! Ваш баланс: {balance}")
                
                elif user_solution == "Нет" or user_solution == "нет":
                    
                    print("Для того, чтобы вернуться в главное меню", end="\n\n")

                    functions.clear()

                    functions.function_user()

                    break

                else:
                    print("Введите корректное значение!")

                    functions.clear()

        except Exception as error:

            print(f"Ошибка: {error}", end="\n\n")

            functions.clear()


def user_discount_car():

    result_discount_car = list(map(lambda x: {**x, "Цена (РУБ)": x["Цена (РУБ)"] // 2}, car.cars))

    for i in result_discount_car:
        for key, value in i.items():

            print(f"{key} --- {value}")

        print()

    functions.clear()

    functions.function_user()

    

def filter_car():


    try:
        print("""   Выберите вариант фильтрации:
    1. Фильтрация по цвету.
    2. Фильтрация по году выпуска.
    3. Фильтрация по приводу.""")

        
        filtering_option_user = int(input())

        if filtering_option_user == 1:
            
            print("""По какому цвету необходимо отфильтровать?
    1. Белый
    2. Черный
    3. Красный""", end="\n\n")
            color_filter = int(input())

            if color_filter == 1:
                function_filter("Цвет", "Белый")
            elif color_filter ==2:
                function_filter("Цвет", "Черный")
            elif color_filter == 3:
                function_filter("Цвет", "Красный")
            
        
        elif filtering_option_user == 2:
            
            print("""Укажите год, по которому необходимо отфильтровать.
    1. 2024
    2. 2023
    3. 2014 """, end="\n\n")

            years_filter = int(input())

            if years_filter == 1: 
                function_filter("Год выпуска", 2024)
            elif years_filter == 2:
                function_filter("Год выпуска", 2023)
            elif years_filter == 3:
                function_filter("Год выпуска", 2014)


        elif filtering_option_user == 3:

            print("""Выберите привод по которому необходимо отфильтровать.
    1. Передний
    2. Задний
    3. Полный""", end="\n\n")

            drive = int(input())

            if drive == 1:
                function_filter("Привод", "Передний")
            elif drive == 2:
                function_filter("Привод", "Задний")
            elif drive == 3:
                function_filter("Привод", "Полный")

        else:
            print("Введите корректное значение!!!")

            functions.clear()
            functions.function_user()

    except Exception as error:
        print(f"Ошибка: {error}")

        functions.clear()
        functions.function_user()
        

def function_filter(key_filter, value_filter):


    result_filter = list(filter(lambda car: car [key_filter] == value_filter, car.cars))

    if len(result_filter) > 0:

        for i in result_filter:
            for key, value in i.items():

                print(f"{key} -- {value}")
                
            print()

        functions.clear()
        functions.function_user()

    else:
        print("Таких данных нет!!!")

        functions.clear()
        functions.function_user()

