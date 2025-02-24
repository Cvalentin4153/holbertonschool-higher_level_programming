from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import (
    JWTManager, create_access_token, jwt_required,
    get_jwt_identity, get_jwt
)
from datetime import timedelta

app = Flask(__name__)
auth = HTTPBasicAuth()

# =========== JWT CONFIG ===========
app.config["JWT_SECRET_KEY"] = "super-secret-key"  # In production, use a stronger key!
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(hours=1)
jwt = JWTManager(app)

# =========== IN-MEMORY USER DATA ===========
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

# ===========================================
# 1) BASIC AUTHENTICATION
# ===========================================
@auth.verify_password
def verify_password(username, password):
    """
    Called by Flask-HTTPAuth to verify user credentials.
    Returns the 'username' if valid, otherwise None.
    """
    user = users.get(username)
    if user and check_password_hash(user["password"], password):
        return username
    return None

@auth.error_handler
def basic_auth_unauthorized():
    """
    Returns a 401 JSON response for basic auth failures.
    """
    return jsonify({"error": "Unauthorized"}), 401

@app.route("/basic-protected")
@auth.login_required
def basic_protected():
    """
    A route protected by Basic Auth.
    - If valid credentials => "Basic Auth: Access Granted"
    - If missing/invalid => 401
    """
    return "Basic Auth: Access Granted"

# ===========================================
# 2) JWT AUTHENTICATION
# ===========================================
@app.route("/login", methods=["POST"])
def login():
    """
    Logs in user with username/password, returns a JWT if valid.
    POST JSON: {"username":"...", "password":"..."}
    """
    data = request.get_json()
    if not data or "username" not in data or "password" not in data:
        return jsonify({"error": "Username and password required"}), 400

    username = data["username"]
    password = data["password"]

    user = users.get(username)
    if not user or not check_password_hash(user["password"], password):
        return jsonify({"error": "Invalid credentials"}), 401

    # Create JWT token, embedding the user's role
    token = create_access_token(
        identity=username,
        additional_claims={"role": user["role"]}
    )
    return jsonify({"access_token": token}), 200

@app.route("/jwt-protected")
@jwt_required()
def jwt_protected():
    """
    A route protected by JWT.
    - If valid token => "JWT Auth: Access Granted"
    - If missing/invalid => 401
    """
    return "JWT Auth: Access Granted"

@app.route("/admin-only")
@jwt_required()
def admin_only():
    """
    A route that requires user to be 'admin'.
    - If admin => "Admin Access: Granted"
    - If valid token but non-admin => 403 with {"error":"Admin access required"}
    - If missing/invalid token => 401
    """
    claims = get_jwt()  # Retrieve custom claims from the token
    if claims.get("role") != "admin":
        return jsonify({"error": "Admin access required"}), 403

    return "Admin Access: Granted"

# ===========================================
# 3) CUSTOM ERROR HANDLERS FOR JWT
# ===========================================
@jwt.unauthorized_loader
def handle_unauthorized_error(err):
    return jsonify({"error": "Missing or invalid token"}), 401

@jwt.invalid_token_loader
def handle_invalid_token_error(err):
    return jsonify({"error": "Invalid token"}), 401

@jwt.expired_token_loader
def handle_expired_token_error(jwt_header, jwt_payload):
    return jsonify({"error": "Token has expired"}), 401

@jwt.revoked_token_loader
def handle_revoked_token_error(jwt_header, jwt_payload):
    return jsonify({"error": "Token has been revoked"}), 401

@jwt.needs_fresh_token_loader
def handle_needs_fresh_token_error(jwt_header, jwt_payload):
    return jsonify({"error": "Fresh token required"}), 401

# ===========================================
# 4) RUN THE APP
# ===========================================
if __name__ == "__main__":
    app.run()
