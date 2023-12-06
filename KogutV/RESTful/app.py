from flask import Flask, request, jsonify
from utility import get_assets, add_asset, update_asset, delete_asset

app = Flask(__name__)

@app.route('/assets', methods=['GET'])
def get_assets_route():
    return jsonify(get_assets())

@app.route('/assets', methods=['POST'])
def add_asset_route():
    new_asset = request.json
    return jsonify(add_asset(new_asset))

@app.route('/assets/<int:asset_id>', methods=['PATCH'])
def update_asset_route(asset_id):
    update_info = request.json
    return jsonify(update_asset(asset_id, update_info))

@app.route('/assets/<int:asset_id>', methods=['DELETE'])
def delete_asset_route(asset_id):
    return jsonify(delete_asset(asset_id))

if __name__ == '__main__':
    app.run(debug=True)
