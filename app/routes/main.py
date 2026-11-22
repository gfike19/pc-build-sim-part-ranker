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
            return redirect(url_for("main.index"))
        
        elif action == "delete-stash":
            stash_id = request.form.get("stash_id", type=int)
            stash_service.del_stash_by_id(stash_id)
            return redirect(url_for("main.index"))
        
        elif action =="add-parts":
            stash_id = request.form.get("stash_id", type=int)
            return redirect(url_for("main.addParts", stash_id=stash_id))
    
    if request.method == "GET":
        stashes = stash_service.get_all_Stashes()
        return render_template("index.html", stashes=stashes)

@main_bp.route("/add-parts/<int:stash_id>", methods=["GET", "POST"])
def addParts(stash_id):
    if request.method == "GET":
        cpus = part_service.get_all_cpus()
        gpus = part_service.get_all_gpus()
        return render_template("add-parts.html", cpus=cpus, gpus=gpus)
    # if request.method == "POST":