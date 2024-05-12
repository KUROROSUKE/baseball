import math
from air_resistance import air_resistance
from gravity import gravity
import matplotlib.pyplot as plot

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