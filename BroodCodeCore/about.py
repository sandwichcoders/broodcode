NAME = "BroodCode Core"
AUTHOR = "Yirnick van Dijk"
VERSION = "1.1.1"

def get_full_info():
    """Get the full information about the BroodCode Core

    Returns: the name, author and version of the BroodCode Core as a string

    """
    return f"{NAME} by {AUTHOR}. Version {VERSION}"

def get_name():
    """Get the name of the software

    :return: The name of the software
    """
    return NAME

def get_author():
    """Get the author's name

    :return: The author's name
    """
    return AUTHOR

def get_version():
    """Get the software's version number

    :return: The software's version number
    """
    return VERSION