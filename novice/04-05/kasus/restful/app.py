from flask import Flask
from flask_restful import Resource, Api
from flask import jsonify

app = Flask(__name__)
api = Api(app)

class book(Resource):
    def get(self):
        res = {'Title': 'Gang of Four', 
               'Writer': 'Erich Gamma, Richard Helm, Ralph Johnson, John Vlissides', 
               'Author': 'Addison-Wesley',
               'Year': '1994'}
        return jsonify(res)

api.add_resource(book, '/get')

if __name__ == '__main__':    
    app.run(debug=True)