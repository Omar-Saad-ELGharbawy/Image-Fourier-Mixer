import numpy as np
from scipy.fft import ifft2, ifftshift
from matplotlib import pyplot as plt
from image import Image
import cv2
from werkzeug.utils import secure_filename
from datetime import datetime
import os

processedImagePath = "http://127.0.0.1:5000/api/file/processed/"


class Processing:
    img1 = Image()
    img2 = Image()
    mixed_image_path = ""
    mixed_image_url = ""

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
        now = datetime.now()
        file_date = now.strftime("%m/%d/%Y, %H:%M:%S")
        file_date = secure_filename(file_date)

        Processing.mixed_image_url = processedImagePath+"mixed_img"+file_date+".png"

        Processing.mixed_image_path = f".\\storage\\processed\\mixed_img{file_date}.png"

        plt.imsave(Processing.mixed_image_path, mixed_image.real, cmap='gray')

    @staticmethod
    def select_and_save_mixed_img():
        if (Processing.img1.image_url == "" and Processing.img2.image_url == ""):
            Processing.mixed_image_url = ""
            return
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

    @staticmethod
    def getPaths():
        return {
            "img1": Processing.img1.image_url,
            "mag1": Processing.img1.mag_url,
            "phase1": Processing.img1.phase_url,
            "img2": Processing.img2.image_url,
            "mag2": Processing.img2.mag_url,
            "phase2": Processing.img2.phase_url,
            "mixed_img": Processing.mixed_image_url}
