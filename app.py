#!flask/bin/python
from flask import Flask
from flask import request
import ImageProcessing
app = Flask(__name__)

@app.route('/')
def index():
    return "Traffic Violation Detection Image Processing Module"

@app.route('/process-number-plate', methods=['GET'])
def processNumberPlate():
    fileName = "~/traffic-violation-detector/images/" + request.args.get('fileName')
    print "Processing file: " + fileName
    status = ImageProcessing.main(fileName)
    if(status.startswith("Error")):
        print "Error"
        return "error"
    else:
        return status    
    #return "KA03MZ1557", 200

if __name__ == '__main__':
    app.run(debug=True, port=3002)
