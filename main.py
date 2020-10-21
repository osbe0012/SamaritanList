from flask import Blueprint, render_template, redirect, url_for, request, jsonify
from .models import Task, HelperInstance
from . import db, TaskForm, HelperForm
import requests

main = Blueprint('main', __name__)

def getTasks():
  results = db.session.execute(f'select taskId, taskName, taskDescription from task')
  rows = results.fetchall()
  return rows
  
def getHelpers():
  results = db.session.execute(f'select helperInstanceTaskId, helperInstanceName from helper_instance')
  rows = results.fetchall()
  return rows

@main.route('/')
@main.route('/tasks')
def tasks():
  taskForm = TaskForm()
  tasks = getTasks()
  helpers = getHelpers()
  return render_template('tasks.html', tasks=tasks, helpers = helpers, taskForm=taskForm)
  
@main.route('/tasks/new', methods=['GET', 'POST'])
def newTask():
  taskForm = TaskForm()
  helpers = getHelpers()
  if taskForm.validate_on_submit():
    count = db.session.query(Task).count()
    task = Task(taskId=count+1, taskName=taskForm.taskName.data, taskDescription=taskForm.taskDescription.data)
    db.session.add(task)
    db.session.commit()
    tasks = getTasks()
    return render_template('tasks.html', tasks=tasks, helpers=helpers, taskForm=taskForm)
  tasks = getTasks()
  return render_template('tasks.html', tasks=tasks, helpers=helpers, taskForm=taskForm)

@main.route('/helper/<taskId>', methods=['GET', 'POST'])
def helper(taskId):
  helperForm = HelperForm()
  return render_template('helper.html', taskId=taskId, helperForm=helperForm)

@main.route('/helper/new/<taskId>', methods=['GET', 'POST'])
def newHelper(taskId):
  helperForm = HelperForm()
  taskForm = TaskForm()
  tasks = getTasks()
  if helperForm.validate_on_submit():
    count = db.session.query(HelperInstance).count()
    helper = HelperInstance(helperInstanceId=count+1, helperInstanceTaskId=taskId, helperInstanceName=helperForm.helperInstanceName.data)
    db.session.add(helper)
    db.session.commit()
    helpers = getHelpers()
    return render_template('tasks.html', tasks=tasks, helpers=helpers, helperForm=helperForm, taskForm=taskForm)
  helpers = getHelpers()
  return render_template('tasks.html', tasks=tasks, helpers=helpers, helperForm=helperForm, taskForm=taskForm)