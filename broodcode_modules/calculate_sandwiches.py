import pickle
from collections import defaultdict
from broodcode_modules.menu_props import get_max_widths, format_row, format_separator, print_header
from BroodCodeCore.calc_sandwiches import calculate_sandwiches


def print_pickle(data, header):
    totals = {"profit": 0, "count": 0}

    print_header(header)

    # Prepare data for table rows
    rows = [["Sandwich", "Type", "Quantity"]]

    for product in data:
        for bread_type in data[product]:
            # Add row to rows list
            rows.append(
                [
                    product,
                    bread_type.lower(),
                    str(data[product][bread_type]),
                ]
            )

    col_widths = get_max_widths(
        rows
    )  # Calculate column widths based on max string length in each column

    # Print the table
    print(format_row(rows[0], col_widths))  # Print header row
    print(format_separator(col_widths))  # Print separator
    for row in rows[1:]:
        print(format_row(row, col_widths))  # Print data rows

    print(f"\n{totals['count']} sandwiches. {totals['profit']} cents profit!")
    print("")


def open_pickle(filename):
    try:
        with open(f"./pickles/{filename}.pickle", "rb") as file:
            data = pickle.load(file)
    except FileNotFoundError:
        return False
    return data


def fetch_orders():
    orders = calculate_sandwiches("orders", ["sandwiches", "paninis", "special"])

    print("COPY BLOCK")

    profit_sandwiches = None
    profit_paninis = None
    profit_specials = None
    
    for index, pickle in enumerate(orders):
        messages = ["Freshly topped sandwiches", "Paninis", "Special of the Week"]
        print_pickle(orders[pickle], messages[index])

    print("Don't forget to copy the sentence below to put in the notes on the order summary screen:")
    print("'Graag, als dit mogelijk is, de broodsoorten op de zakken schrijven b.v.d.'")

    print("/COPY BLOCK")
    print()

    if profit_sandwiches:
        print(f"Average sandwich profit: {profit_sandwiches} cents per sandwich")
    if profit_paninis:
        print(f"Average panini profit: {profit_paninis} cents per panini")
    if profit_specials:
        print(f"Average special profit: {profit_specials} cents per special")
