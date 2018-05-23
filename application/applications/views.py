from application import app, db
from flask import redirect, render_template, request, url_for
from application.applications.models import Application

@app.route("/applications", methods=["GET"])
def applications_index():
    return render_template("applications/list.html", applications = Application.query.all())

@app.route("/applications/new/")
def applications_form():
    return render_template("applications/new.html")

@app.route("/applications/<application_id>/", methods=["POST"])
def applications_set_approved(application_id):

    t = Application.query.get(application_id)
    t.approved = True
    db.session().commit()

    return redirect(url_for("applications_index"))

@app.route("/applications/", methods=["POST"])
def applications_create():
    t = Application(request.form.get("name"))

    db.session().add(t)
    db.session().commit()
  
    return redirect(url_for("applications_index"))
