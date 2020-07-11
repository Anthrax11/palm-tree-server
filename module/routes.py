from module import app, bcrypt, db
from flask import render_template, request, redirect, url_for
from module.forms import RegisterUser
from module.model import User


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html', title='Welcome')


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterUser()
    if request.method == 'POST' and form.validate():
        hash_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hash_password)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('register.html', form=form)