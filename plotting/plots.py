import matplotlib.pyplot as plt
from utils.tools import time_points
from propulsion.rocket_equation import (
    mass_flow_rate,
    thrust,
    mass_at_time
)





def thrust_time_graphic(burn_time, propellant_mass, specific_impulse, g_x):
    time = time_points(burn_time)
    thrust_l = []
    for i in time:
        t = thrust(propellant_mass, burn_time, specific_impulse, g_x)
        thrust_l.append(t)

    plt.plot(time, thrust_l)
    plt.xlabel('Time')
    plt.ylabel('Thrust')
    plt.title('Thrust - Time')
    plt.grid(True)
    plt.show()

def remaining_mass_time(dry_mass, propellant_mass, burn_time):
    time = time_points(burn_time)
    mass_l = []
    m_t = mass_at_time(propellant_mass, dry_mass, burn_time)
    for i in time:
        m = m_t[i]
        mass_l.append(m)

    plt.plot(time, mass_l)
    plt.xlabel('Time')
    plt.ylabel('Remaining Mass')
    plt.title('Remaining Mass - Time')
    plt.grid(True)
    plt.show()


def thrust_to_weight_time(burn_time, propellant_mass,dry_mass, specific_impulse, g_x):
    time = time_points(burn_time)
    tw_l = []
    m_t = mass_at_time(propellant_mass, dry_mass, burn_time)
    for i in time:
        t = thrust(propellant_mass, burn_time, specific_impulse, g_x)
        m = m_t[i]
        tw = t / (m * g_x)
        tw_l.append(tw)
    
    plt.plot(time, tw_l)
    plt.xlabel('Time')
    plt.ylabel('T/W')
    plt.title('Thrust to Weight - Time')
    plt.grid(True)
    plt.show()

