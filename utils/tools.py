def time_points(burn_time):
    l = []
    i = 0
    while i < burn_time:
        l.append(i)
        i += 0.01
    l.append(burn_time)
    return l

def opening():

    #Title
    name = 'RocketEngineTool v0.1'
    length = len(name)
    print('=' * (10 + length))
    print(' ' * 4, name, ' ' * 6)
    print('=' * (10 + length))

def control_element(prompt):
    while True:
        try:
            element = float(input(prompt))
            if element > 0:
                break
            else:
                print('Error! Please enter a positive number.')
                continue
        except ValueError:
            print('Error! Please enter a number.')
    return element

def select_gravity():
    from utils.costants import gravity

    print()
    print('Environment gravity')
    print('1 - Earth')
    print('2 - Mars')
    print('3 - Moon')
    print()

    #Cheking the environment
    while True:
        try:
            environment = int(input('Select the environment for the gravity: '))
        except ValueError:
            print('Error! Please chose one of the numbers requested.')
            continue
            

        #Checking the G
        if environment == 1:
            g_x = gravity['Earth']
            break
        elif environment == 2:
            g_x = gravity['Mars']
            break
        elif environment == 3:
            g_x = gravity['Moon']
            break
        else:
            print('Chose a number between 1 to 3.')

    return g_x

