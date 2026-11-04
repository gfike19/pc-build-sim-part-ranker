from flask import Blueprint, render_template
from app.services import part_service

main_bp = Blueprint("main", __name__)


@main_bp.route("/")
def index():
    parts = part_service.get_all_parts()
    return render_template("index.html", parts=parts)
