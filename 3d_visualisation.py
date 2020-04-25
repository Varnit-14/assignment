# -*- coding: utf-8 -*-
"""3d_visualisation

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1QXLQs8whDZ3eglww8EC7lmSTU-bVARjj
"""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sklearn import decomposition
from sklearn import datasets

df=datasets.load_iris()
print(dir(df))
X=df.data
y=df.target

fig = plt.figure(1, figsize=(8, 6))
ax = Axes3D(fig, elev=-150, azim=110)
X_reduced =decomposition.PCA(n_components=3).fit_transform(df.data)
ax.scatter(X_reduced[:, 0], X_reduced[:, 1], X_reduced[:, 2], c=y,
           cmap=plt.cm.Set1, edgecolor='k', s=40)
ax.set_title("First three PCA directions")
ax.set_xlabel(df.target_names[0])
ax.w_xaxis.set_ticklabels([])
ax.set_ylabel(df.target_names[1])
ax.w_yaxis.set_ticklabels([])
ax.set_zlabel(df.target_names[2])
ax.w_zaxis.set_ticklabels([])

