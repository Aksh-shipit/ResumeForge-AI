from flask import (
    Blueprint,
    render_template,
    request,
    jsonify,
    send_file,
    redirect,
    url_for,
    flash
)

from flask_login import (
    login_user,
    logout_user,
    login_required,
    current_user
)

from extensions import db, bcrypt

from models.user import User
from models.resume import Resume

import json

from utils.ai import (
    generate_summary,
    analyze_resume
)

from utils.pdf_generator import create_resume_pdf


main = Blueprint("main", __name__)


# -------------------------
# Home Page
# -------------------------

@main.route("/")
@login_required
def home():

    return render_template(
        "index.html",
        user=current_user
    )


# -------------------------
# Register
# -------------------------

@main.route("/register", methods=["GET", "POST"])
def register():

    if request.method == "POST":

        name = request.form["name"]
        email = request.form["email"]
        password = request.form["password"]

        existing_user = User.query.filter_by(
            email=email
        ).first()

        if existing_user:

            flash("Email already exists!")

            return redirect(
                url_for("main.register")
            )

        hashed_password = bcrypt.generate_password_hash(
            password
        ).decode("utf-8")

        user = User(
            name=name,
            email=email,
            password=hashed_password
        )

        db.session.add(user)
        db.session.commit()

        flash("Registration Successful!")

        return redirect(
            url_for("main.login")
        )

    return render_template("register.html")


# -------------------------
# Login
# -------------------------

@main.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        email = request.form["email"]
        password = request.form["password"]

        user = User.query.filter_by(
            email=email
        ).first()

        if user and bcrypt.check_password_hash(
            user.password,
            password
        ):

            login_user(user)

            return redirect(
                url_for("main.home")
            )

        flash("Invalid Email or Password")

    return render_template("login.html")


# -------------------------
# Logout
# -------------------------

@main.route("/logout")
@login_required
def logout():

    logout_user()

    return redirect(
        url_for("main.login")
    )


# -------------------------
# AI Summary
# -------------------------

@main.route("/generate-summary", methods=["POST"])
@login_required
def summary():

    data = request.get_json()

    role = data.get("role", "")
    skills = data.get("skills", "")
    experience = data.get("experience", "")

    result = generate_summary(
        role,
        skills,
        experience
    )

    return jsonify({
        "summary": result
    })


# -------------------------
# AI Resume Analysis
# -------------------------

@main.route("/analyze-resume", methods=["POST"])
@login_required
def analyze():

    data = request.get_json()

    suggestions = analyze_resume(data)

    return jsonify({
        "suggestions": suggestions
    })



# -------------------------
# Save Resume
# -------------------------

@main.route("/save-resume", methods=["POST"])
@login_required
def save_resume():

    data = request.get_json()

    resume = Resume(

        user_id=current_user.id,

        title=f"{data.get('name', 'Untitled')} Resume",

        name=data.get("name"),

        email=data.get("email"),

        phone=data.get("phone"),

        address=data.get("address"),

        linkedin=data.get("linkedin"),

        github=data.get("github"),

        summary=data.get("summary"),

        education=json.dumps(data.get("education", [])),

        skills=json.dumps(data.get("skills", [])),

        experience=json.dumps(data.get("experience", [])),

        projects=json.dumps(data.get("projects", [])),

        template=data.get("template", "classic"),

        data=json.dumps(data)

    )

    db.session.add(resume)

    db.session.commit()

    return jsonify({

        "message": "Resume Saved Successfully!"

    })
# -------------------------
# My Resumes
# -------------------------

@main.route("/my-resumes")
@login_required
def my_resumes():

    resumes = Resume.query.filter_by(

        user_id=current_user.id

    ).order_by(

        Resume.created_at.desc()

    ).all()

    return render_template(

        "my_resumes.html",

        resumes=resumes

    )


# -------------------------
# Download Resume PDF
# -------------------------

@main.route("/download-resume", methods=["POST"])
@login_required
def download_resume():

    data = request.get_json()

    template = data.get(
        "template",
        "classic"
    )

    data["template"] = template

    pdf_path = create_resume_pdf(
        data,
        "resume.pdf"
    )

    return send_file(

        pdf_path,

        as_attachment=True,

        download_name="Resume.pdf",

        mimetype="application/pdf"

    )

@main.route("/delete-resume/<int:id>", methods=["DELETE"])
@login_required
def delete_resume(id):

    resume = Resume.query.filter_by(
        id=id,
        user_id=current_user.id
    ).first()

    if not resume:

        return jsonify({
            "message":"Resume not found."
        }),404

    db.session.delete(resume)

    db.session.commit()

    return jsonify({
        "message":"Resume deleted successfully!"
    })


# -------------------------
# Edit Resume
# -------------------------

@main.route("/edit-resume/<int:id>")
@login_required
def edit_resume(id):

    resume = Resume.query.filter_by(
        id=id,
        user_id=current_user.id
    ).first()

    if not resume:
        flash("Resume not found.")
        return redirect(url_for("main.my_resumes"))

    resume_data = json.loads(resume.data)

    return render_template(
        "index.html",
        resume=resume_data,
        resume_id=id
    )


# -------------------------
# Update Resume
# -------------------------

@main.route("/update-resume/<int:id>", methods=["POST"])
@login_required
def update_resume(id):

    resume = Resume.query.filter_by(
        id=id,
        user_id=current_user.id
    ).first()

    if not resume:
        return jsonify({
            "message": "Resume not found"
        }), 404

    data = request.get_json()

    resume.title = f"{data.get('name', 'Untitled')} Resume"
    resume.name = data.get("name")
    resume.email = data.get("email")
    resume.phone = data.get("phone")
    resume.address = data.get("address")
    resume.linkedin = data.get("linkedin")
    resume.github = data.get("github")
    resume.summary = data.get("summary")
    resume.education = json.dumps(data.get("education", []))
    resume.skills = json.dumps(data.get("skills", []))
    resume.experience = json.dumps(data.get("experience", []))
    resume.projects = json.dumps(data.get("projects", []))
    resume.template = data.get("template", "classic")
    resume.data = json.dumps(data)

    db.session.commit()

    return jsonify({
        "message": "Resume Updated Successfully!"
    })


# -------------------------
# Get Resume Data
# -------------------------

@main.route("/resume-data/<int:id>")
@login_required
def resume_data(id):

    resume = Resume.query.filter_by(
        id=id,
        user_id=current_user.id
    ).first()

    if not resume:
        return jsonify({
            "message": "Resume not found"
        }), 404

    return jsonify(json.loads(resume.data))

@main.route("/ats-score", methods=["POST"])
@login_required
def ats_score():

    data = request.get_json()

    score = 0
    feedback = []

    if data.get("name"):
        score += 10
    else:
        feedback.append("Add your full name.")

    if data.get("email"):
        score += 10
    else:
        feedback.append("Add your email address.")

    if data.get("phone"):
        score += 10
    else:
        feedback.append("Add your phone number.")

    if data.get("summary"):
        score += 15
    else:
        feedback.append("Add a professional summary.")

    skills = data.get("skills", [])

    if len(skills) >= 5:
        score += 20
    else:
        feedback.append("Add at least 5 skills.")

    if len(data.get("education", [])) > 0:
        score += 10
    else:
        feedback.append("Add education.")

    if len(data.get("experience", [])) > 0:
        score += 15
    else:
        feedback.append("Add work experience.")

    if len(data.get("projects", [])) > 0:
        score += 10
    else:
        feedback.append("Add projects.")

    return jsonify({
        "score": score,
        "feedback": feedback
    })