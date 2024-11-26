import os
import user
import car
import menu
import admin

def clear():
    enter = input("Нажмите ENTER!")
    clear = lambda: os.system('cls')
    clear()

def function_user():

    menu_user = menu.main_menu_user()

    if menu_user == 1:
        car.print_cars_model_user(cars=car.cars)
    
    elif menu_user == 2:
        car.sorted_cars()

    elif menu_user == 3:
        user.car_characteristics(cars=car.cars) 

    elif menu_user == 4:
        user.buy_car(cars=car.cars)
    
    elif menu_user == 5:
        user.user_discount_car()

    elif menu_user == 6:
        user.filter_car()
    
    elif menu_user == 7:
        admin.come_back_menu()


def function_admin():

    menu_admin = menu.main_menu_admin()

    if menu_admin == 1:
        admin.add_car()

    elif menu_admin == 2:
        admin.delete_car()

    elif menu_admin == 3:
        admin.car.print_cars_model_admin(cars=car.cars)

    elif menu_admin == 4:
        admin.sum_price_car()
    
    elif menu_admin == 5:
        admin.user_data()

    elif menu_admin == 6:
        admin.come_back_menu()
    
    
def function_start_menu():
    

    start_menu = menu.start_menu()


    if start_menu == 1:
        admin.avtorization_admin(3)

        function_admin()
        
    elif start_menu == 2:
        user.avtoriation_user()
        
        function_user()
