from flask import Flask, request

app = Flask(__name__)

data = {
    1401: {'name': 'Aba Quaye', 'grade': 'A'},
    1652: {'name': 'Mark Brown', 'grade': 'B'},
    1913: {'name': 'Dave Sam', 'grade': 'E'},
    1004: {'name': 'Marthe Grey', 'grade': 'A'},
    }

@app.route('/')
def hello_world():
    return "Hello World"

@app.route('/all_data', methods=['GET'])
def getAll():
    return data

@app.route('/data/<int:id>', methods=['GET'])
def get_id(id):
    return data[id]

@app.route('/newRecord', methods= ['POST'])
def createData():
    newRec = request.get_json()
    print(newRec)
    return newRec



app.run(debug=True)