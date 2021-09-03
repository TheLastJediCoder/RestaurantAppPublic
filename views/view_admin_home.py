from flask import Blueprint, render_template, session, request, redirect, flash, url_for

admin_home = Blueprint('admin_home', __name__, static_folder='static', template_folder='templates')


def check_session():
    if 'username' in session:
        return True
    else:
        return False


@admin_home.route('/')
def home():
    if not check_session():
        return redirect(url_for('admin_home.login'))
    return render_template('aindex.html')


@admin_home.route('/login', methods=['GET', 'POST'])
def login():
    if check_session():
        return redirect('admin/')
    if request.method == 'GET':
        return render_template('login.html')
    elif request.method == 'POST':
        username = request.form['user_name']
        password = request.form['password']
        if username == 'admin' and password == 'admin123':
            session.permanent = True
            session['username'] = username
            return redirect(url_for('admin_home.home'))
        else:
            flash('Please check Credentials!')
            return render_template('login.html')


@admin_home.route('/logout')
def logout():
    if check_session():
        session.pop('username', None)
        return redirect(url_for('admin_home.home'))
    else:
        return redirect(url_for('admin_home.login'))
