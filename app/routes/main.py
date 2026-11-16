from flask import Blueprint, render_template, request
from app.services import part_service

main_bp = Blueprint("main", __name__)


@main_bp.route("/", methods=["GET", "POST"])
def index():
    # parts = part_service.get_all_parts()
    # return render_template("index.html", parts=parts)
    if request.method == "POST":
        
    return render_template("index.html")

@main_bp.route("/create-stash")
def create_stash():
    return render_template("create-stash.html")