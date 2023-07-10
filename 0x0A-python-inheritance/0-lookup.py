#!/usr/bin/python3
"""
module with class base-geometry
"""

class Basegeometry:
    """method for calculated area"""
    raise Exception("area() is not implemented")

def integer_validator(self, name, value):
    """Method for validate if a num is integer"""

    if type(value) is not int:
        raise TypeError("{} must be an integer". format(name))
    if value <= 0:
        raise ValueError("{} must be grater than 0". format(name))
