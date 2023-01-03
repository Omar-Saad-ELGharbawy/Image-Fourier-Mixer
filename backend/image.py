import numpy as np
from scipy.fft import fft2, ifft2, fftshift, ifftshift
from scipy.fftpack import ifftshift
import cv2
from matplotlib import pyplot as plt
from werkzeug.utils import secure_filename
from datetime import datetime

processedImagePath = "http://127.0.0.1:5000/api/file/processed/"

# Image Class contains all the information about the image (image, size(width & height) , image path, magnitude, phase)

# It also contains the methods to:
#  - Read the image from the uploaded folder in gray scale
#  - Resize the image to required size (default 300x200) if the image is not in the required size
#  - Calculate fourier transform of the image
#  - split fourier to magnitude and phase of the image
#  - Save the image in the processed folder
#  - Save the magnitude of the image in the processed folder
#  - Save the phase of the image in the processed folder
#    (the name of the image is the name of the uploaded image + the current date and time)
#  -  crop image magnitude and phase (crop in or crop out)


class Image:
    # Constructor of the class to initialize the width, height, magnitude and phase of the image
    def __init__(self , width=300, height=200):
        self.width = width
        self.height = height
        self.image_url = ""
        self.mag_url = ""
        self.phase_url = ""
        self.phase = 0
        self.mag = 1
        # original magnitude and phase to be used in crop method to overcome cropping on the cropped image
        self.original_phase = 0
        self.original_mag = 1
    
    # read method to read the image from the uploaded folder in gray scale and resize it to required size
    def read(self, image_path, name):
        self.name = name
        self.image_path = image_path
        self.image = cv2.imread(self.image_path, 0)
        if (self.image.shape[1] != self.width) or (self.image.shape[0] != self.height):
            self.image = cv2.resize(self.image, (self.width, self.height))
    
    # calculate_magnitude_and_phase method to calculate fourier transform of the image and split fourier to magnitude and phase of the image
    def calculate_magnitude_and_phase(self):
        # calculate fourier transform of the 2d image
        fftdata = fft2(self.image)
        # shift the zero frequency component to the center of the spectrum
        fftdata = fftshift(fftdata)
        # split fourier to magnitude and phase of the image
        self.mag = np.abs(fftdata)
        self.phase = np.angle(fftdata)
        self.original_mag = self.mag
        self.original_phase = self.phase
    
    # save method to save the image, magnitude of the image, phase of the image in the processed folder
    def save(self):
        # get the current date and time to be used in the name of the image
        now = datetime.now()
        file_date = now.strftime("%m/%d/%Y, %H:%M:%S")
        file_date = secure_filename(file_date)
        # set the url of the image, magnitude of the image, phase of the image to be used in the response
        self.image_url = processedImagePath+self.name+file_date+".png"
        self.mag_url = processedImagePath+self.name+file_date+"_mag.png"
        self.phase_url = processedImagePath + self.name+file_date+"_phase.png"
        # set the path of the image, magnitude of the image, phase of the image to be used in saving the image
        self.image_path = f".\\storage\\processed\\{self.name+file_date}.png"
        self.image_mag_path = f".\\storage\\processed\\{self.name+file_date}_mag.png"
        self.image_phase_path = f".\\storage\\processed\\{self.name+file_date}_phase.png"
        # save the image, magnitude of the image, phase of the image in the processed folder
        plt.imsave(self.image_path, self.image, cmap='gray')
        plt.imsave(self.image_mag_path, np.log(self.mag), cmap='gray')
        plt.imsave(self.image_phase_path, self.phase, cmap='gray')

    # crop_mag_and_phase method to crop image magnitude and phase (crop in or crop out)
    def crop_mag_and_phase(self, select_in, **dimenions ):
        # calculate the x1, x2, y1, y2 of the selected area
        x1 = int(dimenions["x"] * self.width / 100)
        x2 = int(x1 + (dimenions["width"] * self.width / 100))
        y2 = int((100 - dimenions["y"]) * self.height / 100)
        y1 = int(y2 - (dimenions["height"] * self.height / 100))

        # check if it is required to:
        #  -select in and crop out
        #  -select out and crop in
        if select_in  :
            print("Seleect in")
            self.mag = np.zeros_like(self.original_mag)
            self.phase = np.zeros_like(self.original_phase)
            self.mag[self.height-1-y2 : self.height-1-y1 , x1:x2] = self.original_mag[self.height-1-y2 : self.height-1-y1 , x1:x2]
            self.phase[self.height-1-y2 : self.height-1-y1 , x1:x2] = self.original_phase[self.height-1-y2 : self.height-1-y1 , x1:x2]
        elif not select_in :
            self.mag = np.copy(self.original_mag)
            self.phase = np.copy(self.original_phase)
            self.mag[self.height-1-y2 : self.height-1-y1 , x1:x2] = 0
            self.phase[self.height-1-y2 : self.height-1-y1 , x1:x2] = 0
