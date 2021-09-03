from flask import Blueprint, render_template, request, redirect, url_for

team_home = Blueprint('team_home', __name__, static_folder='static', template_folder='template')


@team_home.route('/team')
def home():
    return render_template('admin/table_team_category.html')


@team_home.route('/team_add')
def add():
    return render_template('admin/form_team_category.html')


@team_home.route('/team_edit')
def edit():
    return render_template('admin/form_team_category.html')


@team_home.route('/team_delete')
def delete():
    return render_template('admin/table_team_category.html')