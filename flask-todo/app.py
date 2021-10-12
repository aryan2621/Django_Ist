from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'hjshjhdjah kjshkjdhjs'

db = SQLAlchemy(app)


class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    complete = db.Column(db.Boolean)


@app.route("/")
def index():
    todo_list = Todo.query.all()
    print(todo_list)
    return render_template("base.html", todo_list=todo_list)


@app.route("/add", methods=["POST"])
def add():
    if request.method == "POST":
        title = request.form.get("title")
        if title == '':
            flash("Please enter the valid  Title ", category="error")
            return redirect(url_for("index"))

        else:
            new_Todo = Todo(title=title, complete=False)
            db.session.add(new_Todo)
            db.session.commit()
            flash("List Added Successfully", category="success")
            return redirect(url_for("index"))



@app.route("/update/<int:todo_id>")
def update(todo_id):
    todo = Todo.query.filter_by(id=todo_id).first()
    todo.complete = not todo.complete
    db.session.commit()
    return redirect(url_for("index"))


@app.route("/delete/<int:todo_id>")
def delete(todo_id):
    todo = Todo.query.filter_by(id=todo_id).first()
    db.session.delete(todo)
    db.session.commit()
    return redirect(url_for("index"))


if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)
