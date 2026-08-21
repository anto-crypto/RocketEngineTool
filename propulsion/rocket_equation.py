import math
from utils.tools import (
    time_points
)

def mass_flow_rate(propellant_mass, burn_time):
    return propellant_mass / burn_time

def effective_exhaust_velocity(specific_impulse, g_x):
    return specific_impulse * g_x

def thrust(propellant_mass, burn_time, specific_impulse, g_x):
    m = mass_flow_rate(propellant_mass, burn_time)
    return m * specific_impulse * g_x

def total_impulse(propellant_mass, burn_time, specific_impulse, g_x):
    t = thrust(propellant_mass, burn_time, specific_impulse, g_x)
    return t * burn_time

def delta_v(specific_impulse, dry_mass, propellant_mass, g_x):
    return specific_impulse * g_x * math.log((dry_mass + propellant_mass) / dry_mass)

def t_w(propellant_mass, burn_time, specific_impulse, dry_mass, g_x):
    t = thrust(propellant_mass, burn_time, specific_impulse, g_x)
    return t / ((dry_mass + propellant_mass) * g_x)

def mass_at_time(propellant_mass, dry_mass, burn_time):
    m = mass_flow_rate(propellant_mass, burn_time)
    m0 = propellant_mass + dry_mass
    time_l = time_points(burn_time)
    m_t = dict()
    for i in time_l:
        value = m0 - m * i
        m_t[i] = value
    return m_t

