import json
import logging
from urllib.request import urlopen


def retrieve_version(version_url="https://raw.githubusercontent.com/"
                                 + "Gilgames000/nos-damage/develop/"
                                 + "src/build/settings/base.json"):
    version = "0.0.0"
    try:
        with urlopen(version_url, timeout=5) as url:
            data = json.loads(url.read().decode())
            version = data["version"]
    except:
        logging.info(f"Failed to retrieve version from {version_url}")

    return version


def compute_version_number(version):
    version = version.split(".")
    return (
            int(version[0]) * 10 ** 4
            + int(version[1]) * 10 ** 2
            + int(version[2])
    )


def update_needed(version):
    current_version = compute_version_number(version)
    upstream_version = compute_version_number(retrieve_version())
    return current_version < upstream_version
