import numpy as np
from scipy.fft import fft2, ifft2, fftshift, ifftshift
from scipy.fftpack import ifftshift
import cv2
from matplotlib import pyplot as plt
from werkzeug.utils import secure_filename
from datetime import datetime
import os

processedImagePath = "http://127.0.0.1:5000/api/file/processed/"


class Image:
    width = 300
    height = 200
    # image_path = ""
    # image_mag_path = ""
    # image_phase_path = ""
    # dimensions = {}
    image_url = ""
    mag_url = ""
    phase_url = ""

    def __init__(self):
        self.image_url = ""
        self.mag_url = ""
        self.phase_url = ""
        # pass
        self.phase = 0
        self.mag = 1

    def read(self, image_path, name):
        self.name = name
        self.image_path = image_path
        self.image = cv2.imread(self.image_path, 0)
        if (self.image.shape[1] != self.width) or (self.image.shape[0] != self.height):
            self.image = cv2.resize(self.image, (self.width, self.height))

    def calculate_magnitude_and_phase(self):
        fftdata = fft2(self.image)
        fftdata = fftshift(fftdata)
        self.mag = np.abs(fftdata)
        self.phase = np.angle(fftdata)
        self.original_mag = self.mag
        self.original_phase = self.phase

    def save(self):
        # img_mag = ifftshift(np.multiply(self.mag, 1))
        # img_mag = ifft2(img_mag)
        # img_phase = ifftshift(100 * np.exp(np.multiply(1j, self.phase)))
        # img_phase = ifft2(img_phase)
        # img_phase = cv2.equalizeHist(img_phase.astype(np.uint8))
        # img_mag = cv2.equalizeHist(img_mag.astype(np.uint8))
        now = datetime.now()
        file_date = now.strftime("%m/%d/%Y, %H:%M:%S")
        file_date = secure_filename(file_date)

        self.image_url = processedImagePath+self.name+file_date+".png"
        self.mag_url = processedImagePath+self.name+file_date+"_mag.png"
        self.phase_url = processedImagePath + self.name+file_date+"_phase.png"

        self.image_path = f".\\storage\\processed\\{self.name+file_date}.png"
        self.image_mag_path = f".\\storage\\processed\\{self.name+file_date}_mag.png"
        self.image_phase_path = f".\\storage\\processed\\{self.name+file_date}_phase.png"
        # plt.imsave(self.image_path, self.image, cmap='gray')
        # plt.imsave(self.image_mag_path, img_mag.real, cmap='gray')
        # plt.imsave(self.image_phase_path, img_phase.real, cmap='gray')
        plt.imsave(self.image_path, self.image, cmap='gray')
        plt.imsave(self.image_mag_path, np.log(self.mag), cmap='gray')
        plt.imsave(self.image_phase_path, self.phase, cmap='gray')

    def crop_mag_and_phase(self, **dimenions):
        # max_height = self.image.shape[0]-1
        x1 = dimenions["x"] * self.width / 100
        x2 = x1 + (dimenions["width"] * self.width / 100)
        y2 = (100 - dimenions["y"]) * self.height / 100
        y1 = y2 - (dimenions["height"] * self.height / 100)
    #     cutted_img = np.ones_like(image)
    #     cutted_img = np.full_like(image,235)
        self.mag = np.zeros_like(self.original_mag)
        self.phase = np.zeros_like(self.original_phase)

        for x in range(int(x1), int(x2)):
            for y in range(int(y1), int(y2)):
                self.mag[self.height-1-y,
                         x] = self.original_mag[self.height-1-y, x]
                self.phase[self.height-1-y,
                           x] = self.original_phase[self.height-1-y, x]
