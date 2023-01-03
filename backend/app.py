# Description: This file contains the Flask APIs that receives files from the client and saves it in the server.

from flask import Flask, request, send_from_directory
from flask_cors import CORS
import os.path
from processing import Processing
from image import Image

# ----------------------------------------------------------------------------------------------------------------------#
# Configurations
app = Flask(__name__)

# set the folders to save the original and processed images
originalImgsFolder = '.\\storage\\original\\'
processedImgsFolder = '.\\storage\\processed\\'

app.config['originalImgsFolder'] = originalImgsFolder
app.config['processedImgsFolder'] = processedImgsFolder

originalImagePath = "http://127.0.0.1:5000/api/file/original/"
processedImagePath = "http://127.0.0.1:5000/api/file/processed/"

CORS(app)

ALLOWED_EXTENSIONS = {'png', 'jpeg', 'jpg'}   # Extension Allowed
# ----------------------------------------------------------------------------------------------------------------------#

# -------------------------------------------------------- Methods -----------------------------------------------------#

# ----------------------------------------------------------------------------------------------------------------------#
# function description:
#       Arguments: File name
#               check if the file has an allowed extension or not
#       Return: True or Flase
def allowed_file(filename):
    return '.' in filename and \
        filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
# ----------------------------------------------------------------------------------------------------------------------#

# function description:
#       Arguments: File
#               get the name of the file without the extension
#       Return: File name
def get_image_name(file):
    return file.filename.split('.')[0]

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

    if "type" not in request.form:
        return {"There is an error": 'err'}, 401

    data = request.form

    # check file extension
    if not allowed_file(file.filename):
        return {"err": "File format is not accepted"}, 402

    # save the file to the server
    img_path = os.path.join(originalImgsFolder, file.filename)
    file.save(img_path)
    img_url = originalImgsFolder + file.filename

    # create an image object
    img = Image()
    # read the image
    img.read(img_url, get_image_name(file))
    img.calculate_magnitude_and_phase()
    # save the image to the server
    img.save()

    # check the type (image1 or image2) of the upload image and store it in the static object
    if (data["type"] == "1"):
        Processing.img1 = img
    elif (data["type"] == "2"):
        Processing.img2 = img
    # return the pathes to the frontend
    return Processing.getPaths(), 200
# ----------------------------------------------------------------------------------------------------------------------#

# ----------------------------------------------------------------------------------------------------------------------#
# API description:
#       Fuction: Update the file to the server
#       Return: File URL


@ app.route("/api/update", methods=['POST'])
def update():

    # get request data
    data = request.get_json()
    # store the selected components of the images (magnitude or phase) in the static object flags
    Processing.phase1 = data["phase_1_selected"]
    Processing.phase2 = data["phase_2_selected"]
    Processing.mag1 = data["mag_1_selected"]
    Processing.mag2 = data["mag_2_selected"]
    # check the selected components of the images and save the mixed image
    Processing.select_and_save_mixed_img()
    # return the pathes to the frontend
    return Processing.getPaths(), 200
# ----------------------------------------------------------------------------------------------------------------------#


# ----------------------------------------------------------------------------------------------------------------------#
# API description:
#       Fuction: Crop image magnitude and phase 
#       Return: File URL
@ app.route("/api/crop", methods=['POST'])
def crop():

    # get request data
    data = request.get_json()

    # get the dimensions
    dimensions = data["dimensions"]
    type = data["type"]  # 1 or 2
    isSelectIn = data["isSelectIn"]  # True or False
    #  check the selected image and crop its magnitude and phase
    if (type == 1):
        print("Cropping in 1")
        Processing.img1.crop_mag_and_phase( isSelectIn , **dimensions)
    elif (type == 2):
        print("Cropping in 2")
        Processing.img2.crop_mag_and_phase( isSelectIn , **dimensions)
    # save the mixed image
    Processing.select_and_save_mixed_img()
    # return the pathes to the frontend
    return Processing.getPaths(), 200
# ----------------------------------------------------------------------------------------------------------------------#

# ----------------------------------------------------------------------------------------------------------------------#
# API description:
#       Fuction: delete the selected image
#       Return: File URL
@ app.route("/api/delete", methods=['POST'])
def delete():
    # get request data
    data = request.form
    type = data["type"]  # 1 or 2

    # check the selected image and delete it and create a new empty image object
    if (type == "1"):
        Processing.img1 = Image()
    elif (type == "2"):
        Processing.img2 = Image()
    # save the mixed image after deleting image 1 or 2
    Processing.select_and_save_mixed_img()
    # return the pathes to the frontend
    return Processing.getPaths(), 200
# ----------------------------------------------------------------------------------------------------------------------#


# ----------------------------------------------------------------------------------------------------------------------#
# API description:
#       Fuction: Download the file from the server
#       Return: File
@ app.route('/api/file/<proccessed>/<file_name>', methods=['GET'])
def file(file_name, proccessed):
    if request.method == 'GET':
        if proccessed == 'original':
            return send_from_directory(app.config['originalImgsFolder'], file_name)
        elif proccessed == 'processed':
            return send_from_directory(directory=app.config['processedImgsFolder'], path=file_name), 200

# ----------------------------------------------------------------------------------------------------------------------#


# ----------------------------------------------------------------------------------------------------------------------#
# Run the app
if __name__ == "__main__":
    # debug = true --> if the app has any error they will pop up on the web page
    app.run(debug=True)
# ----------------------------------------------------------------------------------------------------------------------#


# Senirio 1: Upload image 1 => Resize img1 + save it + mag + phase
# Senirio 2: Upload image 2 and Image 1 uploaded =>
# Senirio 3: Select type(Mag/Phase) =>
# Senirio 3: Crop image1/2 =>
