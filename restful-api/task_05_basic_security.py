from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import (
    JWTManager, create_access_token,
    jwt_required, get_jwt_identity, get_jwt
)
from datetime import timedelta

app = Flask(__name__)
auth = HTTPBasicAuth()

# Configure JWT
app.config["JWT_SECRET_KEY"] = "super-secret-key"   # Change this in production!
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(hours=1)
jwt = JWTManager(app)

# In-memory user store (username -> user data)
users = {
    "user1": {
        "username": "user1",
        "password": generate_password_hash("password"),
        "role": "user"
    },
    "admin1": {
        "username": "admin1",
        "password": generate_password_hash("password"),
        "role": "admin"
    }
}

########################################
# 1. Basic Authentication
########################################
@auth.verify_password
def verify_password(username, password):
    """
    Called by Flask-HTTPAuth to verify username/password.
    Returns the username if valid, None otherwise.
    """
    user = users.get(username)
    if not user:
        return None
    if check_password_hash(user["password"], password):
        return username  # Authentication successful
    return None         # Authentication failed

@app.route("/basic-protected")
@auth.login_required
def basic_protected():
    """
    A route protected by Basic Auth.
    Returns 401 Unauthorized if credentials are missing or invalid.
    """
    return "Basic Auth: Access Granted"

########################################
# 2. JWT Authentication
########################################
@app.route("/login", methods=["POST"])
def login():
    """
    Logs a user in using username/password and returns a JWT token if valid.
    """
    data = request.get_json()
    if not data or "username" not in data or "password" not in data:
        return jsonify({"error": "Username and password required"}), 400

    username = data["username"]
    password = data["password"]
    user = users.get(username)

    if user and check_password_hash(user["password"], password):
        # Generate a new JWT token
        access_token = create_access_token(
            identity=user["username"],  # The identity is typically the username
            additional_claims={"role": user["role"]}  # We embed the role in the token
        )
        return jsonify({"access_token": access_token}), 200
    else:
        return jsonify({"error": "Invalid credentials"}), 401

@app.route("/jwt-protected")
@jwt_required()
def jwt_protected():
    """
    A route protected by JWT.
    Returns 401 Unauthorized if token is invalid or missing.
    """
    return "JWT Auth: Access Granted"

@app.route("/admin-only")
@jwt_required()
def admin_only():
    """
    A route protected by JWT, but also checks the user's role.
    Returns 403 Forbidden if the user is not an admin.
    """
    # Get user role from token claims
    claims = get_jwt()
    if claims.get("role") != "admin":
        return jsonify({"error": "Admin access required"}), 403

    return "Admin Access: Granted"

########################################
# 3. Custom Error Handlers for JWT
########################################
@jwt.unauthorized_loader
def handle_unauthorized_error(err):
    """
    Missing/invalid token in the request.
    """
    return jsonify({"error": "Missing or invalid token"}), 401

@jwt.invalid_token_loader
def handle_invalid_token_error(err):
    """
    Token is not well-formed or has invalid signature.
    """
    return jsonify({"error": "Invalid token"}), 401

@jwt.expired_token_loader
def handle_expired_token_error(jwt_header, jwt_payload):
    """
    Token has expired.
    """
    return jsonify({"error": "Token has expired"}), 401

@jwt.revoked_token_loader
def handle_revoked_token_error(jwt_header, jwt_payload):
    """
    Token has been revoked (not used in this example, but provided as reference).
    """
    return jsonify({"error": "Token has been revoked"}), 401

@jwt.needs_fresh_token_loader
def handle_needs_fresh_token_error(jwt_header, jwt_payload):
    """
    Token is valid but not 'fresh' (not used in this example).
    """
    return jsonify({"error": "Fresh token required"}), 401

########################################
# 4. Run the Flask App
########################################
if __name__ == "__main__":
    app.run(debug=True)
