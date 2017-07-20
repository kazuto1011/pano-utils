#!/usr/bin/env python
# coding: utf-8
#
# Author:   Kazuto Nakashima
# URL:      http://kazuto1011.github.io
# Created:  2017-07-19

import sys
from itertools import product
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D
# import seaborn as sns

__HDL32E_VRANGE = 41.3
__HDL32E_VOFFSET = 10.67
__HDL32E_HRANGE = 360.0

panorama_d = np.load(sys.argv[1])
# panorama_r = np.load(sys.argv[2])

h, w, c = panorama_d.shape

points = []
# intensity = []
for i, j in product(range(h), range(w)):
    points.append((i, j, panorama_d[i, j, 0]))
    # intensity.append(panorama_r[i, j, 0])

points = np.asarray(points)
# intensity = np.asarray(intensity)
# intensity = intensity.clip(max=0.3)

print '{} points'.format(len(points))

yaw = np.radians(__HDL32E_HRANGE * points[:, 1] / w + 180)
pitch = np.radians(-__HDL32E_VRANGE * points[:, 0] / h + __HDL32E_VOFFSET)
range = points[:, 2]

X = range * np.sin(yaw) * np.cos(pitch)
Y = range * np.cos(yaw) * np.cos(pitch)
Z = range * np.sin(pitch)

fig = plt.figure(figsize=(20, 20))
ax = Axes3D(fig)

ax.scatter(X, Y, Z,
           c=points[:, 0],
           cmap='winter_r',
           s=1.0,
           )

ax.set_xlim(-0.5, 0.5)
ax.set_ylim(-0.5, 0.5)
ax.set_zlim(-0.1, 0.9)
ax.set_aspect('equal', adjustable='box')
ax.set_facecolor('black')
ax.axis('off')

# fig.savefig('cloud.png', transparent=True)
fig.savefig('cloud.png')
plt.show()
