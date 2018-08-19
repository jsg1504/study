
import numpy as np

def mse(y,t) :
    return 0.5*np.sum((y-t)**2)

def cee(y,t) :
    delta = 1e-7
    return -np.sum(t*np.log(y+delta))

t = [0,0,1,0,0,0,0,0,0,0]
y = [0.1,0.05,0.6,0.0,0.05,0.1,0.0,0.1,0.0,0.0]

print("MSE : ")
print(mse(np.array(y),np.array(t)))
print("CEE : ")
print(cee(np.array(y),np.array(t)))

y = [0.1,0.05,0.1,0.0,0.05,0.1,0.0,0.6,0.0,0.0]

print("MSE : ")
print(mse(np.array(y),np.array(t)))
print("CEE : ")
print(cee(np.array(y),np.array(t)))

