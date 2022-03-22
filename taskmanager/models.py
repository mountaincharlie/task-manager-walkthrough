# we need to import the SQLAlchemy db to define things in our db
from taskmanager import db


# table for various categories with SQLAlchemy's model
class Category(db.Model):
    # schema for the Category model
    id = db.Column(db.Integer, primary_key=True)
    # max 25 chars & must be unique & is required
    category_name = db.Column(db.String(25), unique=True, nullable=False)
    # not a column, just to ref the one-to-many relationship
    tasks = db.relationship("Task", backref="category", cascade="all, delete", lazy=True)

    def __repr__(self):
        # to represent itself in the form of a string
        return self.category_name


# table for each task created
class Task(db.Model):
    # schema for the Task model
    id = db.Column(db.Integer, primary_key=True)
    # max 50 chars & must be unique & is required
    task_name = db.Column(db.String(50), unique=True, nullable=False)
    task_description = db.Column(db.Text, nullable=False)
    is_urgent = db.Column(db.Boolean, default=False, nullable=False)
    due_date = db.Column(db.Date, nullable=False)
    # ondelete cascade => if the cat is deleted all associated tasks will be
    category_id = db.Column(db.Integer, db.ForeignKey("category.id", ondelete="CASCADE"), nullable=False)

    def __repr__(self):
        # to represent itself in the form of a string
        return f"#{self.id} - Task:{self.task_name} | Urgent:{self.is_urgent}"
