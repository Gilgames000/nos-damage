import json
import logging

from datastructs import Entity


def load_entities(folder="entities"):
    from glob import glob
    entity_filenames = glob(f"{folder}/*.json")
    entities = [ps.load_entity(filename=fn) for fn in entity_filenames]

    return entities


def save_entity(entity, filename):
    save_dataclass(entity.to_dict(), filename)


def load_entity(filename, update_name=True):
    d = load_dataclass(filename)
    if update_name:
        from os.path import basename, splitext
        d["name"] = splitext(basename(filename))[0]
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
