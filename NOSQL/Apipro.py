from flask import Flask, jsonify, redirect, request
from pymongo import MongoClient

client=MongoClient('mongodb://localhost:27017/')
Db = client['MRECWAI']
Collection = Db['Students']

app = Flask(__name__)

@app.route('/')
def home():
    return "welcome to MRECWAI"

@app.route('/getStudents', methods=['GET'])
def get_all_students():
    result = []
    for stu in Collection.find():
        stu['_id'] = str(stu['_id'])
        result.append(stu)
    return jsonify(result)

@app.route('/addStudents', methods=['GET'])
def add_Student():
    data = request.get_json()
    result = Collection.insert_one(data)
    return jsonify({"message":"Students added", "id": str(result.inserted_id)}), 201



if __name__=='__main__':
    app.run(debug=True)