import sys, os
sys.path.append(os.pardir) # 현재 system path의 parent directory로 system path 수정
import numpy as np
from common.functions import softmax, cross_entropy_error
from common.gradient import numerical_gradient

class simpleNet :

    def __init__(self) :
        self.W = np.random.randn(2,3)


    def predict(self, x) :
        return np.dot(x, self.W)

    def loss(self, x, t) :
        z = self.predict(x)
