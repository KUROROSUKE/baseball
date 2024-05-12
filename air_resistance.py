import math

def air_resistance(radius,velocity,resis_coeff = 0.35 ,air_density = 1.225):
    """
    Args:
        radius : int or float type. unit is "m".
        velocity : int or float type. unit is "m/s".
        resis_coeff : int or float type. Defaults is 0.35.
        air_density : int or float type. unit is "kg/m^3". Defaults is 1.225.

    Returns:
        Force: float (or int) type.
    
    This function is based on the "DragForce".
    """
    Force = resis_coeff * air_density * 4 * math.pi * radius * pow(velocity,2)
    return Force
