from flask import render_template, request, redirect, url_for
from application import app, db
from application.applications.models import Application
from application.applications.forms import ApplicationForm

@app.route("/applications/new/")
def applications_form():
    return render_template("applications/new.html", form=ApplicationForm())

@app.route("/applications", methods=["GET"])
def applications_index():
    return render_template("applications/list.html", applications = Application.query.all())

@app.route("/applications/<application_id>/", methods=["POST"])
def applications_set_approved(application_id):

    t = Application.query.get(application_id)
    t.approved = True
    db.session().commit()

    return redirect(url_for("applications_index"))

@app.route("/applications/", methods=["POST"])
def applications_create():
    form = ApplicationForm(request.form)

    if not form.validate():
        return render_template("applications/new.html", form=form)

    t = Application(form.name.data)
    t.sum = form.sum.data
    t.definition = form.definition.data

    db.session().add(t)
    db.session().commit()

    return redirect(url_for("applications_index"))
