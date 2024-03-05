from flask import Flask, render_template, request, redirect, flash, get_flashed_messages
from app.models.user import *
from config import *
from . import views
from sqlalchemy.sql.expression import func


@views.route('/')
def index():
    name_username = users.query.order_by(func.random()).limit(5).all()

    avatars_urls = {user.id_: get_avatar(user.id_) for user in name_username}
    return render_template("home_page.html",
                           name_username=name_username,
                           avatars_urls=avatars_urls)

