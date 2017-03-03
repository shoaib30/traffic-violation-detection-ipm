#!flask/bin/python
from flask import Flask
from flask import request
app = Flask(__name__)

@app.route('/')
def index():
    return "Traffic Violation Detection Image Processing Module"

@app.route('/process-number-plate', methods=['GET'])
def processNumberPlate():
    fileName = request.args.get('fileName')
    print "Processing file: " + fileName
    return "KA03MZ1557", 200

if __name__ == '__main__':
    app.run(debug=True, port=3002)
