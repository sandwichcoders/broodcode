def check_breadtypes(breadtypes: str):
    """
    Check if the breadtypes is not empty and fix it when there is at least not an array detected
    :param breadtypes: jsonified string of the breadtypes list
    :return:
    """
    if breadtypes == "":
        return "[]"
    return breadtypes