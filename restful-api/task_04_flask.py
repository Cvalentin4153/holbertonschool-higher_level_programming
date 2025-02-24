from flask import Flask, jsonify, request

app = Flask(__name__)

users = {
    "jane": {"username": "jane", "name": "Jane", "age": 28, "city": "Los Angeles"},
    "john": {"username": "john", "name": "John", "age": 30, "city": "New York"}
}

@app.route("/")
def home():
    return "Welcome to the Flask API!"

@app.route("/data")
def get_usernames():
    if not users:
        return jsonify([])
    return jsonify(list(users.keys()))

@app.route("/status")
def status():
    return "OK"

@app.route("/users/<username>")
def get_user(username):
    user = users.get(username)
    if user:
        return jsonify(user)
    return jsonify({"error": "User not found"}), 404

@app.route("/add_user", methods=["POST"])
def add_user():
    data = request.get_json()

    if not data:
        return jsonify({"error": "Invalid JSON data"}), 400

    if "username" not in data or not data["username"].strip():
        return jsonify({"error": "Username is required"}), 400

    username = data["username"].strip().lower()

    if username in users:
        return jsonify({"error": "User already exists"}), 400

    name = data.get("name", "Unknown")
    age = data.get("age", 0)
    city = data.get("city", "Unknown")

    users[username] = {"username": username, "name": name, "age": age, "city": city}

    return jsonify({"message": "User added", "user": users[username]}), 201

if __name__ == "__main__":
    app.run(debug=True)
