import time

from constants import FOLDER_NAMES


def print_time(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        print(
            f"\nExecution time: [{time.time() - start}] seconds, "
            f"average per website: [{(time.time() - start)/len(FOLDER_NAMES)}] seconds\n"
        )

    return wrapper
