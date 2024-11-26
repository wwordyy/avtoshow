import functions

def logo_lada():
    print()

    print("  L          A       DDDD        A  ")
    print("  L         A A      D   D      A A ")
    print("  L        AAAAA     D   D     AAAAA")
    print("  L       A     A    D   D    A     A")
    print("  LLLLL  A       A   DDDDD   A       A")
    
    print()


def start_menu():

    
    while True:

        logo_lada()

        print("""Добро пожаловать в АВТОСАЛОН LADA! 🚘

    Как вы хотите авторизоваться?
    1. Администратор 💻
    2. Пользователь 🗿
    3. Выйти из автосалона ☹
    """)
        try:
            admin_or_user = int(input())
            if admin_or_user <= 2 and admin_or_user > 0:
                
                print("Теперь необходимо ввести свои данные!", end="\n\n")
                functions.clear()

                return admin_or_user
            
            elif admin_or_user == 3:
                print("Было приятно с вами иметь дело! 😉")

                break
            else:
                print("Выберите правильный диапозон!", end="\n\n")
                

        except Exception as error:
            print(f"Ошибка: {error}")
            print()
            functions.clear()

            
        


def main_menu_user():



    while True:
        try:
            logo_lada()
            print("""    1. Просмотреть полностью весь автосалон.
    2. Отсортировать машины.
    3. Узнать характеристики автомобиля.
    4. Купить машину.
    5. Просмотр авто со скидкой.
    6. Фильтрация.
    7. Вернуться в меню авторизации.""")
            user = int(input())
            if user > 0 and user <=7:
                return user
            
            else:
                print("Введите корректное значение!!!")

                functions.clear()

                logo_lada()

        except Exception as error:
            print(f"Ошибка: {error}")

            functions.clear()

            
    
def main_menu_admin():

    logo_lada()
    while True:

        try:
            print("""    1. Добавить машину.
    2. Удалить машину.
    3. Просмотр всех авто.
    4. Общая стоимость авто.
    5. Посмотреть данные о пользователях.
    6. Вернуться в меню авторизации.""")
            
            admin = int(input())

            if admin <= 6 and admin > 0:
                return admin

            else:   
                print("Введите корректные данные!!!")

                functions.clear()
        
        except Exception as error:
            print(f"Ошибка: {error}")

            functions.clear()

