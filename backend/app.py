# Description: This file contains the Flask APIs that receives files from the client and saves it in the server.

from flask import Flask, request, send_from_directory
from flask_cors import CORS
import os.path

import numpy as np
from scipy.fft import  rfft2, irfft2,fft2,ifft2 , fftshift , ifftshift
from scipy.fftpack import ifftshift

import cv2
import pylab
from matplotlib import pyplot as plt

# # from processing.py import *
# import sys
# # caution: path[0] is reserved for script path (or '' in REPL)
# # sys.path.insert(1, 'backend\processing.py')
# sys.path.append('C:\Users\Lenovo\Desktop\main dsp 4\DSP_TASK_4\backend') 
# from processing import *

uploade_img1_path = r"data/upload_images/human_back.jpg"
uploade_img2_path = r"data\upload_images\jamal.png"

# ----------------------------------------------------------------------------------------------------------------------#
# Configurations
app = Flask(__name__)

originalImgsFolder = '.\\storage\\original'
processedImgsFolder = '.\\storage\\processed'

app.config['originalImgsFolder'] = originalImgsFolder
app.config['processedImgsFolder'] = processedImgsFolder

CORS(app)

ALLOWED_EXTENSIONS = {'png', 'jpeg', 'jpg'}   # Extension Allowed
# ----------------------------------------------------------------------------------------------------------------------#

# ----------------------------------------------------------------------------------------------------------------------#
# function description:
#       Arguments: File name
#               check if the file has an allowed extension or not
#       Return: True or Flase
def allowed_file(filename):
    return '.' in filename and \
        filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
# ----------------------------------------------------------------------------------------------------------------------#


# -------------------------------------------------------- Methods -----------------------------------------------------#
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

def save_3_images(image,fftmag,fftangle,name):
    img_mag = ifftshift(np.multiply(fftmag,1))
    img_mag = ifft2(img_mag)
    img_phase = ifftshift(1 * np.exp(np.multiply(1j,fftangle)))
    img_phase = ifft2(img_phase)
    plt.imsave(f"C:\\Users\\Lenovo\\Desktop\\main dsp 4\\DSP_TASK_4\\backend\\storage\\processed\\{name}.png",image, cmap='gray')
    plt.imsave(f"C:\\Users\\Lenovo\\Desktop\\main dsp 4\\DSP_TASK_4\\backend\\storage\\processed\\{name}_mag.png",img_mag.real, cmap='gray')
    plt.imsave(f"C:\\Users\\Lenovo\\Desktop\\main dsp 4\\DSP_TASK_4\\backend\\storage\\processed\\{name}_phase.png",img_phase.real, cmap='gray')

def save_mixed_image(img_mag_data,img_angle_data):
    mixed_img = ifftshift(np.multiply(img_mag_data,np.exp(np.multiply(1j,img_angle_data))))
    mixed_img = np.abs(ifft2(mixed_img))
    plt.imsave("data\processed\mixed_img.png",mixed_img, cmap='gray')

# ----------------------------------------------------------------------------------------------------------------------#

# ----------------------------------------------------------------------------------------------------------------------#
# API description:
#       Fuction: Upload the file to the server
#       Return: File URL
@app.route("/api/upload", methods=['POST'])
def upload_file():
    # check if the post request has the file part
    if "file" not in request.files:
        return {"There is an error": 'err'}, 401

    # get the file
    file = request.files["file"]

    # check file extension
    if not allowed_file(file.filename):
        return {"err": "File format is not accepted"}, 400

    # save the file to the server
    signalPath = os.path.join(originalImgsFolder, file.filename)
    file.save(signalPath)
    img_url="http://127.0.0.1:5000/api/file/" + file.filename

    # Read images
    image= read_and_resize_image(img_url,600,900)

    # get magnitude and phase components of images
    img_magnitude , img_phase = get_img_magnitude_phase(image)

    # Save magnitude and phase images
    save_3_images(image,img_magnitude,img_phase,"image1")

    return {"file_url": img_url, }, 200
# ----------------------------------------------------------------------------------------------------------------------#

# ----------------------------------------------------------------------------------------------------------------------#
# API description:
#       Fuction: Upload the file to the server
#       Return: File URL
@app.route("/api/update", methods=['POST'])
def update():

    # get request data
    data = request.get_json()

    # get the dimensions
    dimensions = data["dimensions"]

    return {"dimensions": dimensions}, 200
# ----------------------------------------------------------------------------------------------------------------------#


# ----------------------------------------------------------------------------------------------------------------------#
# API description:
#       Fuction: Download the file from the server
#       Return: File
@app.route('/api/file/<file_name>', methods=['GET'])
def file(file_name):
    if request.method == 'GET':
        return send_from_directory(directory=app.config['processedImgsFolder'], path=file_name), 200

# ----------------------------------------------------------------------------------------------------------------------#


# ----------------------------------------------------------------------------------------------------------------------#
# Run the app
if __name__ == "__main__":
    # debug = true --> if the app has any error they will pop up on the web page
    app.run(debug=True)
# ----------------------------------------------------------------------------------------------------------------------#


# Upload => File + (img1 or img2)
# Update dimesions + type +
# Update type



# Mix 2 defualt imgs

# if img1 sent => img1 + def img
# if img2 sent => img2 + def img
# if img1 and img 2 sent => img1 + img2
