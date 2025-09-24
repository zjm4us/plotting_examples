import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)  # reproducible results

samples = 10000  # number of samples
mu = 100         # Gaussian mean
sigma = 6        # Gaussian std deviation

# Canvas 1: Single Gaussian
data1 = np.random.normal(mu, sigma, samples)  # generate Gaussian
plt.figure(figsize=(8,5))
plt.hist(data1, bins=100, range=(50,150), histtype='step', color='blue', linewidth=1.5)  # histogram
plt.xlabel('x')       # x-axis label
plt.ylabel('Frequency')  # y-axis label
plt.title('Random Gaussian')  # title
plt.grid(True)        # show grid
plt.savefig('canvas1_py.png', dpi=300)  # save figure
plt.close()           # close figure

# Canvas 2: 2x2 Panels
fig, axs = plt.subplots(2,2, figsize=(10,8))  # create 2x2 panel

# Panel 1: Original Gaussian
axs[0,0].hist(data1, bins=100, range=(50,150), histtype='step', color='blue', linewidth=1.5)
axs[0,0].set_title('Original Gaussian')
axs[0,0].set_xlabel('x')
axs[0,0].set_ylabel('Frequency')
axs[0,0].grid(True)

# Panel 2: Gaussian + Uniform Offset
data2 = np.append(data1, np.random.uniform(50,150,samples//3))  # add uniform numbers
axs[0,1].hist(data2, bins=100, range=(50,150), histtype='step', color='green', linewidth=1.5)
axs[0,1].set_title('Gaussian + Uniform Offset')
axs[0,1].set_xlabel('x')
axs[0,1].set_ylabel('Frequency')
axs[0,1].grid(True)

# Panel 3: Gaussian + 1/x^2 baseline
u = np.random.uniform(0,1,samples*30)  # uniform random
x_vals = 40 + 10 / np.sqrt(u)          # transform to 1/x^2 distribution
data3 = np.append(data1, x_vals)       # combine with original Gaussian
axs[1,0].hist(data3, bins=100, range=(50,150), histtype='step', color='red', linewidth=1.5, log=True)  # log scale
axs[1,0].set_title('Gaussian + 1/x^2 Baseline')
axs[1,0].set_xlabel('x')
axs[1,0].set_ylabel('Frequency')
axs[1,0].grid(True, which='both')

# Panel 4: Double Gaussian (superposition)
data4 = data1.copy()  # original Gaussian
data4 = np.append(data4, np.random.normal(mu, 20, samples//2))  # add second Gaussian
counts, bins = np.histogram(data4, bins=100, range=(50,150))  # get max count
axs[1,1].hist(data4, bins=100, range=(50,150), histtype='step', color='purple', linewidth=1.5)
axs[1,1].set_title('Double Gaussian')
axs[1,1].set_xlabel('x')
axs[1,1].set_ylabel('Frequency')
axs[1,1].grid(True)
axs[1,1].set_ylim(0, counts.max()*1.1)  # adjust y-axis to include all events

plt.tight_layout()           # adjust layout
plt.savefig('canvas2_py.pdf')  # save figure
plt.close()                  # close figure

