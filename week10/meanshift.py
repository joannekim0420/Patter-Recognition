import numpy as np


#점과 점 사이의 거리
def calc_euclidean_distance(p1, p2):
    return np.sqrt(np.sum((p1 - p2) ** 2))


def calc_weight(x, kernel='flat'):
    if x <= 1:
        if kernel.lower() == 'flat':
            return 1
        elif kernel.lower() == 'gaussian':
            return np.exp(-1 * (x ** 2))
        else:
            raise Exception("'%s' is invalid kernel" % kernel)
    else:
        return 0

    
def mean_shift(X, bandwidth, n_iteration=20, epsilon=0.001): #bandwidth=탐색에 사용하는 원의 직경
    centroids = np.zeros_like(X)   

    for i in range(len(X)):        
        centroid = X[i].copy()  # 초기 중심점(t_0) 설정 -> 각 datapoint를 초기 중심점으로 할당
        prev = centroid.copy()
        
        t = 0
        while True:

            #points_within = []

            # for feature in X:
            #     if (calc_euclidean_distance(feature,centroid) <= bandwidth):
            #             points_within.append(feature)

            numerator=0
            denominator =0
            for sample in X:
                #print(points_[0])
                distance = calc_euclidean_distance(centroid,sample)
                weight = calc_weight(distance, 'gaussian')
                numerator += (sample-centroid)*weight
                denominator += weight

            if denominator ==0:
                shitf =0
            else:
                shift = new_centroid = numerator/denominator
            centroid += shift

            if(t>n_iteration):
                break
            if(calc_euclidean_distance(centroid, prev)<epsilon):
                break


            prev=centroid.copy()
            t += 1

        centroids[i] = centroid.copy()

    return centroids

    
def mean_shift_with_history(X, bandwidth, n_iteration=20, epsilon=0.001):
    history = {}
    for i in range(len(X)):
        history[i] = []
    centroids = np.zeros_like(X)   

    for i in range(len(X)):
        centroid = X[i].copy()  # 초기 중심점(t_0) 설정 -> 각 datapoint를 초기 중심점으로 할당
        prev = centroid.copy()
        history[i].append(centroid.copy())
        
        t = 0
        while True:
            """
            코드 완성할 부분
            """
            points_within = []

            for feature in X:
                if (calc_euclidean_distance(feature,centroid) <= bandwidth):
                        points_within.append(feature)

            a=0
            b=0
            for points_ in points_within:
                #print(points_[0])
                distance = calc_euclidean_distance(points_,centroid)
                w = calc_weight(distance, 'gaussian')
                a+=points_*w
                b+=w
            new_centroid = a/b

            t+=1
            prev=centroid.copy()
            centroid=new_centroid.copy()
            
            #print("t:{}".format(t))
            if(t>n_iteration):
                break
            if(calc_euclidean_distance(centroid, prev)<epsilon):
                break
            history[i].append(centroid.copy())

        
        centroids[i] = centroid.copy()

    return centroids, history
