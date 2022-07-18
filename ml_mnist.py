print('Praise the Lord')
import numpy as np
import struct
import matplotlib.pyplot as plt


import os
#os.chdir("C:\Users\christy\Downloads\mnist")
os.chdir("C:/Users/christy/Downloads/mnist")

#os.listdir('/content/drive/My Drive/mnist/')
def read_image_file(fname):
   fin = open(fname,'rb');
   mnum =  struct.unpack('>i',fin.read(4))
   nimages =  struct.unpack('>i',fin.read(4))
   nrows =   struct.unpack('>i',fin.read(4))
   ncols =   struct.unpack('>i',fin.read(4))
   dim = nrows[0]*ncols[0] ;
   x = np.array(list(fin.read()));
   x = x.reshape(nimages[0],dim);
   fin.close()
   return x;
def read_label_file(fname):
   fin = open(fname,'rb');
   mnum =  struct.unpack('>i',fin.read(4))
   nimages =  struct.unpack('>i',fin.read(4))
   x = np.array(list(fin.read()));
   x = x.reshape(nimages[0],1);
   fin.close()
   return x;
X = read_image_file('train-images-idx3-ubyte');
Y = read_label_file('train-labels-idx1-ubyte');
test_x = read_image_file('t10k-images-idx3-ubyte');
test_y = read_label_file('t10k-labels-idx1-ubyte');
print(X.shape)
print(Y.shape)
print(test_x.shape)
print(test_y.shape)
# display one image #

print(Y[7,:]);
print(X[7,:].shape)
x = X[501,:].reshape(28,28);

plt.imshow(x.astype('uint8'));
#plt.show()
rows=X.shape[1]
w=np.zeros((784,1))
b=0
print(w.shape)
print(X.shape)
X=X.reshape(X.shape[1],X.shape[0])
print(X.shape)
#To compute loss ,first compute the predictions
o=np.dot(w.T,X)+b

print(w.shape)
#apply sigmoid
h_x=1/(1+np.exp(-o))
m=X.shape[1]
J1 = (-1/m)*(np.sum(Y*np.log(h_x)+((1-Y)*np.log(1-h_x))))

"""
#compute cross entropy
#J1 = (-1/m)*(np.sum((Y*np.log(h_x))+((1-Y)*np.log(1-h_x)))  )
#J= (-1/m)*J1

#print cross entorpy
print(J)
for i in range(100): # start with 100 epochs
    print(i); # print epoch number

    # Compute gradients
    dw = (1/m)*np.dot((h_x-Y).T,X)
    db = (1/m) * (np.sum(h_x-Y))
    #db = db1
    #dw = (1/m) * (np.dot(X,(A-Y).T))
    #db = (1/m) * (np.sum(A-Y))
    # update weights
    alpha=0.0001
    w=w-alpha*dw
    b=b-alpha*db
print(w.shape)
"""

