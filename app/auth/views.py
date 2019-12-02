from flask import render_template
from . import auth
from . forms import LoginForm, RegistrationForm
from ..models import User
from flask_login import login_user, logout_user, login_required
#da view functions
auth.route('/register')
def registration():
    # instantiate the form
    form=RegistrationForm()
    if form.validate_on_submit():
        user=User(email=form.email.data, username=form.username.data, password_hash=form.password.data)
        db.session.add(user)
        db.session.commit()
        mail_message("Welcome to Thy Blog Post", "email/welcome_thy", user.email, user=user)
        return redirect(url_for('auth.login'))
        title='New Account'
    return render_template('auth/register.html', title=title, registration_form=form)
