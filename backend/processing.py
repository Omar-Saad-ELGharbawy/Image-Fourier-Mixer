import numpy as np
from scipy.fft import ifft2, ifftshift
from matplotlib import pyplot as plt
from image import Image
import cv2

class Processing:
    img1 = Image()
    img2 = Image()
    mixed_image_path = ""

    phase1 = False
    phase2 = False
    mag1 = False
    mag2 = False

    @staticmethod
    def save_mixed_image(mag, phase):
        mixed_image = ifftshift(np.multiply(
            mag, np.exp(np.multiply(1j, phase))))
        mixed_image = ifft2(mixed_image)
        # mixed_image = cv2.equalizeHist(mixed_image.astype(np.uint8))
        # mixed_image = np.abs(mixed_image)
        plt.imsave(f".\\storage\\processed\mixed_img.png",
                mixed_image.real, cmap='gray')

    @staticmethod
    def select_and_save_mixed_img():
        if (Processing.phase1 and not Processing.mag2):
            Processing.save_mixed_image(
            1, Processing.img1.phase)
        elif (Processing.phase2 and not Processing.mag1):
            Processing.save_mixed_image(
            1, Processing.img2.phase)
        elif (Processing.mag1 and not Processing.phase2):
            Processing.save_mixed_image(
            Processing.img1.mag, 0)
        elif (Processing.mag2 and not Processing.phase1):
            Processing.save_mixed_image(
            Processing.img2.mag, 0)
        elif (Processing.mag1 and Processing.phase2):
            Processing.save_mixed_image(
            Processing.img1.mag, Processing.img2.phase)
        elif (Processing.mag2 and Processing.phase1):
            Processing.save_mixed_image(
            Processing.img2.mag, Processing.img1.phase)