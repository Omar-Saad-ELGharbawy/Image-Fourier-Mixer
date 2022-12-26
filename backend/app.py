# Description: This file contains the Flask APIs that receives files from the client and saves it in the server.

from flask import Flask, request, send_from_directory
from flask_cors import CORS
import os.path


# ----------------------------------------------------------------------------------------------------------------------#
# Configurations
app = Flask(__name__)

originalImgsFolder = '.\\storage\\original'
processedImgsFolder = '.\\storage\\processed'

app.config['originalImgsFolder'] = originalImgsFolder
app.config['processedImgsFolder'] = processedImgsFolder

CORS(app)

ALLOWED_EXTENSIONS = {'png', 'jpeg'}   # Extension Allowed
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
#                                                 Write you methods here
# ----------------------------------------------------------------------------------------------------------------------#


# ----------------------------------------------------------------------------------------------------------------------#
# API description:
#       Fuction: Upload the file to the server
#       Return: File URL
@app.route("/api/upload", methods=['POST'])
def upload_file():
    # check if the post request has the file part
    if "file" not in request.files:
        return {"There is an error": 'err'}, 400

    # get the file
    file = request.files["file"]

    # check file extension
    if not allowed_file(file.filename):
        return {"err": "File format is not accepted"}, 400

    # save the file to the server
    signalPath = os.path.join(originalImgsFolder, file.filename)
    file.save(signalPath)

    return {"file_url": "http://127.0.0.1:5000/api/file/" + file.filename, }, 200
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
