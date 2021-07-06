import numpy as np

class KNN:
    def __init__(self, n_neighbors):
        self.k = n_neighbors
        
    def fit(self, X, y):
        self.X = X
        self.y = y
        return self
    
    def predict(self, x_test):
        return self.__predict_private(x_test, self.X, self.y, self.k)

    def __square_diff(self, v1, v2):
        assert v1.shape==v2.shape
        v1_ = np.array(v1)
        v2_ = np.array(v2)
        return (v1_ - v2_)**2

    def __root_sum_squared(self, v1):
        return np.sqrt(v1.sum())

    def __euclidean_distances(self, v1, v2):
        return self.__root_sum_squared(self.__square_diff(v1, v2))

    def __predict_1(self, x_test, x_true, y_true, k = 5):
        # return (x_test, x_true[:2], y_true[:2])    
        dist_y = np.zeros(shape=(x_true.shape[0], 2))
        
        for i in np.arange(0, x_true.shape[0]):
            dist_y[i,0] = self.__euclidean_distances(x_test, x_true[i])
            dist_y[i,1] = y_true[i]
            
        dist_y = np.array(sorted(dist_y, key=lambda x: x[0]))
        dist_y = np.array(dist_y.T[1], dtype=np.int8)
        dist_y = np.bincount(dist_y[:k]).argmax()
        
        return dist_y


    def __predict_private(self, x_test, x_true, y_true, k = 5):
        
        all_dists = np.zeros(shape=x_test.shape[0], dtype=np.int8)
        
        for i in np.arange(0, x_test.shape[0]):
            all_dists[i] = self.__predict_1(x_test[i], x_true, y_true, k)
            
        return all_dists