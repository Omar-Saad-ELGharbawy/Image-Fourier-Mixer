# Description: This file contains the Flask APIs that receives files from the client and saves it in the server.

from flask import Flask, request, send_from_directory
from flask_cors import CORS
import os.path
from processing import Processing
from image import Image

# ----------------------------------------------------------------------------------------------------------------------#
# Configurations
app = Flask(__name__)

originalImgsFolder = '.\\storage\\original'
processedImgsFolder = '.\\storage\\processed'

app.config['originalImgsFolder'] = originalImgsFolder
app.config['processedImgsFolder'] = processedImgsFolder

originalImagePath = "http://127.0.0.1:5000/api/original/file/"
processedImagePath = "http://127.0.0.1:5000/api/processed/file/"

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
    return file.name.split('.')[0]

# ----------------------------------------------------------------------------------------------------------------------#

# ----------------------------------------------------------------------------------------------------------------------#
# API description:
#       Fuction: Upload the file to the server
#       Return: File URL


@app.route("/api/upload", methods=['POST'])
def upload_file():
    # print(request.files["file"])
    # print(request.get_json()['type'])
    # check if the post request has the file part
    if "file" not in request.files:
        return {"There is an error": 'err'}, 401

    # get the file
    file = request.files["file"]

    # get request data
    data = request.get_json()

    # check file extension
    if not allowed_file(file.filename):
        return {"err": "File format is not accepted"}, 402

    # save the file to the server
    img_path = os.path.join(originalImgsFolder, file.filename)
    file.save(img_path)
    img_url = originalImgsFolder + file.filename

    # img = Image()
    # img.read(img_url)
    # img.calculate_magnitude_and_phase()
    # img.save(get_image_name(file))

    # if (data["type"] == 1):
    #     Processing().img1 = img
    # elif (data["type"] == 2):
    #     Processing().img2 = img

    return {"img_url": processedImagePath+get_image_name(file), "mag_url": processedImagePath+get_image_name(file)+"_mag", "phase_url": processedImagePath+get_image_name(file)+"_phase"}, 200
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
@app.route('/api/file/<proccessed>/<file_name>', methods=['GET'])
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
