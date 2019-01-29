from time import time


def generate_filename():
    return str(int(time() * 10 ** 6))
