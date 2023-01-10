import numpy as np
from scipy.fft import ifft2, ifftshift
from matplotlib import pyplot as plt
from image import Image
import cv2
from werkzeug.utils import secure_filename
from datetime import datetime

processedImagePath = "http://127.0.0.1:5000/api/file/processed/"

#  Processing Class contains static objects of the Image Class to access it in mixing images to be used in backend
#  It also contains the methods to:
#  - save the mixed image
#  - select which images components (mag,phase) to be mixed
#  - get all the urls of the images (mixed, img1, img2, mag1, mag2, phase1, phase2) to be used in the frontend to display the images
class Processing:
    # static objects of the Image Class for image 1 and image 2
    img1 = Image()
    img2 = Image()
    mixed_image_path = ""
    mixed_image_url = ""
    # flags to check which image components to be mixed
    phase1 = False
    phase2 = False
    mag1 = False
    mag2 = False

    # static method to save the mixed image
    @staticmethod
    def save_mixed_image(mag, phase, cv=False):
        #  mutliply the magnitude and phase of the image 1 and image 2 and inverse shift the result
        mixed_image = ifftshift(np.multiply(mag, np.exp(np.multiply(1j, phase))))
        # calculate the inverse fourier transform of the mixed image
        mixed_image = ifft2(mixed_image)
        if cv:
            mixed_image = cv2.equalizeHist(mixed_image.astype(np.uint8))
        # get the current date and time to be used in the image name
        now = datetime.now()
        file_date = now.strftime("%m/%d/%Y, %H:%M:%S")
        file_date = secure_filename(file_date)
        # mixed image url to be used in the frontend to display the image
        Processing.mixed_image_url = processedImagePath+"mixed_img"+file_date+".png"
        # mixed image path to be used in the backend to save the image
        Processing.mixed_image_path = f".\\storage\\processed\\mixed_img{file_date}.png"
        # save the mixed image
        plt.imsave(Processing.mixed_image_path, mixed_image.real, cmap='gray')

    # static method to select which image components to be mixed
    # it also calls the save_mixed_image method to save the mixed image
    @staticmethod
    def select_and_save_mixed_img():
        # if both images are empty, set the mixed image url to be empty
        if (Processing.img1.image_url == "" and Processing.img2.image_url == ""):
            Processing.mixed_image_url = ""
            print("No Image")
        # select the image components to be mixed from the flags
        elif not(Processing.mag1 or Processing.mag2 or Processing.phase1 or Processing.phase2):
            Processing.mixed_image_url = ""
        else:
            magVal = Processing.img1.mag if Processing.mag1 else Processing.img2.mag if Processing.mag2 else 100
            phaseVal = Processing.img1.phase if Processing.phase1 else Processing.img2.phase if Processing.phase2 else 0
            isCV = Processing.mag1 and not Processing.phase2 or Processing.mag2 and not Processing.phase1
            Processing.save_mixed_image(magVal, phaseVal, isCV)

    # static method to get all the urls of the images (mixed, img1, img2, mag1, mag2, phase1, phase2) to be used in the frontend to display the images
    @staticmethod
    def getPaths():
        # return the urls of the images
        return {
            "img1": Processing.img1.image_url,
            "mag1": Processing.img1.mag_url,
            "phase1": Processing.img1.phase_url,
            "img2": Processing.img2.image_url,
            "mag2": Processing.img2.mag_url,
            "phase2": Processing.img2.phase_url,
            "mixed_img": Processing.mixed_image_url}
