#!/bin/bash/python3


import math
import sys


def dist(gps: tuple, coords: tuple) -> float:
    """Calculates the distance between the GPS and the target coords.

    Args:
        gps (tuple): GPS coords tuple
        cords (tuple): Target coords tuple

    Raises:
        Exception: Couldn't calculate the distance

    Returns:
        float: distance
    """
    try:
        return (math.sqrt(math.pow(gps[0] - coords[0], 2) +
                math.pow(gps[1] - coords[1], 2) +
                math.pow(gps[2] - coords[2], 2)))
    except Exception:
        raise Exception("Failed to calculate distance.")


def parse_coords(string: str) -> tuple:
    """Parse the given coords in a string (format: "1,2,3")

    Args:
        string (str): String to parse

    Raises:
        Exception: Couldn't parse (ValueError ?)

    Returns:
        tuple: Parsed coords as a tuple
    """
    try:
        coords = tuple()  # Creating base tuple
        for arg in string.split(","):  # For each parsed arg
            coords = coords + (int(arg),)  # Adding parsed arg to the tuple
        return (coords)
    except Exception as e:
        raise Exception(f"Error while parsing : {e}")


print("=== Game Coordinate System ===\n")
gps_pos = (10, 20, 5)
origin = (0, 0, 0)
print(f"Position created: {gps_pos}")
print(f"Distance between {origin} and {gps_pos}: {dist(gps_pos, origin):.2f}")
print("")
print(f"Parsing coordinates : \"{sys.argv[1]}\"")
try:
    coords = parse_coords(sys.argv[1])
except Exception as e:
    print("Error:", e)

print(f"Parsed position: {coords}")
print(f"Distance between {origin} and {coords}: {dist(origin, coords):.1f}")
print("")
print("Parsing invalid coords")
try:
    new_coords = parse_coords(sys.argv[2])
    print(f"New coords : {new_coords}")
except Exception as e:
    print("Error:", e)
print("")
print("Unpacking demo:")
print(f"Player at x={coords[0]}, y={coords[1]}, z={coords[2]}")
print(f"Coordinates: X={coords[0]}, Y={coords[1]}, Z={coords[2]}")
