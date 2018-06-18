from flask import render_template, request, redirect, url_for
from flask_login import current_user, login_required

from application import app, db
from application.applications.models import Application
from application.applications.forms import ApplicationForm

@app.route("/applications/new/")
@login_required
def applications_form():
    return render_template("applications/new.html", form=ApplicationForm())

@app.route("/applications", methods=["GET"])
@login_required
def applications_index():
    return render_template("applications/list.html", applications = Application.query.all())

@app.route("/applications/<application_id>/", methods=["POST"])
@login_required
def applications_set_approved(application_id):

    t = Application.query.get(application_id)
    t.approved = True
    db.session().commit()

    return redirect(url_for("applications_index"))

@app.route("/applications/", methods=["POST"])
@login_required
def applications_create():
    form = ApplicationForm(request.form)

    if not form.validate():
        return render_template("applications/new.html", form=form)

    t = Application(form.name.data)
    t.sum = form.sum.data
    t.definition = form.definition.data
    t.account_id = current_user.id

    db.session().add(t)
    db.session().commit()

    return redirect(url_for("applications_index"))

@app.route("/applications/remove/<application_id>/", methods=["POST"])
@login_required
def applications_remove(application_id):

    t = Application.query.get(application_id)
    db.session().delete(t)
    db.session().commit()

    return redirect(url_for("applications_index"))


@app.route("/applications/view/<application_id>")
@login_required
def applications_view(application_id):
    return render_template("applications/view.html", application=Application.query.get(application_id))


@app.route("/applications/edit/<application_id>")
@login_required
def applications_edit_form(application_id):
    return render_template("applications/edit.html", form=ApplicationForm(), application=Application.query.get(application_id))


@app.route("/applications/edit/<application_id>", methods=["POST"])
@login_required
def applications_edit(application_id):
    form = ApplicationForm(request.form)
    application = Application.query.get(application_id)
    form.application_id = application.id
    if not form.validate():
        return render_template("applications/edit.html", form=form, application=application)
    form.name = application.name
    application.sum = form.sum.data
    form.definition = application.definition
    db.session().commit()
    return redirect(url_for("applications_index"))
