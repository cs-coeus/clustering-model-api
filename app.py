import os
from dotenv import dotenv_values
from flask import Flask, jsonify, request

from models.model import ModelClustering

is_production = os.environ.get('FLASK_ENV') == 'production'
authentication_token = os.environ.get('AUTHORIZATION_KEY')
config = dotenv_values(".env")

model = ModelClustering()
app = Flask(__name__)


@app.route('/healthcheck')
def health_check():
    return 'OK'


@app.route('/predict/agglomerative-clustering', methods=['POST'])
def predict_agglomerative_clustering():
    if request.method == 'POST' and request.json is not None:
        if is_production:
            token = request.headers.get('Authorization').split(' ')[1]
            if token != authentication_token:
                return jsonify({"error": "Unauthorized request"}), 403
        data = request.json['data']
        if data is not None:
            try:
                result = model.predict(data)
                return jsonify({"result": result})
            except Exception as e:
                print(data, flush=True)
                print(e, flush=True)
                return jsonify({"error": "Data format wrong"}), 400
    return jsonify({"error": "Data is invalid or not exist"}), 400

@app.route('/predict/k-medoids', methods=['POST'])
def predict_k_medoids():
    if request.method == 'POST' and request.json is not None:
        if is_production:
            token = request.headers.get('Authorization').split(' ')[1]
            if token != authentication_token:
                return jsonify({"error": "Unauthorized request"}), 403
        data = request.json['data']
        if data is not None:
            try:
                result = model.k_medoids_clustering(data)
                return jsonify({"result": result})
            except Exception as e:
                print(data, flush=True)
                print(e, flush=True)
                return jsonify({"error": "Data format wrong"}), 400
    return jsonify({"error": "Data is invalid or not exist"}), 400