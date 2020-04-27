import numpy as np


def getData(nclass, seed = None):

    assert nclass == 2 or nclass == 3

    if seed != None:
        np.random.seed(seed)

    # 2次元の spherical な正規分布3つからデータを生成
    X0   = 0.10 * np.random.randn(200, 2) + [ 0.3, 0.3 ]
    X1   = 0.10 * np.random.randn(200, 2) + [ 0.7, 0.6 ]
    X2   = 0.05 * np.random.randn(200, 2) + [ 0.3, 0.7 ]

    # それらのラベル用のarray
    lab0 = np.zeros(X0.shape[0], dtype = int)
    lab1 = np.zeros(X1.shape[0], dtype = int) + 1
    lab2 = np.zeros(X2.shape[0], dtype = int) + 2

    # X （入力データ）, label （クラスラベル）, t（教師信号） をつくる
    if nclass == 2:
        X = np.vstack((X0, X1))
        label = np.hstack((lab0, lab1))
        t = np.zeros(X.shape[0])
        t[label == 1] = 1.0
    else:
        X = np.vstack((X0, X1, X2))
        label = np.hstack((lab0, lab1, lab2))
        t = np.zeros((X.shape[0], nclass))
        for ik in range(nclass):
            t[label == ik, ik] = 1.0

    return X, label, t