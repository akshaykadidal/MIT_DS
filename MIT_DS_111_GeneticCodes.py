# -*- coding: utf-8 -*-
"""
Created on Sun Oct 28 01:58:14 2018

@author: Akshay
"""

import pandas as pd
from pandas import *
import os
import re
from itertools import product

#dir_path = os.getcwd()
#os.chdir("C:\\Users\\akshay\\Desktop\\Self To-Do\\MIT DS")

# Open the file
f = open("gene.txt", 'r')
lines = list(f)
txt = str()
for i in range(len(lines)):
    txt = txt + lines[i].replace("\n", "")

txt = re.sub("(.{300})", "\\1\\n", txt)

print(txt, file=open('new.txt', 'w'))

f.close()

f=open("new.txt", 'r')
lines = list(f)
list_p = [''.join(p) for p in product('acgt', repeat=3)] 
df = pd.DataFrame(columns = list_p)


for i in range(len(lines)):
    txt =  lines[i]
    lst = (re.sub("(.{3})", "\\1 ",txt))
    wordlist = lst.split()
    wordfreq = []
    for w in list_p:
        wordfreq.append(wordlist.count(w))
    df.loc[i] = wordfreq

f.close()

from sklearn.preprocessing import StandardScaler
X_std = StandardScaler().fit_transform(df)


from sklearn.decomposition import PCA
pca = PCA(n_components=2)
principalComponents = pca.fit_transform(X_std)
principalDf = pd.DataFrame(data = principalComponents, columns = ['principal component 1', 'principal component 2'])

import matplotlib.pyplot as plt
plt.plot(principalDf['principal component 1'], principalDf['principal component 2'], 'bo') 



from sklearn.cluster import KMeans
import numpy as np

kmeans = KMeans(n_clusters=7)
kmeans.fit(principalDf)
y_kmeans = kmeans.predict(principalDf)

plt.scatter(principalDf['principal component 1'], principalDf['principal component 2'], c=y_kmeans, s=50, cmap='viridis')

centers = kmeans.cluster_centers_
plt.scatter(centers[:, 0], centers[:, 1], c='black', s=200, alpha=0.5);
