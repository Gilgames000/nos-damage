import json
import logging

from datastructs import Entity


def save_attacker(attacker, filename):
    save_dataclass(attacker.to_dict(), filename)


def save_defender(defender, filename):
    save_dataclass(defender.to_dict(), filename)


def load_attacker(filename):
    d = load_dataclass(filename)
    return Entity.from_dict(d)


def load_defender(filename):
    d = load_dataclass(filename)
    return Entity.from_dict(d)


def save_dataclass(data, filename):
    try:
        logging.info(f"saving dataclass to {filename}")
        with open(filename, "w") as fp:
            json.dump(data, fp)
    except FileNotFoundError:
        logging.info(f"couldn't load dataclass from {filename}, file not "
                     f"found")


def load_dataclass(filename):
    data = {}
    try:
        logging.info(f"loading dataclass from {filename}")
        with open(filename, "r") as fp:
            data = json.load(fp)
    except FileNotFoundError:
        logging.info(f"couldn't load dataclass from {filename}, file not "
                     f"found")
    finally:
        return data
