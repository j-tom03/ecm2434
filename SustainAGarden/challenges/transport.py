import re
import what3words
from geopy.distance import geodesic


def validate_format(data) -> bool:
    match = re.match(r"^([A-Za-z]+(\.[A-Za-z]+)+)$", data)
    if match is None:
        return False
    return True


def get_distance(start, end) -> (float, int):
    print("get distance")
    geocoder = what3words.Geocoder("COLQ41FP")
    start = geocoder.convert_to_coordinates(start)
    if "error" in start:
        print(f"start: {start}")
        return start["error"]["code"], start["error"]["message"]
    end = geocoder.convert_to_coordinates(end)
    if "error" in end:
        print(f"end: {end}")
        return end["error"]["code"], end["error"]["message"]

    start = (start["coordinates"]["lng"], start["coordinates"]["lat"])
    end = (end["coordinates"]["lng"], end["coordinates"]["lat"])

    print(start)
    print(end)

    return geodesic(start, end).km

