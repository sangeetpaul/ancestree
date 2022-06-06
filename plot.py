import numpy as np
import matplotlib.pyplot as plt
import full_binary

n = 2279
height = np.empty(n, int)
n_leaves = np.empty(n, int)

for i in range(n):
    height[i] = full_binary.height_of_tree(i)
    n_leaves[i] = full_binary.n_leaves_in_tree(i)

fig, ax = plt.subplots(2, 2, figsize=(2*6.4, 2*4.8))
ns = np.arange(0, n)

ax[0, 0].plot(ns, height, label="height")
ax[0, 0].plot(ns, n_leaves, label="no. of leaves", lw=1)
ax[0, 0].legend()
ax[0, 0].set_xlabel("tree")

ax[0, 1].set_xscale('log')
ax[0, 1].plot(ns, height, label="height")
ax[0, 1].plot(ns, n_leaves, label="no. of leaves", lw=1)
ax[0, 1].legend()
ax[0, 1].set_xlabel("tree")

ax[1, 0].hist(n_leaves, bins=max(n_leaves))
ax[1, 0].set_xlabel("no. of leaves")

ax[1, 1].hist(height, bins=max(height)+1, log=True)
ax[1, 1].set_xlabel("height")

fig.tight_layout()
fig.savefig('plot.png')
