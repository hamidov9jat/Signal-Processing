# There should be two graphs one partly filled with statistics
# the other with all statistics

# Group members:
# Hamidov Nijat, Azimov Farhad, 
# Gurbanov Kanan, Mamedov Kanan, Majidzade Javid. (CS-019)

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import statistics as st

# Create 42*13 matrix from ICE.txt
ICE = np.genfromtxt(fname="ICE.txt",
                    delimiter="   ")
# check
print(ICE)

# create 12 x 2 matrix for the year 1979
X = np.zeros([12, 2])
for j in range(12):
    X[j, 0] = ICE[0, 0] + (j + 0.5) / 12
    X[j, 1] = ICE[0, j + 1]
print(X)

# create 504 = 12*42 lines and 2 columns
A = np.zeros([42 * 12, 2])
month = 0
for i in range(42):
    for j in range(12):
        # time for month (j starts from 0)
        # j+1 - 0.5
        A[month, 0] = ICE[i, 0] + (j + 0.5) / 12
        A[month, 1] = ICE[i, j + 1]
        month += 1

print(A)

plt.plot(A[:, 0], A[:, 1])

# Assign 504*2 matrix to RAW
RAW = A

# Get sample mean
mu_RAW = st.mean(RAW[:, 1])

print("Mu_Raw: ", mu_RAW)

# Get standard deviation
stdev_RAW = st.pstdev(RAW[:, 1])

print("mu_STDV ", stdev_RAW)

# ADD mu, mu +std, mu - std as columns in RAW
RAW = np.append(RAW,
                np.array([[mu_RAW]] * 504), axis=1)

plt.plot(RAW[:, 0], RAW[:, 1], RAW[:, 0], RAW[:, 2])

RAW = np.append(RAW,
                np.array([[mu_RAW + stdev_RAW]] * 504), axis=1)

RAW = np.append(RAW,
                np.array([[mu_RAW - stdev_RAW]] * 504), axis=1)
# Display time series + mean + (mean + std) + (mean -std)
plt.plot(RAW[:, 0], RAW[:, 1], RAW[:, 0], RAW[:, 2],
         RAW[:, 0], RAW[:, 3], RAW[:, 0], RAW[:, 4])
plt.show()  # first graph
# check
print(RAW)
# ------------------------------------------------------------

# Display moving average + moving std up and down

# Note that's the second column in RAW
data = RAW[:, 1]

# data values for each month
data_series = pd.Series(data)

moving_average = data_series.rolling(25).mean()
moving_std = data_series.rolling(25).std()

rolling_up_std = moving_std.copy()
rolling_down_std = moving_std.copy()

for i in range(0, 504):
    # get movMu - movSTD
    rolling_up_std[i] = moving_average[i] + moving_std[i]

for i in range(0, 504):
    # get movMu - movSTD
    rolling_down_std[i] = moving_average[i] - moving_std[i]

# check for moving average
print(moving_average)

# Display all statistics
# Second Graph
plt.plot(RAW[:, 0], RAW[:, 1], RAW[:, 0], RAW[:, 2],
         RAW[:, 0], RAW[:, 3], RAW[:, 0], RAW[:, 4], RAW[:, 0], moving_average,
         RAW[:, 0], rolling_up_std, RAW[:, 0], rolling_down_std)

plt.show()
