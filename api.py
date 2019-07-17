from flask import Flask, request, jsonify
from flask_restful import Api, Resource
from main import AnimalDecisionTree


app = Flask(__name__)
API = Api(app)

class SEND_PREDICTION(Resource):
    def __init__(self):
        self.tree = AnimalDecisionTree(trained=True)
    def get(self):
        return jsonify({"message": "working"})
    def post(self):
        print("Reçu le contenu du client")
        content = request.json
        print("Appel du modèle...")
        prediction = self.tree.predict(content)
        print("Envoi...")
        return jsonify({"content": content,
                        "message": prediction})

API.add_resource(SEND_PREDICTION, "/send")

if __name__ == "__main__":
    app.run(debug=True, host="192.168.1.192")