from flask import Flask, jsonify
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

# Create a BasicAuth instance
auth = HTTPBasicAuth()

# Example in-memory user store with hashed passwords
users = {
    "user1": generate_password_hash("password"),
    "admin1": generate_password_hash("password")
}

@auth.verify_password
def verify_password(username, password):
    """
    This function is called automatically to verify the user's credentials.
    Return the username if valid, otherwise return None.
    """
    if username in users and check_password_hash(users[username], password):
        return username
    return None

@auth.error_handler
def unauthorized():
    """
    If authentication fails or credentials are missing,
    Flask-HTTPAuth will call this function to return a 401 response.
    """
    return jsonify({"error": "Unauthorized"}), 401

@app.route("/basic-protected")
@auth.login_required
def basic_protected():
    """
    A route that requires valid Basic Auth credentials.
    If no credentials or wrong credentials are provided,
    it will return a 401 response.
    """
    return "Basic Auth: Access Granted"

# Optional: You can add a simple root endpoint for testing
@app.route("/")
def home():
    return "Home - No Auth Needed"

if __name__ == "__main__":
    # Run in debug mode for easier troubleshooting
    app.run(debug=True, host="0.0.0.0", port=5000)
