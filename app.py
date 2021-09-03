from flask import Flask
from flask_session import Session
from views.view_admin_home import admin_home
from views.view_menu import menu_home
from views.view_deal import deal_home
from views.view_team import team_home
from views.view_menu_item import menu_item_home
from views.view_deal_item import deal_item_home
from views.view_team_member import team_member_home
from views.view_home import home
from models import *

app = Flask(__name__)
app.config.from_pyfile('setting.py')
app.debug = False
db.init_app(app)
app.config['SESSION_SQLALCHEMY'] = db
Session(app)

app.register_blueprint(home)
app.register_blueprint(admin_home, url_prefix='/admin')
app.register_blueprint(menu_home, url_prefix='/admin')
app.register_blueprint(menu_item_home, url_prefix='/admin')
app.register_blueprint(deal_home, url_prefix='/admin')
app.register_blueprint(deal_item_home, url_prefix='/admin')
app.register_blueprint(team_home, url_prefix='/admin')
app.register_blueprint(team_member_home, url_prefix='/admin')


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run()
