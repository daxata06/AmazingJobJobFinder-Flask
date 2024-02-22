from flask import Flask, render_template, request, redirect, flash, get_flashed_messages
from app.models.user import *
from config import *
from . import views


@views.route('/')
def index():
    return render_template("home_page.html")

