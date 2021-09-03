# RestaurantAppPublic
Application with landing page and admin panel for resturant to advertise and manage menu and deals.


# Description
Public view of commercial project.
Its an application developed using Flask and MySQL as backend.
HTML, CSS, JavaScript and jQuery as frontend(Referred Bootstrap and Google Searches).
For image storage used Cloudinary API to upload images.

# Application Funcationality(Public)
- Login
- Logout
- Home page
- Admin Panel
- Add/View/Update/Delete Menu Category
- Add/View/Update/Delete Menu Item
- Add/View/Update/Delete Deal Category
- Add/View/Update/Delete Deal Item

# Requirements
- cachelib==0.3.0
- certifi==2021.5.30
- click==8.0.1
- cloudinary==1.26.0
- colorama==0.4.4
- Flask==2.0.1
- Flask-MySQLdb==0.2.0
- Flask-Session==0.4.0
- Flask-SQLAlchemy==2.5.1
- greenlet==1.1.1
- gunicorn==20.1.0
- itsdangerous==2.0.1
- Jinja2==3.0.1
- MarkupSafe==2.0.1
- mysqlclient==2.0.3
- PyMySQL==1.0.2
- python-dotenv==0.19.0
- six==1.16.0
- SQLAlchemy==1.4.23
- urllib3==1.26.6
- Werkzeug==2.0.1


# Database Design
- menu Table
  | Field         | Type          | Key           |
  | ------------- | ------------- | ------------- |
  | menu_id       | Int           | PK            |
  | menu_name     | Varchar       |               |
  | menu_image | Text       |               |
  
- menu_item Table
  | Field              | Type          | Key           |
  | ------------------ | ------------- | ------------- |
  | menu_item_id        | Int           | PK            |
  | menu_id          | Int       |     FK(user)           |
  | menu_item_name | Varchar           |      |
  | menu_item_description | Text           |        |
  | menu_item_price    | Float       |               |
  | menu_item_image | Text       |               |
  
- deal Table
  | Field                | Type          | Key           |
  | -------------------- | ------------- | ------------- |
  | deal_id           | Int           | PK            |
  | deal_name | Varchar           | FK(user)      |
  | deal_description   | Text           |        |
  | deal_start_date       | Varchar       |               |
  | deal_end_date       | Varchar       |               |
  | deal_week_day       | Varchar       |               |
  | deal_category_image       | Text       |               |
  
- deal Table
  | Field                | Type          | Key           |
  | -------------------- | ------------- | ------------- |
  | deal_item_id           | Int           | PK            |
  | deal_id | Int           | FK(user)      |
  | deal_item_name   | Varchar           |       |
  | deal_item_description       | Text       |               |
  | deal_item_price       | Float       |               |
  | deal_item_discounted_price       | Float       |               |
  | deal_item_image       | Text       |               |
