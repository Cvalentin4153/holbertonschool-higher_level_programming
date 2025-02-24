from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory user database
users = {
    "jane": {"username": "jane", "name": "Jane", "age": 28, "city": "Los Angeles"},
    "john": {"username": "john", "name": "John", "age": 30, "city": "New York"}
}

@app.route("/")
def home():
    return "Welcome to the Flask API!"

@app.route("/data")
def get_usernames():
    return jsonify(list(users.keys())) if users else jsonify([])

@app.route("/status")
def status():
    return "OK"

@app.route("/users/<username>")
def get_user(username):
    user = users.get(username.lower())  # Normalize lookup
    if user:
        return jsonify(user)
    return jsonify({"error": "User not found"}), 404

@app.route("/add_user", methods=["POST"])
def add_user():
    try:
        data = request.get_json(force=True)
    except:
        return jsonify({"error": "Invalid JSON data"}), 400

    if not data or "username" not in data or not data["username"].strip():
        return jsonify({"error": "Username is required"}), 400

    username = data["username"].strip().lower()  # Normalize username

    if username in users:
        return jsonify({"error": "User already exists"}), 400

    users[username] = {
        "username": username,
        "name": data.get("name", "Unknown"),
        "age": data.get("age", 0),
        "city": data.get("city", "Unknown")
    }

    return jsonify({"message": "User added", "user": users[username]}), 201

if __name__ == "__main__":
    app.run(debug=True)
