from . import db

class Task(db.Model):
  taskId = db.Column(db.Integer, primary_key=True)
  taskCreatorId = db.Column(db.Integer)
  taskName = db.Column(db.String(100))
  taskDescription = db.Column(db.String(500))

class HelperInstance(db.Model):
  helperInstanceId = db.Column(db.Integer, primary_key=True)
  helperInstanceTaskId = db.Column(db.Integer)
  helperInstanceName = db.Column(db.Integer)