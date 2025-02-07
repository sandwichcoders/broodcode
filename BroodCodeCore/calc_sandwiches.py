from collections import defaultdict
from BroodCodeCore.pickle_storage import read_from_pickle
from BroodCodeCore.prices import _format_price

opened_pickles = []

def calculate_sandwiches(orders: str, pickles: list):
    """Calculate the ordered sandwiches

    :param orders: name of the .txt file containing the orders
    :param pickles: list of names of the pickles used to calculate the sandwiches with
    :return: A dict of counted products from the orders categorised
    """
    calculated_orders = {}

    try:
        with open(f"{orders}.txt") as file:
            lines = [line.strip() for line in file.readlines() if line.strip()]
    except FileNotFoundError:
        print(
            "\033[31mCORE ERROR AT 'calc_sandwiches.py' IN 'calculate_sandwiches()':\nCreate a text file with orders with a single order per line, or delete the pickles for a new order round.\033[0m"
        )
        return

    for pickle in pickles:
        opened_pickle = read_from_pickle(pickle)
        calculated_orders[pickle] = _sum_up_sandwiches(lines, opened_pickle)

    return calculated_orders

def _sum_up_sandwiches(lines, data):
    """Sum up ordered sandwiches

    :param lines: The prices people paid for their order
    :param data: The data in the opened pickle
    :return: A dict of counted products from the orders
    """
    totals = {"profit": 0, "count": 0}
    orders = defaultdict(lambda: defaultdict(int))
    paid_orders = [_format_price(int(line)) for line in lines]

    for order in paid_orders:
        if order in data["codes"]:
            title, bread_type, profit = data["codes"][order]
            orders[title][bread_type] += 1
            totals["profit"] += profit
            totals["count"] += 1

    return orders