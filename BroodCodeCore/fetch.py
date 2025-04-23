import requests
import json
from datetime import date
from BroodCodeCore.clippy import Clippy
clippy = Clippy()

def fetch_menu():
    """Fetch the menu from the Broodbode API

    :return: A raw but categorised and stripped version of the menu
    """
    try:
        response = requests.get(
            f"https://bestellen.broodbode.nl/v2-2/pccheck/null/{date.today()}/afhalen/8?cb=1695969466297",
            headers={
                "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:125.0) Gecko/20100101 Firefox/125.0"
            },
            timeout=10,  # Timeout after 10 seconds
        )
    except requests.exceptions.Timeout:
        clippy.c_print("\033[31mCORE ERROR: The request timed out. Please try again later.\033[0m")
        return {"products": [], "breadtypes": {}}
    except requests.exceptions.RequestException as e:
        clippy.c_print(f"\033[31mCORE ERROR: An error occurred: {e}\033[0m")
        return {"products": [], "breadtypes": {}}

    data = response.json()
    if 'errorMessage' in data:
        clippy.c_print(f"\033[31mCORE ERROR: Because Broodbode is closed, their API refuses to give the menu. Try again tomorrow.\033[0m")
        return {"products": [], "breadtypes": {}}
    products = data["products"]
    bread_types_by_id = {b["id"]: b for b in data["breadtypes"]}

    full_menu = {"products": products, "breadtypes": bread_types_by_id}

    return _strip_menu(full_menu)

def _strip_menu(full_menu):
    """ Strip and categorize the menu

    :param full_menu: The fully fetched menu
    :return: The categorized menu
    """
    menu_categories = ["special", "sandwiches", "paninis"]
    stripped_menu = []
    final_menu = {}

    for category in menu_categories:
        for product in sorted(full_menu["products"], key=lambda product: product["price"]):
            if len(json.loads(product["breadtypes"])) > 1 and category == "sandwiches":
                stripped_menu.append(product)
            if "special van de week" in product["title"].lower() and category == "special":
                stripped_menu.append(product)
                break
            if product["categorie_id"] == 71 and category == "paninis":
                stripped_menu.append(product)
        final_menu[category] = stripped_menu
        stripped_menu = []
    final_menu["breadtypes"] = full_menu["breadtypes"]
    return final_menu