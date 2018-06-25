from flask import render_template, request, redirect, url_for
from flask_login import login_user, logout_user, current_user

from application import app, db, login_required
from application.stipends.models import Stipend
from application.auth.models import User
from application.stipends.forms import StipendForm, ReceiverForm

@app.route("/stipends/new/")
@login_required(role="ADMIN")
def stipends_form():
    return render_template("stipends/new.html", form=StipendForm())

@app.route("/stipends", methods=["GET"])
@login_required(role="ADMIN")
def stipends_index():
    return render_template("stipends/list.html", stipends=Stipend.query.all())

@app.route("/stipends-user", methods=["GET"])
@login_required(role="USER")
def stipends_index_user():
    return render_template("stipends/list-user.html", stipends=Stipend.query.all())

@app.route("/stipends/set/<stipend_id>/", methods=["POST"])
@login_required(role="ADMIN")
def stipends_set_receiver(stipend_id):

    t = Stipend.query.get(stipend_id)
    form = ReceiverForm(request.form)

    if not form.validate():
        return render_template("stipends/set.html", form=form)

    t.receiver = form.receiver.data

    db.session().add(t)
    db.session().commit()

    return redirect(url_for("stipends_index"))

@app.route("/stipends/", methods=["POST"])
@login_required(role="ADMIN")
def stipends_create():
    form = StipendForm(request.form)

    if not form.validate():
        return render_template("stipends/new.html", form=form)

    t = Stipend(form.name.data)
    t.sum = form.sum.data
    t.definition = form.definition.data
    t.account_id = current_user.id

    db.session().add(t)
    db.session().commit()

    return redirect(url_for("stipends_index"))

@app.route("/stipends/remove/<stipend_id>/", methods=["POST"])
@login_required(role="ADMIN")
def stipends_remove(stipend_id):

    t = Stipend.query.get(stipend_id)
    db.session().delete(t)
    db.session().commit()

    return redirect(url_for("stipends_index"))

@app.route("/stipend/edit/<stipend_id>")
@login_required(role="ADMIN")
def stipends_edit_form(stipend_id):
    return render_template("stipends/edit.html", form=ReceiverForm(), stipend=Stipend.query.get(stipend_id))

@app.route("/stipends/edit/<stipend_id>", methods=["POST"])
@login_required(role="ADMIN")
def stipends_edit(stipend_id):
    form = ReceiverForm(request.form)
    stipend = Stipend.query.get(stipend_id)
    form.stipend_id = stipend.id
    if not form.validate():
        return render_template("stipends/edit.html", form=form, stipend=stipend)
    form.name = stipend.name
    stipend.sum = stipend.sum
    stipend.definition = stipend.definition
    stipend.receiver = form.receiver.data
    db.session().commit()
    return redirect(url_for("stipends_index"))


@app.route("/stipends/<stipend_id>/auth/<account_id>/", methods=["POST"])
@login_required(role="USER")
def stipend_applier_add(stipend_id, account_id):
    a = Stipend.query.get(stipend_id)
    r = User.query.get(account_id)
    r.children.append(a)

    try:
        db.session().commit()
    except:
        db.session().rollback()
        raise

    return redirect(url_for("stipends_thank_you"))


@app.route("/stipends/thankyou/")
@login_required(role="USER")
def stipends_thank_you():
    return render_template("stipends/thankyou.html")
