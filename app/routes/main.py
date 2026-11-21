from flask import Blueprint, render_template, request, redirect, url_for
from app.services import part_service, stash_service

main_bp = Blueprint("main", __name__)

@main_bp.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        action = request.form.get("action")
        if action == "create-stash":
            stashName = request.form["stashName"]
            stash_service.create_new_stash(stashName)
            # msg = "Stash #" + str(stash.id) + " was successfully created!"
            # Session["msg"] = msg
        return redirect(url_for("main.index"))
    if request.method == "GET":
        stashes = stash_service.get_all_Stashes()
        return render_template("index.html", stashes=stashes)

@main_bp.route("/create-stash")
def create_stash():
    return render_template("create-stash.html")