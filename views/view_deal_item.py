from flask import Blueprint, render_template, request, redirect, url_for
from models import DealItem, Deal
from extension import db
from setting import cloudinary
from views.view_admin_home import admin_home, check_session, session

deal_item_home = Blueprint('deal_item_home', __name__, static_folder='static', template_folder='templates')


@deal_item_home.route('/deal_item')
def home():
    if not check_session():
        return redirect(url_for('admin_home.login'))
    get_deal_item = DealItem.query.all()
    return render_template('table_deal_item.html', itemList=get_deal_item)


@deal_item_home.route('/deal_item_add', methods=['GET', 'POST'])
def add():
    if not check_session():
        return redirect(url_for('admin_home.login'))
    get_deal = Deal.query.all()
    if request.method == 'POST':
        print('test')
        if request.files['deal_item_image']:
            result = cloudinary.uploader.upload(request.files['deal_item_image'])
            result = result['url']
        else:
            result = None

        new_deal_item = DealItem(deal_id=request.form['deal_id'],
                                 deal_item_image=result,
                                 deal_item_name=request.form['deal_item_name'],
                                 deal_item_description=request.form['deal_item_description'],
                                 deal_item_price=request.form['deal_item_price'],
                                 deal_item_discounted_price=request.form['deal_item_discounted_price'])
        db.session.add(new_deal_item)
        db.session.commit()
    return render_template('form_deal_item.html', dealId=get_deal)


@deal_item_home.route('/deal_item_edit/<deal_item_id>')
def edit(deal_item_id):
    if not check_session():
        return redirect(url_for('admin_home.login'))
    get_deal = Deal.query.all()
    get_menu_item = DealItem.query.filter_by(deal_item_id=deal_item_id).first()
    return render_template('form_deal_item.html', item=get_menu_item, dealId=get_deal)


@deal_item_home.route('/deal_item_update', methods=['POST'])
def update():
    if not check_session():
        return redirect(url_for('admin_home.login'))
    get_deal_item = DealItem.query.filter_by(deal_item_id=request.form['deal_item_id']).first()
    get_deal_item.deal_id = request.form['deal_id']
    get_deal_item.deal_item_name = request.form['deal_item_name']
    get_deal_item.deal_item_description = request.form['deal_item_description']
    get_deal_item.deal_item_price = request.form['deal_item_price']
    get_deal_item.deal_item_discounted_price = request.form['deal_item_discounted_price']
    if request.files['deal_item_image']:
        result = cloudinary.uploader.upload(request.files['deal_item_image'])
        get_deal_item.deal_item_image = result['url']
    db.session.commit()
    return redirect(url_for('deal_item_home.home'))


@deal_item_home.route('/deal_item_delete/<deal_item_id>')
def delete(deal_item_id):
    if not check_session():
        return redirect(url_for('admin_home.login'))
    DealItem.query.filter_by(deal_item_id=deal_item_id).delete()
    db.session.commit()
    return redirect(url_for('deal_item_home.home'))
