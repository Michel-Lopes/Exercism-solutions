#Code to caculate expected time to bake a lasagna 

EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 2

def bake_time_remaining(elapsed_bake_time):
    """Calculate the bake time remaining.

    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """
    return EXPECTED_BAKE_TIME - elapsed_bake_time

def preparation_time_in_minutes(number_of_layers):
    """Calculate the preparation time

    :param number_of_layers: int number of layers of the lasagna.
    :return: int - time spent preparing the lasagna

    Function tha calculates the time spent adding extra layers to the lasagna.
    """
    return number_of_layers * PREPARATION_TIME

def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """Calculate elapsed in minutes.

    :param elapsed_bake_time: int - baking time already elapsed.
    :param number_of_layers: int - number of layers of the lasagna.
    :return: int elapsed_time_in_minutes preparing the lasagna.

    Function calculates the time elapsed cooking.
    """
    return preparation_time_in_minutes(number_of_layers) + elapsed_bake_time