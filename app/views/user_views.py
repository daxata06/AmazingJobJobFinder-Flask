from flask import Flask, render_template, request, redirect, flash, get_flashed_messages
from app.models.user import *
from config import *
from . import views
from sqlalchemy.sql.expression import func
from flask_login import current_user


@views.route('/')
def index():
    print(current_user.is_authenticated)
    name_username = users.query.order_by(func.random()).limit(5).all()

    id_=current_user.get_id()
    is_user=True

    User = users.query.filter_by(id_=id_).first()

    if not User:
       is_user=False

    avatars_urls = {user.id_: get_avatar(user.id_) for user in name_username}

    return render_template("home_page.html",
                           name_username=name_username,
                           avatars_urls=avatars_urls,
                           is_user=is_user)

@views.route('/search', methods=['POST', 'GET'])
def search():
    datas = []
    if request.method == 'POST':
        profession_ = request.form['profession']

        if profession_!='':
         
         datas = users.query.filter(users.profession.like(f"%{profession_}%")).all()
         avatars_urls = {user.id_: get_avatar(user.id_) for user in datas}

         return render_template('search.html', 
                                datas=datas,
                               avatars_urls=avatars_urls)

    return render_template('search.html', datas=datas)


@views.route('/emp_page', methods=['POST', 'GET'])
def emp_page():
   
   return render_template("for_employers.html")


@views.errorhandler(404)
def page_not_found(e):
    return 'not found', 404

