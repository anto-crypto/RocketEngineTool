def time_points(burn_time):
    l = []
    i = 0
    while i < burn_time:
        l.append(i)
        i += 0.5
    l.append(burn_time)
    return l

