from broodcode_modules.clippy import Clippy
from BroodCodeCore.fetch import fetch_menu
from BroodCodeCore.prices import calculate_price

FEE = 50

clippy = Clippy()
codes = {}
versions = []


def get_max_widths(rows):
    """Calculate maximum column width based on longest string in each column."""
    return [max(len(str(item)) for item in col) for col in zip(*rows, strict=False)]


def format_row(row_items, col_widths):
    """Format a row with variable column width based on longest content."""
    return (
        "|"
        + "|".join(f" {str(item):<{col_widths[i]}}" for i, item in enumerate(row_items))
        + "|"
    )


def format_separator(col_widths):
    """Create a separator row based on column widths for Markdown table."""
    return "|-" + "|-".join("-" * col_width for col_width in col_widths) + "|"


def print_header(title):
    clippy.c_print(f"## {title}\n")

def simplify_menu(products):
    simplified_menu = []
    product_and_prices = []
    for product in products:
        if "Special" in products[product][0]:
            continue

        if len(product_and_prices) == 6:
            simplified_menu += [product_and_prices]
            product_and_prices = []

        if len(product_and_prices) == 0:
            product_and_prices.append(products[product][0])

        product_and_prices.append(product)

    return simplified_menu


def build_sandwich_menu(menu):
    sandwich_price = calculate_price(menu["sandwiches"], menu["breadtypes"], "sandwiches", FEE)

    print_header("Freshly topped sandwiches")

    # Prepare data for table rows
    rows = [["Sandwich", "White", "Grain", "Foca", "Spelt", "G-Free"]]

    rows += simplify_menu(sandwich_price)

    col_widths = get_max_widths(
        rows
    )  # Calculate column widths based on max string length in each column

    # Print the table
    clippy.c_print("```")
    clippy.c_print(format_row(rows[0], col_widths))  # Print header row
    clippy.c_print(format_separator(col_widths))  # Print separator
    for row in rows[1:]:
        clippy.c_print(format_row(row, col_widths))  # Print data rows
    clippy.c_print("```\n")


def build_special_menu(menu):
    special_price = calculate_price(menu["special"], menu["breadtypes"], "special", FEE)

    print_header("Special of the Week")

    # Initialize row for the special menu
    keys = special_price.keys()
    row = [key for key in keys]

    # Only print the special title if we found a valid special
    if row:
        special_product = special_price[row[0]][0].split(" - ")
        clippy.c_print(special_product[1])  # clippy.c_print the special title
        # Prepare data for the Markdown table
        rows = [["Bread Type", "Price"]]
        for bread_type_id in [41, 42, 43, 44, 45]:
            bread_name = menu["breadtypes"][bread_type_id]["name"].title()
            price = row[bread_type_id - 41]  # Adjust for zero-indexing in the array
            rows.append([bread_name, price])

        col_widths = get_max_widths(
            rows
        )  # Calculate column widths based on max string length in each column

        # Print the table
        clippy.c_print("```")
        clippy.c_print(format_row(rows[0], col_widths))  # Print header row
        clippy.c_print(format_separator(col_widths))  # Print separator
        for r in rows[1:]:
            clippy.c_print(format_row(r, col_widths))  # Print data rows
        clippy.c_print("```\n")


def build_paninis_menu(menu):
    panini_price = calculate_price(menu["paninis"], menu["breadtypes"], "paninis", FEE)

    print_header("Panini's")

    # Prepare data for table rows
    rows = [["Panini", "Focaccia"]]

    for product in panini_price:
        # Initialize row with panini name
        row = [panini_price[product][0].strip()]
        row.append(product)
        # Add row to rows list
        rows.append(row)

    col_widths = get_max_widths(
        rows
    )  # Calculate column widths based on max string length in each column

    # Print the table
    clippy.c_print("```")
    clippy.c_print(format_row(rows[0], col_widths))  # Print header row
    clippy.c_print(format_separator(col_widths))  # Print separator
    for row in rows[1:]:
        clippy.c_print(format_row(row, col_widths))  # Print data rows
    clippy.c_print("```\n")


def menu():
    menu = fetch_menu()
    build_special_menu(menu)
    build_sandwich_menu(menu)
    build_paninis_menu(menu)
    clippy.copy_to_clipboard()

if __name__ == "__main__":
    menu()
