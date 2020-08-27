from app.main import bp, forms
from flask import render_template, redirect, url_for, flash
from app.main.services import pwned_password_service


@bp.route("/", methods=["GET", "POST"])
def index():
    form = forms.PasswordPwnedForm()
    if form.validate_on_submit():
        pwned_service = pwned_password_service.PwnedPasswordService(form.password.data)
        pwned_count = pwned_service.pwned_count()
        if pwned_count > 0:
            flash(f"This password has appeared {pwned_count} times in compromised passwords dataset. "
                  f"If you are using this password anywhere, we strongly recommend you to change it immediately.", "pwned")
        elif pwned_count == 0:
            flash("This password was not found in any of the compromised passwords dataset available.", "not_pwned")
        else:
            flash("Pwned Password service is unavailable. Please try after some time. "
                  "We regret the inconvenience caused.", "service_unavailable")
        return redirect(url_for("main.index"))
    return render_template("index.html", site_name="Pwned Credentials", form=form)
