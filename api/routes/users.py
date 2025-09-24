from flask import Blueprint, request
from models.users import UsersModel, db

# Create a Blueprint for user-related routes
bp = Blueprint("users", __name__, url_prefix="/users")


@bp.get("/")
def get_users():
    """Retrieve all users.
    Returns:
        200: A list of users.
        500: Internal server error.
    """
    try:
        users = UsersModel.query.all()
        bp.logger.info(f"Retrieved {len(users)} users from the database.")
        return {
            "users": {
                user.name: {
                    "email": user.email,
                    "registration_date": user.registration_date,
                }
                for user in users
            }
        }, 200
    except Exception as e:
        return {"error": str(e)}, 500


@bp.post("/")
def create_user():
    """Create a new user.
    Expects a JSON payload with 'name' and 'email' fields.
    Returns:
        201: User created successfully.
        400: Bad request (e.g., missing fields, duplicate email).
        500: Internal server error.
    """
    data = request.get_json()
    if not data:
        return {"error": "No input data provided"}, 400
    elif "name" not in data or "email" not in data:
        return {"error": "Missing 'name' or 'email' in input data"}, 400

    name = data.get("name")
    email = data.get("email")

    print(data)
    try:
        new_user = UsersModel(name=name, email=email)
        db.session.add(new_user)
        db.session.commit()
        return {"message": "User created"}, 201
    # controlar caso de email duplicado
    except Exception as e:
        if "UNIQUE constraint failed" in str(e):
            return {"error": "Email already exists"}, 400
        return {"error": str(e)}, 500
