import math
G0 = 9.80665

def mass_flow_rate(propellant_mass, burn_time):
    return propellant_mass / burn_time

def effective_exhaust_velocity(specific_impulse):
    return specific_impulse * G0

def thrust(propellant_mass, burn_time, specific_impulse):
    m = mass_flow_rate(propellant_mass, burn_time)
    return m * specific_impulse * G0

def total_impulse(propellant_mass, burn_time, specific_impulse):
    m = mass_flow_rate(propellant_mass, burn_time)
    t = m * specific_impulse * G0
    return t * burn_time

def delta_v(specific_impulse, dry_mass, propellant_mass):
    return specific_impulse * G0 * math.log((dry_mass + propellant_mass) / dry_mass)

def t_w(propellant_mass, burn_time, specific_impulse, dry_mass):
    m = mass_flow_rate(propellant_mass, burn_time)
    t = m * specific_impulse * G0
    return t / ((dry_mass + propellant_mass) * G0)

