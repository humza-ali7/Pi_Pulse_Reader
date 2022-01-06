import numpy as np
from sklearn.neighbors import KNeighborsClassifier

# KNN trainer model to determine active and rest state from given pulse rate data

# initialize arrays
X = [] 
y = [] 

X_test = []
y_test = []

# load active state readings 
X.append(np.load("active1.npy"))
y.append(1)

X.append(np.load("active2.npy"))
y.append(1)

X.append(np.load("active3.npy"))
y.append(1)

X.append(np.load("active4.npy"))
y.append(1)

X.append(np.load("active5.npy"))
y.append(1)

# load rest state readings
X.append(np.load("rest1.npy"))
y.append(0)

X.append(np.load("rest2.npy"))
y.append(0)

X.append(np.load("rest3.npy"))
y.append(0)

X.append(np.load("rest4.npy"))
y.append(0)

X.append(np.load("rest5.npy"))
y.append(0)

# active test file for training
X_test.append(np.load("active_test1.npy"))
y_test.append(1)

X_test.append(np.load("active_test2.npy"))
y_test.append(1)

# resting test file for training
X_test.append(np.load("rest_test1.npy"))
y_test.append(0)

X_test.append(np.load("rest_test2.npy"))
y_test.append(0)


# create arrays from X and Y
X = np.array(X)
y = np.array(y)

X_test = np.array(X_test)
y_test = np.array(y_test)

# KNN model (N = 3)
neigh = KNeighborsClassifier(n_neighbors=3)
neigh.fit(X, y)

print(f"Prediction: {neigh.predict(X_test)}, Ground Truth: {y_test}")