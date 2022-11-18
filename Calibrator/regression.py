import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


def plot_points(y, y_unc, x, x_unc):
    style = "seaborn-v0_8-darkgrid"
    plt.style.use(style)
    plt.xlabel("Channel")
    plt.ylabel("Energy [KeV]")
    plt.errorbar(x, y, xerr = x_unc, yerr = y_unc, label = "Energy vs Channel", fmt = "o")
    plt.legend()


# Place the midpoints of the tops in the spectrums, and their corresponding energies
channels = np.array([460, 360, 137.5, 174.5, 212.5, 258, 427.5])
energies = np.array([661, 511, 187  , 242  , 295  , 353  , 609])


# Use least squares to find best line
def squares_method(y, y_unc, x):
    weights     = 1 / (y_unc ** 2)
    sum_weights = np.sum(weights)
    sum_xy      = np.sum(x * y * weights)
    sum_x       = np.sum(x * weights)
    sum_x2      = np.sum(x ** 2 * weights)
    sum_y       = np.sum(y * weights)

    D = sum_weights * sum_x2 - sum_x ** 2
    slope = (sum_weights * sum_xy - sum_x * sum_y) / D
    const = (sum_x2 * sum_y - sum_xy * sum_x) / D
    slope_unc = np.sqrt(sum_weights / D)
    const_unc = np.sqrt(sum_x2 / D)
    print("Slope estimate is ", np.round(slope * 10 ** 15, 4) / 10 ** 15, " +/- ", np.round(slope_unc * 10 ** 15, 4) / 10 ** 15)
    print("Constant estimate is ", np.round(const, 4), " +/- ", np.round(const_unc, 4))
    
    y_pred = slope * y + const
    diff = y_pred - y
    err = (diff / y_unc) ** 2
    chi2 = np.sum(err)
    print("The Chi Squares is ", chi2)

    return slope, slope_unc, const, const_unc


slope, slope_unc, const, const_unc = squares_method(energies, np.array([1 for i in range(7)]), channels)



plot_points(energies, np.array([1 for i in range(7)]), channels, np.array([0.5 for i in range(7)]))
x = np.arange(np.min(channels), np.max(channels), (np.max(channels) - np.min(channels)) / 100)
y = (slope + 0) * x + (const + 0)
plt.plot(x, y, label = "Best fitting line")
y = (slope + slope_unc) * x + (const - const_unc)
plt.plot(x, y, label = "Best fitting line (+ slope_unc - const_unc)")
y = (slope - slope_unc) * x + (const + const_unc)
plt.plot(x, y, label = "Best fitting line (- slope_unc + const_unc)")
plt.legend()
plt.show()