from app.extensions import db


stash_parts = db.Table(
    "stash_parts",

    db.Column(
        "stash_id",
        db.Integer,
        db.ForeignKey("stashes.id"),
        primary_key=True
    ),

    db.Column(
        "part_id",
        db.Integer,
        db.ForeignKey("parts.id"),
        primary_key=True
    )
)