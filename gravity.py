import math

def gravity(time,gravity = 9.8):
    """
    Args:
        time : int or float type. input elapsed time.
        gravity : int or float type. gravitational acceleration. Defaults to 9.8.

    Returns:
        Force: float (or int) type.
    
    This function based on the "Newton's universal gravitation".
    """
    
    Force = gravity * time
    return Force