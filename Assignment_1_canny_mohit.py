import numpy as np
def gaussian_kernel(size, sigma):

    kernel = np.zeros((size, size))

    # code starts here
    a = 1/ (2*np.pi*sigma*sigma)
    for i in range(0,size):
        for j in range(0,size):
            kernel[i][j]=a*np.exp(-((i-size//2)**2 + (j-size//2)**2 )/(2*sigma*sigma))

  

    return kernel

from scipy.signal import convolve2d
def conv(image, kernel):
    Hi, Wi = image.shape
    Hk, Wk = kernel.shape
    out = np.zeros((Hi, Wi))

    pad_width0 = Hk // 2
    pad_width1 = Wk // 2
    pad_width = ((pad_width0,pad_width0),(pad_width1,pad_width1))
    padded = np.pad(image, pad_width, mode='edge')

    
    out = convolve2d(padded, kernel, mode='valid')
    

    return out

import imageio as iio
import matplotlib.pyplot as plt

kernel_size = 5
sigma = 1.8
impath = str(input("enter the path of the image you want to detected edges of:"))

image = iio.imread(impath , mode='F')

kernel = gaussian_kernel(kernel_size, sigma)

smoothed_image = conv(image, kernel)


def partial_x(img):
    out = None

  
    kernel = np.array([0.5, 0, -0.5]).reshape(1,-1)
    out = conv(img, kernel)
    
    return out

grid=np.array([0.5, 0, -0.5]).reshape(1,-1)

grid = np.arange(1, 10).reshape((3, 3))

def partial_y(img):
    out = None
   
    kernel = np.array([0.5, 0, -0.5]).reshape(-1,1)
    out = conv(img, kernel)
    
    return out

Gx = partial_x(smoothed_image)
Gy = partial_y(smoothed_image)


def gradient(img):
    G = np.zeros(img.shape)
    theta = np.zeros(img.shape)

    
    dx = partial_x(img)
    dy = partial_y(img)

    G = np.sqrt(dx**2 + dy**2)
    theta = (np.arctan2(dy, dx) * 180 / np.pi) % 360
    

    return G, theta

G, theta = gradient(smoothed_image)

if not np.all(G >= 0):
    print('Magnitude of gradients should be non-negative.')

if not np.all((theta >= 0) * (theta < 360)):
    print('Direction of gradients should be in range 0 <= theta < 360')

plt.imshow(G)
plt.title('Gradient magnitude')
plt.axis('off')
plt.show()
plt.imshow(image)

