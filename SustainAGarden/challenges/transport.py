import re
import what3words
from geopy.distance import geodesic


def validate_format(data) -> bool:
    match = re.match(r"^([A-Za-z]+(\.[A-Za-z]+)+)$", data)
    if match is None:
        return False
    return True


def get_distance(start, end) -> (float, int):
    geocoder = what3words.Geocoder("UQK40B3T")
    start = geocoder.convert_to_coordinates(start)
    if "error" in start:
        return start["error"]["code"], start["error"]["message"]
    end = geocoder.convert_to_coordinates(end)
    if "error" in end:
        return end["error"]["code"], end["error"]["message"]

    return geodesic(start, end).km

