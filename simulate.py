import math
import matplotlib.pyplot as plot

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

def simulate(velocity,angle,radius,mass):
    """
    Args:
        velocity : int or float type. unit is "m/s".
        angle : int or float type. unit is "Deg".
        radius : radius of ball. unit is "m".
        mass : mass of ball. unit is "g".

    Returns:
        tuple : orbit of ball to x,y.
    """
    x = 0.0
    y = 1.0
    time = 0
    x_history = []
    y_history = []
    angle = math.radians(angle)
    while y > 0:
        x_history.append(x)
        y_history.append(y)
        x_speed = math.cos(angle) * velocity
        y_speed = math.sin(angle) * velocity
        angle = math.atan2(y_speed , x_speed)
        x = x + x_speed - air_resistance(radius,velocity) / mass
        y = y + y_speed - math.copysign(air_resistance(radius,velocity) / mass , y_speed) - gravity(time)
        time += 0.1
    x_history.append(x)
    y_history.append(y)
    return x_history,y_history


x_orbit,y_orbit = simulate(50,45,0.05,128)

plot.plot()
for i in range(len(x_orbit)):
    plot.scatter(x_orbit[i], y_orbit[i]) #ここ汚い
plot.show()