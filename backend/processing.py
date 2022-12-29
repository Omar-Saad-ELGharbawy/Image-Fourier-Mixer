import numpy as np
from scipy.fft import  rfft2, irfft2,fft2,ifft2 , fftshift , ifftshift
from scipy.fftpack import ifftshift

import cv2
import pylab
from matplotlib import pyplot as plt


def read_and_resize_image(image_path,width,height):
    image =cv2.imread(image_path,0)
    if (image.shape[0] != width) & (image.shape[1] != height) :
        image = cv2.resize(image, (width,height))
    return image


def get_img_magnitude_phase(image):
    fftdata = fft2(image)
    fftdata = fftshift(fftdata)
    fftmag = np.abs(fftdata)
    fftangle = np.angle(fftdata)
    return fftmag ,fftangle

def crop_2d_img(image,**dimenions) :
    max_width= image.shape[1]
    max_height= image.shape[0]
    x1 = dimenions["x"] * max_width /100
    x2 = x1 + (dimenions["width"] * max_width /100)
    y2 = (100- dimenions["y"] )* max_width /100
    y1 = y2 - (dimenions["height"] * max_height /100)
#     cutted_img = np.ones_like(image)
#     cutted_img = np.full_like(image,235)
    cutted_img = np.zeros_like(image)
    for x in range(int(x1),int(x2)):
        for y in range(int(y1),int(y2)):
            cutted_img[max_height-1-y,x] = image[max_height-1-y,x]
    return cutted_img

def save_3_images(self,name):
    img_mag = ifftshift(np.multiply(self.fftmag,1))
    img_mag = ifft2(img_mag)
    img_phase = ifftshift(1 * np.exp(np.multiply(1j,self.fftangle)))
    img_phase = ifft2(img_phase)
    plt.imsave(f"data\generated_images\\{name}.png",self.image, cmap='gray')
    plt.imsave(f"data\generated_images\\{name}_mag.png",img_mag.real, cmap='gray')
    plt.imsave(f"data\generated_images\\{name}_phase.png",img_phase.real, cmap='gray')

def save_mixed_image(img_mag_data,img_angle_data):
    mixed_img = ifftshift(np.multiply(img_mag_data,np.exp(np.multiply(1j,img_angle_data))))
    mixed_img = np.abs(ifft2(mixed_img))
    plt.imsave("data\generated_images\mixed_img.png",mixed_img, cmap='gray')