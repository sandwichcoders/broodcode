from pickle import load, dump
from os import path, remove, makedirs, listdir

pickle_path = "./BroodCodeCore/storage/pickles/"

def store_to_pickle(pickle_name: str, data, overwrite: bool = True):
    """Store data to a pickle

    Args:
        pickle_name (str): the name the file will be given
        data (any): The data the user wants to store
        overwrite (bool): Overwrite pickle by standard unless False is given as a parameter
    """
    if not path.exists(pickle_path):
        makedirs(pickle_path)

    if not overwrite:
        pickle_data = read_from_pickle(pickle_name)
        if pickle_data:
            pickle_data.append(data)
        else:
            pickle_data = [data]
        data = pickle_data

    with open(f"{pickle_path}{pickle_name}.pickle", "wb") as file:
        # noinspection PyTypeChecker
        dump(data, file)

def read_from_pickle(pickle_name: str):
    """Read the data from a specific pickle

    Args:
        pickle_name (str): The name of the pickle file to read from

    Returns:
        any: The stored data in the pickle
    """
    try:
        with open(f"{pickle_path}{pickle_name}.pickle", "rb") as file:
            data = load(file)
    except FileNotFoundError:
        print("\033[33mCORE WARNING AT 'pickle_storage.py' IN 'read_from_pickle()':\nPickle has not been found. Did you gave up the right file name?\033[0m")
        return False
    return data

def delete_pickles(pickles: list):
    """Delete a list of pickles

    Args:
        pickles (list): A list of pickle file names to delete the pickle files from
    """
    for pickle in pickles:
        if path.exists(f"{pickle_path}{pickle}.pickle"):
            remove(f"{pickle_path}{pickle}.pickle")
        else:
            print("\033[33mCORE WARNING AT 'pickle_storage.py' IN 'delete_pickles()': The file does not exist\033[0m")

def delete_all_pickles():
    """Delete all pickles in the pickle storage folder at once
    """
    try:
        files = listdir(pickle_path)
        for file in files:
            file_path = path.join(pickle_path, file)
            if path.isfile(file_path):
                remove(file_path)
        print("CORE INFO: All pickle files have been succesfully deleted")
    except:
        print("\033[33mCORE WARNING AT 'pickle_storage.py' IN 'delete_all_pickles()': Cannot delete pickle files. These might already have been deleted\033[0m")
