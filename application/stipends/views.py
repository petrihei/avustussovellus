from flask import render_template, request, redirect, url_for
from flask_login import login_required, current_user

from application import app, db
from application.stipends.models import Stipend
from application.stipends.forms import StipendForm, ReceiverForm

@app.route("/stipends/new/")
@login_required
def stipends_form():
    return render_template("stipends/new.html", form=StipendForm())

@app.route("/stipends", methods=["GET"])
@login_required
def stipends_index():
    return render_template("stipends/list.html", stipends=Stipend.query.all())


@app.route("/stipends/set/<stipend_id>/", methods=["POST"])
@login_required
def stipends_set_receiver(stipend_id):

    t = Stipend.query.get(stipend_id)
    form = ReceiverForm(request.form)

    if not form.validate():
        return render_template("stipends/set.html", form=form)

    t.receiver = form.receiver.data

    db.session().add(t)
    db.session().commit()

    return redirect(url_for("stipends_index"))


@app.route("/stipends/set/")
@login_required
def stipends_set():
    return render_template("stipends/set.html", form=StipendForm())

@app.route("/stipends/", methods=["POST"])
@login_required
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
@login_required
def stipends_remove(stipend_id):

    t = Stipend.query.get(stipend_id)
    db.session().delete(t)
    db.session().commit()

    return redirect(url_for("stipends_index"))
