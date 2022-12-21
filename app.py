#import  libraries---------------------------------------------------------
from flask import Flask , render_template
from functions import *

flasklink = Flask(__name__)

@flasklink.route('/')
def index():
	return render_template('Home.html',custom_css = "home")
    
# run our programe
if __name__== "__main__":  #for make this content appear when file open directly not importent from another file
    flasklink.run(debug=True, port=9000)