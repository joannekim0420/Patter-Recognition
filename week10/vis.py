import numpy as np
import pandas as pd
import copy
import matplotlib.pyplot as plt

import sample_data
from meanshift import mean_shift, mean_shift_with_history

# %matplotlib inline

# # PyCharm에서 인터랙티브 창 띄우기
# import matplotlib
# matplotlib.use('TkAgg')

def calc_euclidean_distance(p1, p2):
    return np.sqrt(np.sum((p1 - p2) ** 2))

X = sample_data.sample2

# meanshift 수행
bandwidth = 4
centroids = mean_shift(X, bandwidth)

# 군집화 단계 (알고리즘 5-6의 line 12~14에 해당)
final_centroids = np.zeros_like(centroids)
for i in range(len(centroids)):
    in_bandwidth = []
    for j in range(len(centroids)):
        if calc_euclidean_distance(centroids[i], centroids[j]) <= bandwidth:
            in_bandwidth.append(centroids[j])

    final_centroids[i] = np.average(in_bandwidth, axis=0)
unique_centroids = np.unique(final_centroids, axis=0)

clusters = dict(zip(range(len(unique_centroids)), np.array([unique_centroids[i,:] for i in range(len(unique_centroids))])))
getcluster = lambda val : [k for k,v in clusters.items() if (v == val).sum()==len(val)][0]
df = pd.DataFrame(columns=['Sample_data','Centroids','Clusters'])
df['Sample_data'] = tuple(X)
df['Centroids']   = tuple(final_centroids)
df['Clusters']    = [getcluster(final_centroids[i]) for i in range(len(final_centroids))]
df