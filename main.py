from utils.tools import (
    opening,
    control_element,
    select_gravity,
    time_points
)


def main():
    opening()

    propellant_mass = control_element('Propellant mass [kg]: ')
    dry_mass = control_element('Dry mass [kg]: ')
    specific_impulse = control_element('Specific impulse [s]: ')
    burn_time = control_element('Burn time [s]: ')
    g_x = select_gravity()

    from propulsion.rocket_equation import mass_flow_rate
    from propulsion.rocket_equation import effective_exhaust_velocity
    from propulsion.rocket_equation import thrust
    from propulsion.rocket_equation import total_impulse
    from propulsion.rocket_equation import delta_v
    from propulsion.rocket_equation import t_w
    from propulsion.rocket_equation import mass_at_time
    from propulsion.rocket_equation import t_w_t

    m = mass_flow_rate(propellant_mass, burn_time)
    e = effective_exhaust_velocity(specific_impulse)
    th = thrust(propellant_mass, burn_time, specific_impulse)
    to = total_impulse(propellant_mass, burn_time, specific_impulse)
    d = delta_v(specific_impulse, dry_mass, propellant_mass)
    tw = t_w(propellant_mass, burn_time, specific_impulse, dry_mass, g_x)

    print(f'Mass flow rate = {m:.3f} kg/s')
    print(f'Effective exhaust velocity = {e:.3f} m/s')
    print(f'Thrust = {th:.3f} N')
    print(f'Total impulse = {to:.3f} Ns')
    print(f'Delta v = {d:.3f} m/s')
    print(f'T/W = {tw:.3f}')

    time_list = time_points(burn_time)
    for i in time_list:
        m_t = mass_at_time(propellant_mass, dry_mass, burn_time, i)
        tw_t = t_w_t(propellant_mass, burn_time, specific_impulse, dry_mass, i)
        print(f't = {i:.2f} s   --->   {m_t:.2f} kg;   {th} N;   {tw_t:.2f}')

    from plotting.plots import thrust_time_graphic
    from plotting.plots import remaining_mass_time
    from plotting.plots import thrust_to_weight_time

    thrust_time_graphic(burn_time, propellant_mass, specific_impulse)
    remaining_mass_time(dry_mass, propellant_mass, burn_time)
    thrust_to_weight_time(burn_time, propellant_mass,dry_mass, specific_impulse, g_x)
    

if __name__ == '__main__':
    main()

