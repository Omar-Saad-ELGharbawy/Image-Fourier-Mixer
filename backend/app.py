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
    img.read(img_url,get_image_name(file))
    img.calculate_magnitude_and_phase()
    img.save()

    if (data["type"] == "1"):
        Processing.img1 = img
    elif (data["type"] == "2"):
        Processing.img2 = img

    return {"img_url": processedImagePath+get_image_name(file)+'.png', "mag_url": processedImagePath+get_image_name(file)+"_mag.png", "phase_url": processedImagePath+get_image_name(file)+"_phase.png"}, 200
# ----------------------------------------------------------------------------------------------------------------------#

# ----------------------------------------------------------------------------------------------------------------------#
# API description:
#       Fuction: Update the file to the server
#       Return: File URL

@ app.route("/api/update", methods=['POST'])
def update():

    # get request data
    data = request.get_json()

    # # get the dimensions
    # dimensions = data["dimensions"]
    # type = data["type"]  # 1 or 2
    # print(dimensions, type)

    # if (data["type"] == 1):
    #     print("Cropping in 1")
    #     Processing.img1.crop_mag_and_phase(**dimensions)
    #     Processing.img1.save()

    # elif (data["type"] == 2):
    #     print("Cropping in 2")
    #     Processing.img2.crop_mag_and_phase(**dimensions)
    #     Processing.img2.save()

    Processing.phase1 = data["phase_1_selected"]
    Processing.phase2 = data["phase_2_selected"]
    Processing.mag1 = data["mag_1_selected"]
    Processing.mag2 = data["mag_2_selected"]

    print(Processing.phase1, Processing.phase2, Processing.mag1, Processing.mag2)

    Processing.select_and_save_mixed_img()
    # if (phase1 and not mag2):
    #     Processing.save_mixed_image(
    #         1, Processing.img1.phase)
    # elif (phase2 and not mag1):
    #     Processing.save_mixed_image(
    #         1, Processing.img2.phase)
    # elif (mag1 and not phase2):
    #     Processing.save_mixed_image(
    #         Processing.img1.mag, 0)
    # elif (mag2 and not phase1):
    #     Processing.save_mixed_image(
    #         Processing.img2.mag, 0)
    # elif (mag1 and phase2):
    #     Processing.save_mixed_image(
    #         Processing.img1.mag, Processing.img2.phase)
    # elif (mag2 and phase1):
    #     Processing.save_mixed_image(
    #         Processing.img2.mag, Processing.img1.phase)

    return {"mixed_img": processedImagePath+'mixed_img.png'}, 200
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
    print(dimensions, type)
    if (data["type"] == 1):
        print("Cropping in 1")
        Processing.img1.crop_mag_and_phase(**dimensions)
        Processing.img1.save()
        name = Processing.img1.name
        # print(Processing.img1.phase)
        # cropped_phase_1 = Processing.crop_2d_img(Processing.img1.phase,**dimensions)
        # cropped_mag_1 = Processing.crop_2d_img(Processing.img1.mag,**dimensions)
    elif (data["type"] == 2):
        # cropped_phase_2 = Processing.crop_2d_img(Processing.img2.phase,**dimensions)
        # cropped_mag_2 = Processing.crop_2d_img(Processing.img2.mag,**dimensions)
        Processing.img2.crop_mag_and_phase(**dimensions)
        Processing.img2.save()
        name = Processing.img2.name

    Processing.select_and_save_mixed_img()
    # update()
    # Processing.save_mixed_image(Processing.img1.phase,Processing.img2.mag)

    # phase1 = data["phase_1_selected"]
    # phase2 = data["phase_2_selected"]
    # mag1 = data["mag_1_selected"]
    # mag2 = data["mag_2_selected"]

    # # print(phase1, phase2, mag1, mag2)
    # if (phase1 and not mag2):
    #     Processing.save_mixed_image(
    #         1, Processing.img1.phase)
    # elif (phase2 and not mag1):
    #     Processing.save_mixed_image(
    #         1, Processing.img2.phase)
    # elif (mag1 and not phase2):
    #     Processing.save_mixed_image(
    #         Processing.img1.mag, 0)
    # elif (mag2 and not phase1):
    #     Processing.save_mixed_image(
    #         Processing.img2.mag, 0)
    # elif (mag1 and phase2):
    #     Processing.save_mixed_image(
    #         Processing.img1.mag, Processing.img2.phase)
    # elif (mag2 and phase1):
    #     Processing.save_mixed_image(
    #         Processing.img2.mag, Processing.img1.phase)
    

    return {"mixed_img": processedImagePath+'mixed_img.png' , "img_url": processedImagePath+name+'.png', "mag_url": processedImagePath+name+"_mag.png", "phase_url": processedImagePath+name+"_phase.png"}, 200
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
