from flask import Blueprint, render_template, request, redirect, url_for
from models import Deal
from extension import db
from setting import cloudinary
from views.view_admin_home import admin_home, check_session, session

deal_home = Blueprint('deal_home', __name__, static_folder='static', template_folder='templates')


@deal_home.route('/deal')
def home():
    if not check_session():
        return redirect(url_for('admin_home.login'))
    get_deal = Deal.query.all()
    return render_template('table_deal_category.html', dealList=get_deal)


@deal_home.route('/deal_add', methods=['GET', 'POST'])
def add():
    if not check_session():
        return redirect(url_for('admin_home.login'))
    if request.method == 'POST':
        if request.files['deal_category_image']:
            result = cloudinary.uploader.upload(request.files['deal_category_image'])
            result = result['url']
        else:
            result = None
        new_deal = Deal(deal_name=request.form['deal_name'],
                        deal_category_image=result,
                        deal_description=request.form['deal_description'],
                        deal_end_date=request.form['deal_end_date'],
                        deal_week_day=request.form['deal_week_day'],
                        deal_start_date=request.form['deal_start_date'])
        db.session.add(new_deal)
        db.session.commit()
    return render_template('form_deal_category.html')


@deal_home.route('/deal_edit/<deal_id>')
def edit(deal_id):
    if not check_session():
        return redirect(url_for('admin_home.login'))
    get_deal = Deal.query.filter_by(deal_id=deal_id).first()
    return render_template('form_deal_category.html', deal=get_deal)


@deal_home.route('/deal_update', methods=['POST'])
def update():
    if not check_session():
        return redirect(url_for('admin_home.login'))
    get_deal = Deal.query.filter_by(deal_id=request.form['deal_id']).first()
    get_deal.deal_name = request.form['deal_name'],
    get_deal.deal_description = request.form['deal_description']
    get_deal.deal_end_date = request.form['deal_end_date']
    get_deal.deal_week_day = request.form['deal_week_day']
    get_deal.deal_start_date = request.form['deal_start_date']
    if request.files['deal_category_image']:
        result = cloudinary.uploader.upload(request.files['deal_category_image'])
        get_deal.deal_category_image = result['url']
    db.session.commit()
    return redirect(url_for('deal_home.home'))


@deal_home.route('/deal_delete/<deal_id>')
def delete(deal_id):
    if not check_session():
        return redirect(url_for('admin_home.login'))
    Deal.query.filter_by(deal_id=deal_id).delete()
    db.session.commit()
    return redirect(url_for('deal_home.home'))

