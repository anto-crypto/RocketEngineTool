import math
from utils.tools import (
    time_points
)
from utils.costants import gravity
G0 = gravity['Earth']


#Static rocket calculations
def mass_flow_rate(propellant_mass, burn_time):
    return propellant_mass / burn_time

def effective_exhaust_velocity(specific_impulse):
    return specific_impulse * G0

def thrust(propellant_mass, burn_time, specific_impulse):
    m = mass_flow_rate(propellant_mass, burn_time)
    return m * specific_impulse * G0

def total_impulse(propellant_mass, burn_time, specific_impulse):
    t = thrust(propellant_mass, burn_time, specific_impulse)
    return t * burn_time

def delta_v(specific_impulse, dry_mass, propellant_mass):
    return specific_impulse * G0 * math.log((dry_mass + propellant_mass) / dry_mass)

def t_w(propellant_mass, burn_time, specific_impulse, dry_mass, g_x):
    t = thrust(propellant_mass, burn_time, specific_impulse)
    return t / ((dry_mass + propellant_mass) * g_x)


#Time domain model
def mass_at_time(propellant_mass, dry_mass, burn_time, time):
    if time <= burn_time:
        m = mass_flow_rate(propellant_mass, burn_time)
        m0 = propellant_mass + dry_mass
        value = m0 - m * time
    else:
        #value = dry mass
        value = dry_mass
    return value

def t_w_t(propellant_mass, burn_time, specific_impulse, dry_mass, time):
    if time <= burn_time:
        t_w = propellant_mass * specific_impulse / (burn_time * mass_at_time(propellant_mass, dry_mass, burn_time, time))
    else:
        t_w = propellant_mass * specific_impulse / (burn_time * mass_at_time(propellant_mass, dry_mass, burn_time, burn_time))
    return t_w

