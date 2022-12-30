import numpy as np
from scipy.fft import fft2, ifft2, fftshift, ifftshift
from scipy.fftpack import ifftshift
import cv2
from matplotlib import pyplot as plt


class Image:
    width = 900
    height = 600
    image_path = ""
    image_mag_path = ""
    image_phase_path = ""
    dimensions = {}

    def __init__(self):
        self.phase = 0
        self.mag = 1

    def read(self, image_path):
        self.image_path = image_path
        self.image = cv2.imread(self.image_path, 0)
        if (self.image.shape[0] != self.width) & (self.image.shape[1] != self.height):
            self.image = cv2.resize(self.image, (self.width, self.height))

    def calculate_magnitude_and_phase(self):
        fftdata = fft2(self.image)
        fftdata = fftshift(fftdata)
        self.mag = np.abs(fftdata)
        self.phase = np.angle(fftdata)

    def save(self, name):
        img_mag = ifftshift(np.multiply(self.mag, 1))
        img_mag = ifft2(img_mag)
        img_phase = ifftshift(1 * np.exp(np.multiply(1j, self.phase)))
        img_phase = ifft2(img_phase)

        # img_phase = cv2.equalizeHist(img_phase.astype(np.uint8))
        # img_mag = cv2.equalizeHist(img_mag.astype(np.uint8))

        self.image_path = f".\\storage\\processed\\{name}.png"
        self.image_mag_path = f".\\storage\\processed\\{name}_mag.png"
        self.image_phase_path = f".\\storage\\processed\\{name}_phase.png"

        plt.imsave(self.image_path, self.image, cmap='gray')
        plt.imsave(self.image_mag_path, img_mag.real, cmap='gray')
        plt.imsave(self.image_phase_path, img_phase.real, cmap='gray')
