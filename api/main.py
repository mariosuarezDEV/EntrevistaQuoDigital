from flask import Flask, jsonify
from routes.users import bp as users_bp
from models.users import db
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)
app.register_blueprint(users_bp)
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv(
    "DATABASE_URL", "sqlite:///default.db"
)

db.init_app(app)


@app.get("/")
def hello_world():
    app.logger.info("The API is working!")
    return jsonify(message="Success!")


# Crear tablas
with app.app_context():
    db.create_all()
