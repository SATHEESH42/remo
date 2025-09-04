from flask import Flask, request, jsonify

app = Flask(__name__)

# Sample data: list of apps
apps = [
    {"id": 1, "name": "ChatApp", "category": "Social", "rating": 4.5},
    {"id": 2, "name": "PhotoEditor", "category": "Photography", "rating": 4.2},
    {"id": 3, "name": "GameZone", "category": "Games", "rating": 4.8}
]

@app.route('/apps', methods=['GET'])
def get_apps():
    return jsonify(apps)

@app.route('/apps/<int:app_id>', methods=['GET'])
def get_app(app_id):
    app_data = next((app for app in apps if app["id"] == app_id), None)
    if app_data:
        return jsonify(app_data)
    return jsonify({"error": "App not found"}), 404

@app.route('/apps', methods=['POST'])
def add_app():
    new_app = request.json
    new_app["id"] = max(app["id"] for app in apps) + 1 if apps else 1
    apps.append(new_app)
    return jsonify(new_app), 201

@app.route('/apps/<int:app_id>', methods=['PUT'])
def update_app(app_id):
    app_data = next((app for app in apps if app["id"] == app_id), None)
    if not app_data:
        return jsonify({"error": "App not found"}), 404
    update_data = request.json
    app_data.update(update_data)
    return jsonify(app_data)

@app.route('/apps/<int:app_id>', methods=['DELETE'])
def delete_app(app_id):
    global apps
    apps = [app for app in apps if app["id"] != app_id]
    return jsonify({"message": "App deleted"})

if __name__ == '__main__':
    app.run(debug=True)