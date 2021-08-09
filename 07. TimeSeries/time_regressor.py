import pandas as pd
import numpy as np


# Load the data
data = pd.read_csv('climate.csv')
data = data.drop(['Date Time'], axis=1)


# Pairing function
def pairing(data, seq_len = 6):
    
    x = []
    y = []
    
    for i in range(0, (data.shape[0]-1)):
        seq = np.zeros((seq_len, data.shape[1]))
        
        for j in range(seq_len):
            seq[j] = data.values[i+j]
        
        x.append(seq)
        y.append(i+seq_len)
        
    return np.array(x), np.array(y)

x, y = pairing(data)


from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

nsamples, nx, xy = X_train.shape
X_train_d2 = X_train.reshape((nsamples, nx*ny))

y_train = y_train.reshape(-1, 1)
y_train.shape
y_test = y_test.reshape(-1, 1)

from sklearn.ensemble import RandomForestRegressor

clf = RandomForestRegressor()
clf.fit(X_train_d2, y_train)

RandomForestRegressor()

from sklearn.metrics import mean_absolute_error
pred = clf.predict(X_test_d2)
mean_absolute_error(y_test, pred)