# ほげほげ
# ver.20171109

import numpy as np 
import getData

if __name__ == '__main__':

    import matplotlib
    import matplotlib.pyplot as plt

    K = 2
    M = 0.005
    
    X, lab, t = getData.getData(K)

    W = []
    m = int(input())

    W = 0.02 * np.random.rand(K) - 0.01

    N = X.shape[0]

    Z = np.zeros(N)
    L = np.zeros(N)

    for i in range(1000000):

        n = np.random.randint(N-1)

        z = 1.0 / (1.0 + np.exp(-W * X))

        h = -t[n] * np.log(z) - (1 - t[n]) * np.log(1 - z)
 
        W = (z - t[n]) * X

        if  i % 2000 == 0:

            H = 0.0
            cnt1 = 0

            Z = 1 / (1 + np.exp(-W * X))

            Z = Z.reshape(N)

            h = -t * np.log(Z) - (1 - t) * np.log(1 - Z)

            L = (0 <= a * X[:,0] + b * X[:,1] + c)

            cnt1 = np.count_nonzero(L == lab)

            cnt = cnt1 / N

            H = np.sum(h)

            print(i,  H,  cnt)
