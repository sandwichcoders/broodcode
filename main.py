from broodcode_modules.broodcode import menu
from broodcode_modules.calculate_sandwiches import fetch_orders
from BroodCodeCore.about import get_full_info
from BroodCodeCore.pickle_storage import delete_all_pickles

APP_VERSION = "3.0.0"

def about():
    app_name = "BroodCode"
    author = "Frank van Viegen"
    maintainers = ["Yirnick van Dijk", "Tal Perets"]

    print(f"""
    {app_name}:
    Author: {author}
    Maintainer(s): {maintainers[0]}, {maintainers[1]}
    Version: {APP_VERSION}
    
    BroodCode versions {APP_VERSION} or higher are powered by:
    {get_full_info()}
    """)

def main():
    print(f"Welcome to the broodcode mass order system version { APP_VERSION }. Please select one of the following options")
    while True:
        print("""
            1. Show the menu
            2. Calculate ordered sandwiches
            3. About BroodCode
            4. Delete all created pickles
            5. Exit
            """)
        while True:
            try:
                option = int(input("Make your choice: "))
                if option:
                    break
            except ValueError:
                print("That is not a number, Just type a number")

        match option:
            case 1:
                menu()
            case 2:
                fetch_orders()
            case 3:
                about()
            case 4:
                delete_all_pickles()
            case 5:
                exit() # request the sandwich ingredients in this option
            case _:
                print("This number does not have an available option. please try another one")

main()