import sys,os
sys.path.append(os.pardir)
import numpy as np
from dataset.mnist import load_mnist

def cee(y,t) :

    delta = 1e-7    

    if y.ndim == 1 :
        t = t.reshape(1,t.size)
        y = y.reshape(1,y.size)

    batch_size = y.shape[0]
    return -np.sum(t*np.log(y+delta))


(x_train,t_train),(x_test,t_test) = \
    load_mnist(normalize=True, one_hot_label=True)


def numerical_gradient(f, x) : # (f(x+h)-f(x-h)) / (2*h)   =>  h = 1e-4

    h = 1e-4
    grad = np.zeros_like(x) # result gradient
    
    for idx in range(x.size) :
        tmp = x[idx]

        #f(x+h)
        x[idx] = tmp + h
        fxph = f(x) # f( x plus h )

        #f(x-h)
        x[idx] = tmp - h
        fxmh = f(x) # f( x minus h )
        
        grad[idx] = (fxph - fxmh) / (2*h)
        x[idx] = tmp # recover

    return grad
        

print(x_train.shape)
print(t_train.shape)

train_size = x_train.shape[0]
batch_size = 10
batch_mask = np.random.choice(train_size, batch_size) # train_size 중 batch_size 만큼 고르기 위해 마스크 만들기
print(batch_mask)
x_batch = x_train[batch_mask]
t_batch = t_train[batch_mask]
 
