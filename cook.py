from time import sleep

def water_starts_boiling() -> bool:
    """ Checks if the water starts to boil or not """
    return True


def water_is_boiling() -> bool:
    """ Cecks if the water is boiling or not """
    return True

def wait_x_minutes(x:int) -> bool:
    """ 'Waits' x minutes for something """
    for i in range(x):
        sleep(1)
        if i == 0:
            print(f"warte {i+1} Minute.")
            continue
        print(f"warte {i+1} Minuten.")
    return True
