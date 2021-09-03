from flask import Blueprint, render_template, request, redirect, url_for
from models import MenuItem, Menu
from extension import db
from setting import cloudinary
from views.view_admin_home import admin_home, check_session, session

menu_item_home = Blueprint('menu_item_home', __name__, static_folder='static', template_folder='templates')


@menu_item_home.route('/menu_item')
def home():
    if not check_session():
        return redirect(url_for('admin_home.login'))
    get_menu_item = MenuItem.query.all()
    return render_template('table_menu_item.html', itemList=get_menu_item)


@menu_item_home.route('/menu_item_add', methods=['GET', 'POST'])
def add():
    if not check_session():
        return redirect(url_for('admin_home.login'))
    get_menu = Menu.query.all()
    if request.method == 'POST':
        print('test')
        if request.files['menu_item_image']:
            result = cloudinary.uploader.upload(request.files['menu_item_image'])
            result = result['url']
        else:
            result = None
        new_menu_item = MenuItem(menu_id=request.form['menu_id'],
                                 menu_item_image=result,
                                 menu_item_name=request.form['menu_item_name'],
                                 menu_item_description=request.form['menu_item_description'],
                                 menu_item_price=request.form['menu_item_price'])
        db.session.add(new_menu_item)
        db.session.commit()
    return render_template('form_menu_item.html', menuId=get_menu)


@menu_item_home.route('/menu_item_edit/<menu_item_id>')
def edit(menu_item_id):
    if not check_session():
        return redirect(url_for('admin_home.login'))
    get_menu = Menu.query.all()
    get_menu_item = MenuItem.query.filter_by(menu_item_id=menu_item_id).first()
    return render_template('form_menu_item.html', item=get_menu_item, menuId=get_menu)


@menu_item_home.route('/menu_item_update', methods=['POST'])
def update():
    if not check_session():
        return redirect(url_for('admin_home.login'))
    get_menu_item = MenuItem.query.filter_by(menu_item_id=request.form['menu_item_id']).first()
    get_menu_item.menu_id = request.form['menu_id']
    get_menu_item.menu_item_name = request.form['menu_item_name']
    get_menu_item.menu_item_description = request.form['menu_item_description']
    get_menu_item.menu_item_price = request.form['menu_item_price']
    if request.files['menu_item_image']:
        result = cloudinary.uploader.upload(request.files['menu_item_image'])
        get_menu_item.menu_item_image = result['url']
    db.session.commit()
    return redirect(url_for('menu_item_home.home'))


@menu_item_home.route('/menu_item_delete/<menu_item_id>')
def delete(menu_item_id):
    if not check_session():
        return redirect(url_for('admin_home.login'))
    MenuItem.query.filter_by(menu_item_id=menu_item_id).delete()
    db.session.commit()
    return redirect(url_for('menu_item_home.home'))
