import functions

def print_sorted(user_text, sorted_cars):

    print()
    print(user_text, end="\n\n")

    for i in sorted_cars:
        for key, value in i.items():

            if key == "Модель":

                print(f"{key} -- {value}")
            
        print()
            



cars = [{   "Модель": "LADA Vesta",
            "Двигатель" : "106 Л.C",
            "Коробка передач" : "Механика (МТ5)",
            "Привод": "Передний",
            "Год выпуска": 2023,
            "Цвет" : "Белый",
            "Цена (РУБ)" : 991000.0,
            "Доступна для продажи": True,},
            
            {"Модель" : "LADA Granta Drive Active",
            "Двигатель" : "106 Л.C",
            "Коробка передач" : "Механика (МТ5)",
            "Привод": "Передний",
            "Год выпуска": 2024,
            "Цвет" : "Черный",
            "Цена (РУБ)" : 990000.0,
            "Доступна для продажи": True},
            
            {"Модель" : "LADA Granta Drive SPORT",
            "Двигатель" : "120 Л.C",
            "Коробка передач" : "Механика (МТ5)",
            "Привод": "Передний",
            "Год выпуска": 2023,
            "Цвет" : "Синий",
            "Цена (РУБ)" : 1200000.0,
            "Доступна для продажи": False},
            
            {"Модель" : "LADA ВАЗ 2107",
            "Двигатель" : "89 Л.C",
            "Коробка передач" : "Механика (МТ5)",
            "Привод": "Задний",
            "Год выпуска": 2014,
            "Цвет" : "Багровый",
            "Цена (РУБ)" : 200000.0,
            "Доступна для продажи": True},
            
            {"Модель" : "LADA ВАЗ 2114",
            "Двигатель" : "98 Л.C",
            "Коробка передач" : "Механика (МТ5)",
            "Привод": "Передний",
            "Год выпуска": 2012,
            "Цвет" : "Серебристый",
            "Цена (РУБ)" : 290000.0,
            "Доступна для продажи": True},
            
            {"Модель" : "LADA Niva Travel",
            "Двигатель" : "119 Л.C",
            "Коробка передач" : "Механика (МТ5)",
            "Привод": "Полный",
            "Год выпуска": 2022,
            "Цвет" : "Белый",
            "Цена (РУБ)" : 1090000.0,
            "Доступна для продажи": True},
            
            {"Модель" : "LADA Надежда",
            "Двигатель" : "129 Л.C",
            "Коробка передач" : "Механика (МТ5)",
            "Привод": "Полный",
            "Год выпуска": 2005,
            "Цвет" : "Черный",
            "Цена (РУБ)"  : 550000.0,
            "Доступна для продажи": False},
            
            {"Модель" : "LADA ВАЗ 2106",
            "Двигатель" : "76 Л.C",
            "Коробка передач" : "Механика (МТ4)",
            "Привод": "Задний",
            "Год выпуска": 2006,
            "Цвет" : "Коричневый",
            "Цена (РУБ)": 150000.0,
            "Доступна для продажи": True},
            
            {"Модель" : "LADA Niva Бронто",
            "Двигатель" : "130 Л.C",
            "Коробка передач" : "Механика (МТ5)",
            "Привод": "Полный",
            "Год выпуска": 2021,
            "Цвет" : "Темно-зеленый",
            "Цена (РУБ)" : 1300000.0,
            "Доступна для продажи": False},
            
            {"Модель" : "LADA Largus универсал",
            "Двигатель" : 101,
            "Коробка передач" : "Механика (МТ5)",
            "Привод": "Передний",
            "Год выпуска": 2019,
            "Цвет" : "Белый",
            "Цена (РУБ)" : 650000.0,
            "Доступна для продажи": True}]

def print_cars_model_user(cars):

    count = 0 
    
    print()
    for i in cars:
        for key, value in i.items():
            if key == "Модель":
                count += 1
                print(f"{count}. {key}:  {value}", end="\n\n")

    print("Для того, чтобы вернуться в главное меню")
    
    functions.clear()

    functions.function_user()


def print_cars_model_admin(cars):

    count = 0 
    
    print()
    for i in cars:
        for key, value in i.items():
            if key == "Модель":
                count += 1
                print(f"{count}. {key}:  {value}", end="\n\n")

    print("Для того, чтобы вернуться в главное меню")
    
    functions.clear()

    functions.function_admin()


#print_sorted(user_text="Сортировка от меньшего к большему", sorted_cars=sorted(cars, key=lambda price: price["Цена (РУБ)"]))


def sorted_cars():
    

    while True:
        try:
            print()
            print("""Выберите метод сортировки, методы указаны ниже:
1. От меньшего к большему (сортировка по цене)
2. От большего к меньшему (сортировка по цене)
3. Сортировка по годам выпуска""",end='\n\n')

            user_sort = int(input())

            if user_sort == 1:

                print_sorted(user_text="Сортировка от меньшего к большему:", sorted_cars=sorted(cars, key=lambda price: price["Цена (РУБ)"]))
                functions.clear()

                functions.function_user()
                break

            elif user_sort == 2:

                print_sorted(user_text="Сортировка от большего к меньшему:", sorted_cars=sorted(cars, key=lambda price: price["Цена (РУБ)"], reverse=True))
                
                functions.clear()

                functions.function_user()
                break

            elif user_sort == 3:

                print_sorted(user_text="Сортировка по годам выпуска:", sorted_cars=sorted(cars, key=lambda years: years["Год выпуска"]))

                functions.clear()

                functions.function_user()
                break

            else:
                print("Не корректное значение!!!")

                functions.clear()


        except Exception as error:
            print(f"Ошибка: {error}")

            functions.clear()
