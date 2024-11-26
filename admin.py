import functions
import car

from functools import reduce



def avtorization_admin(count):
    for _ in range(3):
        
        login_admin = input("Введите логин: ")

        if login_admin == 'wwordyy':
            print("Вы успешно указали данные!", end='\n\n')
            count = 3
            functions.clear()

            break
        else:
            count -= 1
            if count == 0:
                print("Количество попыток было израсходовано! Попробуйте позднее.", end='\n\n')

                functions.clear()
                functions.function_start_menu()

                break
            else:
                print(f"Ошибка. Попробуйте снова! (Количество попыток: {count})", end="\n\n")

    if count > 0:
        for _ in range(3):
            
            password_admin = input("Введите пароль: ")

            if password_admin == "00000":
                print("Вы успешно указали данные!",end='\n\n')
                functions.clear()

                
                print("Добро пожаловать! Вы авторизовались как администратор!")
                break
            else:
                count -= 1
                if count == 0:
                    print("Количество попыток было израсходовано! Попробуйте позднее.",end='\n\n')

                    functions.clear()
                    functions.function_start_menu()
                
                    break
                else:
                    print(f"Ошибка. Попробуйте снова! (Количество попыток: {count})")



def add_car():

    try:
        while True:
            print("Сколько автомобилей необходимо добавить? (max: 5)", end="\n\n")

            admin_car_count = int(input("Введите количество автомобилей: "))

            if admin_car_count > 0 and admin_car_count <= 5:

                for _ in range(admin_car_count):

                    print()

                    admin_car = {
                    "Модель": input("Введите модель авто: "),
                    "Двигатель" : input("Количество Л.C: "),
                    "Коробка передач" : input("Коробка передач: "),
                    "Привод": "Укажите привод: ",
                    "Год выпуска": int(input("Укажите год выпуска: ")),
                    "Цвет" : input("Цвет авто: "),
                    "Цена (РУБ)" : float(int(input("Введите цену авто: "))),
                    "Доступна для продажи":  bool(input("Доступна ли для продажи, True/False: ")),}

                    print()
                    
                    car.cars.append(admin_car)

                    print("Машина успешно добавлена!!!", end="\n\n")

                    print("Для того, чтобы вернуться в главное меню", end="\n\n")
                    functions.clear()

                    functions.function_admin()

                break
            else:
                print("Вы указали неверное количество авто! Попробуйте снова.")

                functions.clear()

    except Exception as error:
        print(f"Ошибка: {error}")

        functions.clear()
        functions.function_admin()

def delete_car():

    while True:
        try:
            print("Какое авто необходимо удалить?", end='\n\n')
            user_delete_car = int(input("Введите номер авто в автосалоне: "))
            
            for key, value in car.cars[user_delete_car - 1].items():
                
                if key == "Модель":
                    model = value

                    print()
                    print(f"Автомобиль: {model} была полностью удалена из автосалона!!!")
            car.cars.pop(user_delete_car - 1)

            functions.clear()
            
            functions.function_admin()
    
            break

        except Exception as error:
            print(f"Ошибка: {error}")

            functions.clear()
        
def come_back_menu():
    functions.clear()
    functions.function_start_menu()

def sum_price_car():
    
    result = reduce(lambda sum, car: sum + car["Цена (РУБ)"], car.cars, 0)
    
    print(f"Общая стоимость всех автомобилей: {result}")

    functions.clear()
    functions.function_admin()

def user_data():

    result = list(zip(functions.user.logins, functions.user.passwrods))

    count_user = 1

    if len(result) > 0:     
        for i in result:
            print(f"Пользователь: {count_user}")
            print(f"Логин: {i[0]} | Пароль: {i[1]}", end="\n\n")
            count_user += 1
        
        functions.clear()
        functions.function_admin()
    else:
        print("Данные отсутствуют!", end="\n\n")

        functions.clear()
        functions.function_admin()


