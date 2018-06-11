from flask import render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required

from application import app, db
from application.auth.models import User
from application.auth.forms import LoginForm, RegistrationForm


@app.route("/auth/login", methods=["GET", "POST"])
def auth_login():
    if request.method == "GET":
        return render_template("auth/loginform.html", form=LoginForm())

    form = LoginForm(request.form)

    user = User.query.filter_by(
        username=form.username.data, password=form.password.data).first()
    if not user:
        return render_template("auth/loginform.html", form=form,
                               error="No such username or password")

    login_user(user)
    return redirect(url_for("index"))


@app.route("/auth/logout")
def auth_logout():
    logout_user()
    return redirect(url_for("index"))


@app.route('/auth/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm(request.form)
    if request.method == 'POST' and form.validate():
        
        t = User(form.name.data)
        t.username = form.username.data
        t.password = form.password.data

        db.session().add(t)
        db.session().commit()

        flash('Thanks for registering')
        return redirect(url_for('auth_login'))
    return render_template('/auth/registrationform.html', form=form)


@app.route("/auth/users")
@login_required
def users_index():
    return render_template("auth/users.html", accounts=User.query.all(), no_applications=User.find_users_with_no_applications())

@app.route("/auth/remove/<account_id>/", methods=["POST"])
@login_required
def users_remove(account_id):

    t = User.query.get(account_id)
    db.session().delete(t)
    db.session().commit()

    return redirect(url_for("users_index"))
