from extension import db


class Menu(db.Model):
    __tablename__ = 'menu'
    menu_id = db.Column(db.Integer, primary_key=True)
    menu_name = db.Column(db.String(50))
    menu_image = db.Column(db.Text)

    def __init__(self, menu_name, menu_image):
        self.menu_name = menu_name
        self.menu_image = menu_image


class MenuItem(db.Model):
    __tablename__ = 'menu_item'
    menu_item_id = db.Column(db.Integer, primary_key=True)
    menu_id = db.Column(db.Integer, db.ForeignKey('menu.menu_id'))
    menu_item_name = db.Column(db.String(50))
    menu_item_description = db.Column(db.Text)
    menu_item_price = db.Column(db.String(20))
    menu_item_image = db.Column(db.Text)

    def __init__(self, menu_id, menu_item_name, menu_item_description, menu_item_price,
                 menu_item_image):
        self.menu_id = menu_id
        self.menu_item_name = menu_item_name
        self.menu_item_description = menu_item_description
        self.menu_item_price = menu_item_price
        self.menu_item_image = menu_item_image


class Deal(db.Model):
    __tablename__ = 'deal'
    deal_id = db.Column(db.Integer, primary_key=True)
    deal_name = db.Column(db.String(50))
    deal_description = db.Column(db.Text)
    deal_start_date = db.Column(db.String(20))
    deal_end_date = db.Column(db.String(20))
    deal_week_day = db.Column(db.String(10))
    deal_category_image = db.Column(db.Text)

    def __init__(self, deal_name, deal_description, deal_start_date, deal_end_date, deal_week_day,
                 deal_category_image):
        self.deal_name = deal_name
        self.deal_description = deal_description
        self.deal_start_date = deal_start_date
        self.deal_end_date = deal_end_date
        self.deal_week_day = deal_week_day
        self.deal_category_image = deal_category_image


class DealItem(db.Model):
    __tablename__ = 'deal_item'
    deal_item_id = db.Column(db.Integer, primary_key=True)
    deal_id = db.Column(db.Integer, db.ForeignKey('deal.deal_id'))
    deal_item_name = db.Column(db.String(50))
    deal_item_description = db.Column(db.Text)
    deal_item_price = db.Column(db.String(20))
    deal_item_discounted_price = db.Column(db.String(20))
    deal_item_image = db.Column(db.Text)

    def __init__(self, deal_id, deal_item_name, deal_item_description, deal_item_price,
                 deal_item_discounted_price, deal_item_image):
        self.deal_id = deal_id
        self.deal_item_name = deal_item_name
        self.deal_item_description = deal_item_description
        self.deal_item_price = deal_item_price
        self.deal_item_discounted_price = deal_item_discounted_price
        self.deal_item_image = deal_item_image


class Team(db.Model):
    __tablename__ = 'team'
    team_id = db.Column(db.Integer, primary_key=True)
    team_name = db.Column(db.String(50))
    team_description = db.Column(db.Text)

    def __init__(self, team_name, team_description):
        self.team_name = team_name
        self.team_description = team_description


class TeamMember(db.Model):
    __tablename__ = 'team_member'
    team_member_id = db.Column(db.Integer, primary_key=True)
    team_category_id = db.Column(db.Integer, db.ForeignKey('team.team_id'))
    team_member_name = db.Column(db.String(50))
    team_member_email = db.Column(db.String(100))
    team_member_phone = db.Column(db.String(20))
    team_member_image = db.Column(db.Text)
    team_member_address = db.Column(db.Text)
    team_member_display = db.Column(db.String(10))
    team_member_account = db.Column(db.String(20))
    team_member_password = db.Column(db.Text)

    def __init__(self, team_category_id, team_member_name, team_member_email, team_member_phone,
                 team_member_image, team_member_address, team_member_display, team_member_account, team_member_password):
        self.team_category_id = team_category_id
        self.team_member_name = team_member_name
        self.team_member_email = team_member_email
        self.team_member_phone = team_member_phone
        self.team_member_image = team_member_image
        self.team_member_address = team_member_address
        self.team_member_display = team_member_display
        self.team_member_account = team_member_account
        self.team_member_password = team_member_password
