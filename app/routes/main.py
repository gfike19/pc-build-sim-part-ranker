from flask import Blueprint, render_template, request, redirect, url_for
from app.services import stash_service

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
            # main.viewEditStash is function, not route
            return redirect(url_for("main.viewEditStash", stash_id=stash_id))
    
    if request.method == "GET":
        stashes = stash_service.get_all_Stashes()
        return render_template("index.html", stashes=stashes)

@main_bp.route("/view-edit-stash/<int:stash_id>", methods=["GET", "POST"])
def viewEditStash(stash_id):
    non_stashed_parts = stash_service.get_parts_not_in_stash(stash_id)
    gpus = [part for part in non_stashed_parts if part.gpu]
    cpus = [part for part in non_stashed_parts if part.cpu]
    stashed_parts = stash_service.get_all_parts_by_stash(stash_id=stash_id)
    if request.method == "GET":
        return render_template("view-edit-stash.html", cpus=cpus, gpus=gpus, stashed_parts=stashed_parts)
    if request.method == "POST":
        gpus = request.form.getlist("gpu_id", type=int)
        cpus = request.form.getlist("cpu_id", type=int)
        part_ids = gpus + cpus
        stash_service.add_parts(stash_id=stash_id, part_ids=part_ids)
        return redirect(url_for("main.viewEditStash", stash_id=stash_id))