from propulsion.rocket_equation import (
    mass_flow_rate,
    effective_exhaust_velocity,
    thrust,
    total_impulse,
    delta_v,
    t_w,
    mass_at_time
)


def test_mass_flow_rate():
    result = mass_flow_rate(20, 5)
    assert result == 4

def test_effective_exhaust_velocity():
    result = effective_exhaust_velocity(250)
    assert abs(result - 2451.6625) < 0.001

def test_thrust():
    result = thrust(20, 5, 250)
    assert abs(result - 9806.65) < 0.001

def test_total_impulse():
    result = total_impulse(20, 5, 250)
    assert abs(result - 49033.25) < 0.001

def test_delta_v():
    result = delta_v(250, 10, 20,)
    assert abs(result - 2693.427) < 0.001

def test_t_w():
    result = t_w(20, 5, 250, 10, 9.80665)
    assert abs(result - 33.333333) < 0.001

def test_mass_at_time():
    result = mass_at_time(20, 10, 5, 0)
    assert abs(result - 30) < 0.001

