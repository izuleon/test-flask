from flask import Flask

from src.db import init_db
from src.exception.generic_exception import handle_custom_exception
from src.routing.dashboard import dashboard_bp
from src.routing.user import user_bp

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///mydatabase.db"
with app.app_context():
    init_db(app)
app.register_error_handler(400, handle_custom_exception)

# Register the blueprints with the app
app.register_blueprint(dashboard_bp)
app.register_blueprint(user_bp, url_prefix="/user")


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5555)
