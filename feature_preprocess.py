import scipy.io as sio
import numpy as np
from sklearn.decomposition import PCA

mat = sio.loadmat('docia.mat')
x = mat['embedmap']

(h,w,d) = x.shape

x = np.reshape(x, ((h*w), d))

pca = PCA(n_components=3)

y = pca.fit_transform(x)

y = np.reshape(y, (h,w,3))

for i in range(3):
    y[:,:,i] = y[:,:,i] - y[:,:,i].min()
    y[:,:,i] = y[:,:,i] - y[:,:,i].max()


