import numpy as np
def polyfit1(x,y,n):
    
    def inv(A):
        return np.linalg.inv(A)
    def trans(A):
        return A.getT()
    def oneMat(xl,n):
        return np.ones((xl,n),dtype=int)
    def prod(A,B):
        return np.dot(A,B)
    
    xlen = len(x)
    ylen = len(y)
    one = np.ones((xlen,n+1),dtype=int)
    c1=one[:,[1]]
    xT=np.matrix(x)
    yT=np.matrix(y)
    A=np.hstack([c1,xT.getT()])
    return prod(prod(inv(prod(trans(A),A)),trans(A)),trans(yT))
    
x=[1,1.6,3.4,4,5.2]
y=[1.2,2,2.4,3.5,3.5]

polyfit1(x,y,1)

def polyfit2(x,y,n):
    
    def inv(A):
        return np.linalg.inv(A)
    def trans(A):
        return A.getT()
    def oneMat(xl,n):
        return np.ones((xl,n),dtype=int)
    def prod(A,B):
        return np.dot(A,B)
    
    xlen = len(x)
    ylen = len(y)
    one = np.ones((xlen,n+1),dtype=int)
    c1=one[:,[1]]
    xT=np.matrix(x)
    yT=np.matrix(y)
    c2=xT.getT()
    c3=np.power(c2,2)
    A=np.hstack([c1,c2,c3])
    print(A)
    return prod(prod(inv(prod(trans(A),A)),trans(A)),trans(yT))

x=[1,2,3]
y=[1,4,9]

polyfit2(x,y,2)


