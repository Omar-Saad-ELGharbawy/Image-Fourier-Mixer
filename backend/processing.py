import numpy as np
from scipy.fft import ifft2, ifftshift
from matplotlib import pyplot as plt
from image import Image

class Processing:
    img1 = Image()
    img2 = Image()
    mixed_image_path = ""

    @staticmethod
    def crop_2d_img(image, **dimenions):
        max_height = image.shape[0]-1

        x1 = dimenions["x"] * image.shape[0] / 100
        x2 = x1 + (dimenions["width"] * image.shape[0] / 100)
        y2 = (100 - dimenions["y"]) * image.shape[1] / 100
        y1 = y2 - (dimenions["height"] * image.shape[1] / 100)
    #     cutted_img = np.ones_like(image)
    #     cutted_img = np.full_like(image,235)
        cutted_img = np.zeros_like(image)
        for x in range(int(x1), int(x2)):
            for y in range(int(y1), int(y2)):
                cutted_img[max_height-1-y, x] = image[max_height-1-y, x]
        return cutted_img

    @staticmethod
    def save_mixed_image(mag, phase):
        mixed_image = ifftshift(np.multiply(
            mag, np.exp(np.multiply(1j, phase))))
        mixed_image = ifft2(mixed_image)
        # mixed_image_data = np.multiply(mag, phase)
        # mixed_image = irfft2(mixed_image_data)
        # mixed_image_abs = np.abs(irfft2(mixed_image_data))

        plt.imsave(f".\\storage\\processed\mixed_img.png",
                mixed_image.real, cmap='gray')
