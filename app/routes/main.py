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
        
        elif action =="view-edit-stash":
            stash_id = request.form.get("stash_id", type=int)
            return redirect(url_for("main.vieweditStash", stash_id=stash_id))
    
    if request.method == "GET":
        stashes = stash_service.get_all_Stashes()
        return render_template("index.html", stashes=stashes)

@main_bp.route("/view-edit-stash/<int:stash_id>", methods=["GET", "POST"])
def addParts(stash_id):
    cpus = part_service.get_all_cpus()
    gpus = part_service.get_all_gpus()
    if request.method == "GET":
        return render_template("view-edit-stash.html", cpus=cpus, gpus=gpus)
    if request.method == "POST":
        gpus = request.form.getlist("gpu_id")
        cpus = request.form.getlist("cpu_id")
        part_ids = gpus + cpus
        stash_service.add_parts(stash_id=stash_id, part_ids=part_ids)
        return render_template("view-edit-stash", cpus=cpus, gpus=gpus)