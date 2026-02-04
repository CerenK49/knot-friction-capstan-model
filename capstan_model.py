import math
import numpy as np
def max_load_static(T_hold, mu, wraps):
    """
    Capstan static model:
    T_max = T_hold * exp(mu * theta)
    theta = 2*pi*wraps 
    """

    theta = 2*math.pi*wraps
    T_max = T_hold * math.exp(mu*theta)
    return T_max

def will_it_hold_static(m, g, T_hold, mu, wraps):
    """
    Static case:
    T_load = m*g
    T_max = max_load_statistic(...)
    koşul: T_load <= T_max
    """

    T_load = m*g
    T_max = max_load_static(T_hold, mu, wraps)
    ok = T_load <= T_max
    return ok, T_load, T_max

# ----- main program -----
m = float(input("mass m(kg):"))
g = 9.81
T_hold = float(input("The maximum tensile strength the holding party can withstand(N):"))
mu = float(input("friction coefficient mu:"))
wraps = float(input("number of wraps:"))

ok, T_load, T_max = will_it_hold_static(m, g, T_hold, mu, wraps)

print("\n--- RESULTS ---")
print(f"Mass: {m:.2f} kg")
print(f"T_load (mg)      = {T_load:.2f} N")
print(f"T_max (capstan)  = {T_max:.2f} N")

if ok:
    print("Decision: This capstan node holds this mass in a STATIC state.")
else:
    print("Desicion: With these parameters the node is INSUFFICIENT in the STATIC state, there is a risk of slippage.")


import matplotlib.pyplot as plt

def plot_wraps_vs_load(m, g, T_hold, mu):
    wraps_list = []
    Tmax_list = []

    # Explore in small steps, between 0 and 3 turns.
    w = 0.0
    while w <= 3.0:
        wraps_list.append(w)

        T_max = max_load_static(T_hold, mu, w)
        Tmax_list.append(T_max)

        w += 0.1   # steps (change it if you want)

    T_load = m * g

    plt.figure()
    plt.plot(wraps_list, Tmax_list, label="T_max (capstan)")
    plt.axhline(T_load, linestyle="--", label="T_load = mg")

    plt.xlabel("Number of wraps (wraps)")
    plt.ylabel("Tension (N)")
    plt.title("Capstan knot — static model")
    plt.grid(True)
    plt.legend()
    plt.show()
plot_wraps_vs_load(m, g, T_hold, mu)

