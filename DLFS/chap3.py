import numpy as np
import matplotlib.pylab as plt


def step_function(x) :
    y = x > 0
    return y.astype(np.int)

def sigmoid(x) :
    return 1 / (1 + np.exp(-x))

def relu(x) :
    return np.maximum(0,x)

def identity_function(x) :
    return x

def func_shape(k) :

    x = np.arange(-5.0,5.0,0.1)
    
    if k == 1 : y = step_function(x)
    elif k == 2 : y = sigmoid(x)
    elif k == 3 : y = relu(x)

    plt.plot(x,y)
    plt.ylim(-0.1, 1.1)
    plt.show()


def softmax(x) :
    c = np.max(x)
    exp_x = np.exp(x-c)
    exp_sum = np.sum(exp_x)
    return exp_x/exp_sum


X = np.array([1.0,0.5])
W1 = np.array([[0.1,0.3,0.5],[0.2,0.4,0.6]])
B1 = np.array([0.1,0.2,0.3])

A1 = np.dot(X,W1)+B1
Z1 = sigmoid(A1)
print(Z1)

W2 = np.array([[0.1,0.4],[0.2,0.5],[0.3,0.6]])
B2 = np.array([0.1,0.2])

A2 = np.dot(Z1,W2)+B2
Z2 = sigmoid(A2)
print(Z2)

W3 = np.array([[0.1,0.3],[0.2,0.4]])
B3 = np.array([0.1,0.2])

A3 = np.dot(Z2,W3)+B3
Y = identity_function(A3)
print(Y)

Y2 = softmax(A3)
print(Y2)

