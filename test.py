import math

A = 1
omega = 0.5
dt = 0.1
phi_0 = -0.7

x1 = lambda t: -A*math.sin(omega * t + phi_0)
x2 = lambda t: A*math.sin(omega * t + phi_0)

t = 0
theta_0 = 0
theta = theta_0
prev_diff = x2(t) - x1(t)
curr_diff = prev_diff
max_diff = None
max_diff_theta = None
while True:
    # take time step
    t += dt
    theta += omega * dt
    prev_diff = curr_diff
    curr_diff = x2(t) - x1(t)

    delta_diff = curr_diff - prev_diff
    print(f't = {t}\ntheta={theta}\ndelta_diff = {delta_diff}\n')

    # cases
    if delta_diff > 0:
        pass
    elif delta_diff < 0:
        print('STOP')
        break


