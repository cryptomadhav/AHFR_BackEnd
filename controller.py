from flask import Flask, jsonify, request
import os
from handwritten_recognition import *

PATH_NAME = 'C:/Users/Madhav/workspace/AHFR_BackEnd/'

ALLOWED_EXTENSIONS = {'png'}

# initialize our Flask application
app= Flask("__name__")
# Set upload file size limit to 16MB
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

@app.route("/", methods=["GET"])
def message():
    return jsonify("Service is live!! Hit /img_to_json to process image!!")

@app.route("/img_to_json", methods=["GET"])
def img_to_json():
    print("Posted file: {}".format(request))
    img = request.files['image']
    img.filename = 'file.' + img.filename.split(".")[-1]
    if allowed_file(img.filename) == False:
        return "File Format not allowed use only png, jpg, jpeg or tiff"
    print(os.path.join(PATH_NAME) + img.filename)
    img.save(os.path.join(PATH_NAME) + img.filename)
    os.system('python handwritten_recognition.py')
    return getJsonFromImage(img.filename)
    # return getJsonFromImage()
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

#  main thread of execution to start the server
if __name__=='__main__':
    app.run(debug=True)