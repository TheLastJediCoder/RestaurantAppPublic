from flask import Blueprint, render_template, request, redirect
from models import Menu, MenuItem, Deal, DealItem
from extension import db
from datetime import datetime


home = Blueprint('home', __name__, static_folder='static', template_folder='templates')


@home.route('/')
def index():
    get_menu = db.session.query(MenuItem, Menu).filter(MenuItem.menu_id == Menu.menu_id).all()

    menu = {}
    menu_image = {}
    for i in get_menu:
        if i.Menu.menu_name not in menu_image:
            menu_image[i.Menu.menu_name] = i.Menu.menu_image
        if i.Menu.menu_name in menu:
            menu[i.Menu.menu_name].append([i.MenuItem.menu_item_name, i.MenuItem.menu_item_description,
                                           i.MenuItem.menu_item_price, i.MenuItem.menu_item_image])
        else:
            menu[i.Menu.menu_name] = [[i.MenuItem.menu_item_name, i.MenuItem.menu_item_description,
                                       i.MenuItem.menu_item_price, i.MenuItem.menu_item_image]]
    today = datetime.today().strftime('%A')

    get_deal = db.session.query(DealItem, Deal).filter((DealItem.deal_id == Deal.deal_id) &
                                                       (Deal.deal_week_day == today)).all()

    print(get_deal)

    return render_template('index.html', menu=menu, menuImage=menu_image, deal=get_deal)
