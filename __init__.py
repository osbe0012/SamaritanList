from flask import Flask, request, Response, render_template
from flask_login import LoginManager, current_user
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from flask_wtf.csrf import CSRFProtect
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField
from wtforms.validators import Regexp
import requests
import itertools
import re
import os


db = SQLAlchemy()

class TaskForm(FlaskForm):
  taskName = StringField("Task Name: ", validators= [
        Regexp(r'^[a-z\,\-\' ]+$', re.IGNORECASE, \
          message="Must contain letters, commas, apostrophes, or hyphens only, and may not be blank")
    ])
  taskDescription = StringField("Task Description: ", validators= [
        Regexp(r'^[a-z\,\-\' ]+$', re.IGNORECASE, \
          message="Must contain letters, commas, apostrophes, or hyphens only, and may not be blank")
    ])
  submit = SubmitField("Create New Task")

class HelperForm(FlaskForm):
  helperInstanceName = StringField("Your Name: ", validators= [
        Regexp(r'^[a-z\,\-\' ]+$', re.IGNORECASE, \
          message="Must contain letters, commas, apostrophes, or hyphens only, and may not be blank")
    ])
  taskId = IntegerField()
  submit = SubmitField("Submit")  

def create_app():
  app = Flask(__name__)
  Bootstrap(app)
  #csrf = CSRFProtect()
  app.config["SECRET_KEY"] = "row the boat"
  app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
  #csrf.init_app(app)
  app._static_folder = 'static'

  db.init_app(app)

  from .main import main as main_blueprint
  app.register_blueprint(main_blueprint)
  
  return app
  
if not os.path.exists("db.sqlite"):
  db.create_all(app=create_app())