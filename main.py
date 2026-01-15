from broodcode_modules.broodcode import menu
from broodcode_modules.calculate_sandwiches import fetch_orders
from BroodCodeCore.about import get_full_info
from BroodCodeCore.pickle_storage import delete_all_pickles
from BroodCodeCore.fetch import fetch_menu
from BroodCodeCore.filter import get_vegan_sandwiches, get_sandwich_by_ingredients, get_ingredients_by_sandwich
from BroodCodeCore.prices import calculate_price

APP_VERSION = "3.1.0"

def about():
    app_name = "BroodCode"
    author = "Frank van Viegen"
    maintainers = ["Yirnick van Dijk", "Tal Perets"]

    print(f"""
    {app_name}:
    Author: {author}
    Maintainer(s): {maintainers[0]}, {maintainers[1]}
    Version: {APP_VERSION}
    
    BroodCode versions 3.0.0 or higher are powered by:
    {get_full_info()}
    """)

def main():
    print(f"Welcome to the broodcode mass order system version { APP_VERSION }. Please select one of the following options")
    while True:
        print("""
            1. Show the menu
            2. Calculate ordered sandwiches
            3. Delete menu cache
            4. Show (possible) vegan sandwiches
            5. Show sandwiches by ingredients
            6. About BroodCode
            7. Exit
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
                delete_all_pickles()
            case 4:
                print("")
                current_menu = fetch_menu()
                sandwiches = calculate_price(current_menu["sandwiches"], current_menu["breadtypes"], "sandwiches")
                vegan_sandwiches = get_vegan_sandwiches(sandwiches)
                for sandwich in vegan_sandwiches:
                    print(sandwich)
            case 5:
                print("")
                ingredient = input("Fill in an ingredient so see which sandwiches have that ingredient: ")
                current_menu = fetch_menu()
                sandwiches = calculate_price(current_menu["sandwiches"], current_menu["breadtypes"], "sandwiches")
                sandwich_by_ing = get_sandwich_by_ingredients([ingredient], sandwiches)
                for sandwich in sandwich_by_ing:
                    print(sandwich["sandwich"])
            case 6:
                about()
            case 7:
                exit()
            case _:
                print("This number does not have an available option. please try another one")

main()