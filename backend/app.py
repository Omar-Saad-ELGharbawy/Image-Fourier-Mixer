# Description: This file contains the Flask APIs that receives files from the client and saves it in the server.

from flask import Flask, request, send_from_directory
from flask_cors import CORS
import os.path
from processing import Processing
from image import Image

# ----------------------------------------------------------------------------------------------------------------------#
# Configurations
app = Flask(__name__)

originalImgsFolder = '.\\storage\\original\\'
processedImgsFolder = '.\\storage\\processed\\'

app.config['originalImgsFolder'] = originalImgsFolder
app.config['processedImgsFolder'] = processedImgsFolder

originalImagePath = "http://127.0.0.1:5000/api/file/original/"
processedImagePath = "http://127.0.0.1:5000/api/file/processed/"

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

    img = Image()
    img.read(img_url, get_image_name(file))
    img.calculate_magnitude_and_phase()
    img.save()

    if (data["type"] == "1"):
        Processing.img1 = img
    elif (data["type"] == "2"):
        Processing.img2 = img

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

    Processing.phase1 = data["phase_1_selected"]
    Processing.phase2 = data["phase_2_selected"]
    Processing.mag1 = data["mag_1_selected"]
    Processing.mag2 = data["mag_2_selected"]

    print(Processing.phase1, Processing.phase2,
          Processing.mag1, Processing.mag2)

    Processing.select_and_save_mixed_img()

    return Processing.getPaths(), 200
# ----------------------------------------------------------------------------------------------------------------------#


# ----------------------------------------------------------------------------------------------------------------------#
# API description:
#       Fuction: Upload the file to the server
#       Return: File URL
@ app.route("/api/crop", methods=['POST'])
def crop():

    # get request data
    data = request.get_json()

    # get the dimensions
    dimensions = data["dimensions"]
    type = data["type"]  # 1 or 2
    isSelectIn = data["isSelectIn"]  # True or False

    print(dimensions, type, isSelectIn)

    if (data["type"] == 1):
        print("Cropping in 1")
        Processing.img1.crop_mag_and_phase( isSelectIn , **dimensions)
        # Processing.img1.save()

    elif (data["type"] == 2):
        print("Cropping in 2")
        Processing.img2.crop_mag_and_phase( isSelectIn , **dimensions)
        # Processing.img2.save()

    Processing.select_and_save_mixed_img()

    return Processing.getPaths(), 200
# ----------------------------------------------------------------------------------------------------------------------#

# ----------------------------------------------------------------------------------------------------------------------#
# API description:
#       Fuction: Upload the file to the server
#       Return: File URL


@ app.route("/api/delete", methods=['POST'])
def delete():
    print("delete called")
    # get request data
    data = request.form
    print("get json called")
    # get the dimensions
    type = data["type"]  # 1 or 2
    print("type called")
    print(type)

    if (data["type"] == "1"):
        Processing.img1 = Image()

    elif (data["type"] == "2"):
        Processing.img2 = Image()

    Processing.select_and_save_mixed_img()

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
