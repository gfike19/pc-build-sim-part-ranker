from flask import Blueprint, render_template, request, redirect, url_for
from app.services import part_service, stash_service
from flask_session import Session

main_bp = Blueprint("main", __name__)

@main_bp.route("/", methods=["GET", "POST"])
def index():
    # parts = part_service.get_all_parts()
    # return render_template("index.html", parts=parts)
    if request.method == "POST":
        stashName = request.form["stashName"]
        stash = stash_service.create_new_stash(stashName)
        msg = "Stash #" + str(stash.id) + " was successfully created!"
        Session["msg"] = msg
        return redirect(url_for("main.index"))
    if request.method == "GET":
        msg = Session["msg"]    
        return render_template("index.html", msg=msg)

@main_bp.route("/create-stash")
def create_stash():
    return render_template("create-stash.html")