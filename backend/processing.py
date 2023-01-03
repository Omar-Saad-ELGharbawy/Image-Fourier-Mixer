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
    def save_mixed_image(mag, phase, cv=False):
        mixed_image = ifftshift(np.multiply(
            mag, np.exp(np.multiply(1j, phase))))
        mixed_image = ifft2(mixed_image)

        if cv:
            mixed_image = cv2.equalizeHist(mixed_image.astype(np.uint8))

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
        else:
            magVal = Processing.img1.mag if Processing.mag1 else Processing.img2.mag if Processing.mag2 else 100
            phaseVal = Processing.img1.phase if Processing.phase1 else Processing.img2.phase if Processing.phase2 else 0
            isCV = Processing.mag1 and not Processing.phase2 or Processing.mag2 and not Processing.phase1
            Processing.save_mixed_image(magVal, phaseVal, isCV)

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
