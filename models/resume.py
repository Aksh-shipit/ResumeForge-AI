from extensions import db
from datetime import datetime, timedelta, UTC


class Resume(db.Model):

    __tablename__ = "resume"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    user_id = db.Column(
        db.Integer,
        db.ForeignKey("users.id"),
        nullable=False
    )

    title = db.Column(
        db.String(100)
    )

    name = db.Column(
        db.String(100)
    )

    email = db.Column(
        db.String(120)
    )

    phone = db.Column(
        db.String(20)
    )

    address = db.Column(
        db.String(200)
    )

    linkedin = db.Column(
        db.String(200)
    )

    github = db.Column(
        db.String(200)
    )

    summary = db.Column(
        db.Text
    )

    education = db.Column(
        db.Text
    )

    skills = db.Column(
        db.Text
    )

    experience = db.Column(
        db.Text
    )

    projects = db.Column(
        db.Text
    )

    template = db.Column(
        db.String(20)
    )

    data = db.Column(
        db.Text
    )

    created_at = db.Column(
        db.DateTime,
        default=lambda: datetime.now(UTC).replace(tzinfo=None) + timedelta(hours=5, minutes=30)
    )