from flask import Blueprint, render_template, request, redirect, url_for

team_member_home = Blueprint('team_member_home', __name__, static_folder='static', template_folder='template')


@team_member_home.route('/team_member')
def home():
    return render_template('admin/table_team_member.html')


@team_member_home.route('/team_member_add')
def add():
    return render_template('admin/form_team_member.html')


@team_member_home.route('/team_member_edit')
def edit():
    return render_template('admin/form_team_member.html')


@team_member_home.route('/team_member_delete')
def delete():
    return render_template('admin/table_team_member.html')
