import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm  # for log scale panel

np.random.seed(42)  # reproducible results

samples = 10000
mu = 100
sigma = 6

# 2x2 Panel Figure
fig, axs = plt.subplots(2,2, figsize=(12,10))

# Panel 1: Original 2D Gaussian
x1 = np.random.normal(mu, sigma, samples)
y1 = np.random.normal(mu, sigma, samples)
h1 = axs[0,0].hist2d(x1, y1, bins=100, range=[[50,150],[50,150]], cmap='Blues')
axs[0,0].set_title('2D Gaussian')
axs[0,0].set_xlabel('x')
axs[0,0].set_ylabel('y')
plt.colorbar(h1[3], ax=axs[0,0])

# Panel 2: Gaussian + Uniform Background
x2 = np.append(x1, np.random.uniform(50,150,samples//3))
y2 = np.append(y1, np.random.uniform(50,150,samples//3))
h2 = axs[0,1].hist2d(x2, y2, bins=100, range=[[50,150],[50,150]], cmap='Greens')
axs[0,1].set_title('2D Gaussian + Uniform')
axs[0,1].set_xlabel('x')
axs[0,1].set_ylabel('y')
plt.colorbar(h2[3], ax=axs[0,1])

# Panel 3: Gaussian + 1/(x*y)^2 Background
u = np.random.uniform(0,1,samples*30)
v = np.random.uniform(0,1,samples*30)
x3_bg = 40 + 10 / np.sqrt(u)
y3_bg = 40 + 10 / np.sqrt(v)
x3 = np.append(x1, x3_bg)
y3 = np.append(y1, y3_bg)
h3 = axs[1,0].hist2d(x3, y3, bins=100, range=[[50,150],[50,150]], cmap='Reds', norm=LogNorm())
axs[1,0].set_title('2D Gaussian + 1/(x*y)^2')
axs[1,0].set_xlabel('x')
axs[1,0].set_ylabel('y')
plt.colorbar(h3[3], ax=axs[1,0])

# Panel 4: Double 2D Gaussian
x4 = np.append(x1, np.random.normal(mu, 20, samples//2))
y4 = np.append(y1, np.random.normal(mu, 20, samples//2))
h4 = axs[1,1].hist2d(x4, y4, bins=100, range=[[50,150],[50,150]], cmap='Purples')
axs[1,1].set_title('Double 2D Gaussian')
axs[1,1].set_xlabel('x')
axs[1,1].set_ylabel('y')
plt.colorbar(h4[3], ax=axs[1,1])

plt.tight_layout()
plt.savefig('canvas2d_py.png', dpi=300)
plt.close()

