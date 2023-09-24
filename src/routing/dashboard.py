from flask import Blueprint

dashboard_bp = Blueprint("main", __name__)


@dashboard_bp.get("/")
def dashboard():
    return "Dashboard page"
