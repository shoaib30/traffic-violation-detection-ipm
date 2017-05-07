#!flask/bin/python
from flask import Flask
from flask import request
import Main
from shutil import copyfile
app = Flask(__name__)

@app.route('/')
def index():
    return "Traffic Violation Detection Image Processing Module"

@app.route('/process-number-plate', methods=['GET'])
def processNumberPlate():
    fi = request.args.get('fileName') + ".jpg"
    fileName = "/home/pi/traffic-violation-detector-cm/" + fi
    print "Processing file: " + fileName
    
    status = Main.main(fileName)
    if(status.startswith("Error")):
        copyLoc = "/home/pi/traffic-violation-detection-fi/app/" + fi 
        copyfile(fileName, copyLoc)
        print "Error"
        return "error"
    else:
        return status    
    #return "KA03MZ1557", 200

if __name__ == '__main__':
    app.run(debug=True, port=3002)
