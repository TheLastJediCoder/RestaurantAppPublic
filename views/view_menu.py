from flask import Blueprint, render_template, request, redirect, url_for
from models import Menu
from extension import db
from setting import cloudinary
from views.view_admin_home import admin_home, check_session, session

menu_home = Blueprint('menu_home', __name__, static_folder='static', template_folder='templates')


@menu_home.route('/menu')
def home():
    if not check_session():
        return redirect(url_for('admin_home.login'))
    get_menu = Menu.query.all()
    return render_template('table_menu_category.html', menuList=get_menu)


@menu_home.route('/menu_add', methods=['GET', 'POST'])
def add():
    if not check_session():
        return redirect(url_for('admin_home.login'))
    if request.method == 'POST':
        print('test')
        if request.files['menu_image']:
            result = cloudinary.uploader.upload(request.files['menu_image'])
            result = result['url']
        else:
            result = None
        new_menu = Menu(menu_name=request.form['menu_name'], menu_image=result)
        db.session.add(new_menu)
        db.session.commit()
    return render_template('form_menu_category.html')


@menu_home.route('/menu_edit/<menu_id>')
def edit(menu_id):
    if not check_session():
        return redirect(url_for('admin_home.login'))
    get_menu = Menu.query.filter_by(menu_id=menu_id).first()
    return render_template('form_menu_category.html', menu=get_menu)


@menu_home.route('/menu_update', methods=['POST'])
def update():
    if not check_session():
        return redirect(url_for('admin_home.login'))
    get_menu = Menu.query.filter_by(menu_id=request.form['menu_id']).first()
    get_menu.menu_name = request.form['menu_name']
    if request.files['menu_image']:
        result = cloudinary.uploader.upload(request.files['menu_image'])
        get_menu.menu_image = result['url']
    db.session.commit()
    return redirect(url_for('menu_home.home'))


@menu_home.route('/menu_delete/<menu_id>')
def delete(menu_id):
    if not check_session():
        return redirect(url_for('admin_home.login'))
    Menu.query.filter_by(menu_id=menu_id).delete()
    db.session.commit()
    return redirect(url_for('menu_home.home'))
