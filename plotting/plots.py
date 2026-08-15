import matplotlib.pyplot as plt
from utils.tools import time_points
from propulsion.rocket_equation import mass_flow_rate
from propulsion.rocket_equation import thrust

G0 = 9.80655




def thrust_time_graphic(burn_time, propellant_mass, specific_impulse):
    time = time_points(burn_time)
    thrust_l = []
    for i in time:
        t = thrust(propellant_mass, burn_time, specific_impulse)
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
    for i in time:
        m = dry_mass + propellant_mass - mass_flow_rate(propellant_mass, burn_time) * i
        mass_l.append(m)

    plt.plot(time, mass_l)
    plt.xlabel('Time')
    plt.ylabel('Remaining Mass')
    plt.title('Remaining Mass - Time')
    plt.grid(True)
    plt.show()


def thrust_to_weight_time(burn_time, propellant_mass,dry_mass, specific_impulse):
    time = time_points(burn_time)
    tw_l = []
    for i in time:
        t = thrust(propellant_mass, burn_time, specific_impulse)
        m = dry_mass + propellant_mass - mass_flow_rate(propellant_mass, burn_time) * i
        tw = t / (m * G0)
        tw_l.append(tw)
    
    plt.plot(time, tw_l)
    plt.xlabel('Time')
    plt.ylabel('T/W')
    plt.title('Thrust to Weight - Time')
    plt.grid(True)
    plt.show()

