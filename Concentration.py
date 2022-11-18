import numpy as np

# reference
box_counts = np.sum(np.array([55150, 15478]))
bck_counts = np.sum(np.array([4729 , 1159 ]))
real_counts = box_counts - bck_counts
counts_unc = np.sqrt(box_counts + bck_counts)
print(np.round(real_counts, 3), np.round(counts_unc, 3))

conc = 4820
conc_unc = 20

t1 = 71.5
t2 = 28

disint = np.log(2) / 91.68
corr1 = np.exp((disint * t1))
corr2 = 1 - np.exp(-0.01133 * t2)


coeff = 2 * (conc * corr2) / (real_counts * corr1)
coeff_unc = (corr2 / corr1) * np.sqrt((conc_unc / real_counts) ** 2 + ((counts_unc * conc) / real_counts ** 2) ** 2)
print(np.round(coeff, 3), np.round(coeff_unc, 3))


# exposed box
box_counts = np.sum(np.array([4121, 1121]))
bck_counts = np.sum(np.array([1805, 520]))
real_counts = box_counts - bck_counts
counts_unc = np.sqrt(box_counts + bck_counts)
print(np.round(real_counts, 3), np.round(counts_unc, 3))

t1 = 72
t2 = 5

disint = np.log(2) / 91.68
corr1 = np.exp((disint * t1))
corr2 = 1 - np.exp(-0.01133 * t2)


conc_calc = (coeff * real_counts * corr1) / corr2
conc_calc_unc = (corr1 / corr2) * np.sqrt((coeff_unc * real_counts) ** 2 + (counts_unc * coeff) ** 2)

print("The radon concentration is: ", np.round(conc_calc, 2), " +/- ", np.round(conc_calc_unc, 2))