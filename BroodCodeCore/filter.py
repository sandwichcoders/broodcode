SANDWICH_TYPING = dict[str, tuple[str, str, int, str]]

def get_sandwich_by_ingredients(ingredients: list, sandwiches: SANDWICH_TYPING):
    """
    Get sandwiches by the ingredients they contain
    Args:
        ingredients: The ingredients the sandwiches may contain
        sandwiches: List of sandwiches to pick from

    Returns: A list of sandwiches which contains the given ingredients
    """
    found_sandwiches = []

    for ingredient in ingredients:
        for sandwich in sandwiches.values():
            if found_sandwiches and found_sandwiches[-1]["sandwich"] == sandwich[0]:
                continue
            sandwich_ing = sandwich[-1].replace(",", "")
            sandwich_ing = sandwich_ing.split(" ")

            if ingredient in sandwich_ing:
                found_sandwiches.append({'sandwich': sandwich[0], 'ingredients': sandwich[-1]})

    if 0 == len(found_sandwiches):
        found_sandwiches.append(None)

    return found_sandwiches


def get_ingredients_by_sandwich(price_code: str, sandwiches: SANDWICH_TYPING):
    """
    Get the ingredients of a sandwich based on their price code
    Args:
        price_code: The price code of the sandwich
        sandwiches: List of sandwiches to pick from

    Returns: The sandwich and it's ingredients
    """
    if '.' in price_code:
        price_code = price_code.replace(".", ",")
        print("Oki")
    try:
        sandwich = {"sandwich": sandwiches[price_code][0], "ingredients": sandwiches[price_code][-1]}
    except KeyError:
        print("\033[33mCORE WARNING AT 'filter.py' IN 'get_ingredients_by_sandwich()':\nSandwich not found. Did you enter the correct price code?\033[0m")
        return None

    return {"sandwich": sandwiches[price_code][0], "ingredients": sandwiches[price_code][-1]}

def get_vegan_sandwiches(sandwiches: SANDWICH_TYPING) -> list:
    """
    Return a list of (possible) vegan sandwiches.
    Args:
        sandwiches: Available price calculated sandwiches

    Returns: A list of (possible) vegan sandwiches
    """
    vegan_sandwiches = []

    for sandwich in sandwiches.values():
        if sandwich[0] in vegan_sandwiches or f'{sandwich[0]} (Can be made vegan on request)' in vegan_sandwiches:
            continue

        title = sandwich[0].split(" ")
        subtitle = sandwich[-1].split(" ")
        if _is_word(title, "(vegan)"):
            vegan_sandwiches.append(sandwich[0])
        elif _is_word(subtitle, "vegan?"):
            vegan_sandwiches.append(f'{sandwich[0]} (Can be made vegan on request)')

    return vegan_sandwiches


def _is_word(sentence, bounty):
    """
    Check if a given word appears in a given sentence
    Args:
        sentence: The sentence to look into
        bounty: The word to look for

    Returns: True if the word was found. False if not.
    """
    for word in sentence:
        if word.lower() == bounty:
            return True
    return False