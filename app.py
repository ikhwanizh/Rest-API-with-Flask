# import library
from flask import Flask, request
from flask_restful import Resource, Api
from flask_cors import CORS

# Create an instance of Flask
app = Flask(__name__)
# Create the API
api = Api(app)
# Enable CORS
CORS(app)

# Create dictionary to store data
identitiy = {}

# Create a resource


class contohResource(Resource):
    def get(self):
        # response = {"msg": "hello world!"}
        return identitiy

    def post(self):
        name = request.form['name']
        age = request.form['age']
        identitiy["name"] = name
        identitiy["age"] = age
        response = {"msg": "data berhasil diinput"}
        return response


# Setup resource
api.add_resource(contohResource, '/contoh', methods=['GET', 'POST'])

# Run the app
if __name__ == '__main__':
    app.run(debug=True, port=5005)
