import re
# import what3words


def validate_format(data) -> bool:
    match = re.match("", data)
    if match is None:
        return False
    return True


def get_distance(start, end) -> (float, int):
    pass


def API_W3W():
    pass
