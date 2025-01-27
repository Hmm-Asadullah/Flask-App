from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///todo.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Todo(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    desc = db.Column(db.String(500), nullable=False)
    date = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self) -> str:
        return f"{self.sno} - {self.title}"

@app.route('/', methods=['GET', 'POST'])
def hello_world():
    if request.method == 'POST':
        title = request.form["title"]
        desc =  request.form["desc"]
        todo = Todo(title=title, desc=desc)
        db.session.add(todo)
        db.session.commit()
    
    allTodo = Todo.query.all() 
    return render_template('index.html', allTodo=allTodo)

@app.route('/show')
def products():
    allTodo = Todo.query.all()
    print(allTodo)
    return 'this is products page'

@app.route('/delete/<int:sno>')
def delete(sno):
    todo = Todo.query.filter_by(sno=sno).first()
    db.session.delete(todo)
    db.session.commit()
    return redirect("/")
 
@app.route('/update/<int:sno>', methods=['GET', 'POST'])
def update(sno):
    if request.method == 'POST':
        title = request.form["title"]
        desc =  request.form["desc"]
        todo = Todo.query.filter_by(sno=sno).first()
        todo.title=title
        todo.desc=desc
        db.session.add(todo)
        db.session.commit()
        return redirect("/")
    todo = Todo.query.filter_by(sno=sno).first()
    return render_template('update.html', todo=todo)

if __name__ == "__main__":
    app.run(debug=True)



# from flask import Flask, render_template
# from flask_sqlalchemy import SQLAlchemy

# app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///form.db"
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# db = SQLAlchemy(app)

# class Form(db.Model):
#     email = db.Column(db.String(100),nullable=False)
#     pword = db.Column(db.String(100),nullable=False)
#     age = db.Column(db.Integer,primary_key=True)
#     add = db.Column(db.String(500),nullable=False)
#     city = db.Column(db.String(100),nullable=False)
#     zip = db.Column(db.Integer,primary_key=True)
#     __table_args__ = (db.UniqueConstraint('age', 'zip', name='unique_age_zip'),)

#     def __repr__(self):
#         return f"{self.email} - {self.city}"


# @app.route("/")
# def hello_world():
#     age = 19
#     zip_code = 5400

#     # Check if the combination already exists
#     existing_record = Form.query.filter_by(age=age, zip=zip_code).first()
#     if existing_record:
#         return "This combination of age and zip already exists in the database."

#     # Insert the new record
#     new_form = Form(email="asad@123", pword="4321", age=age, add="madni", city="lhr")
#     db.session.merge(new_form)
#     db.session.commit()
#     allForm = Form.query.all()

#     return render_template("index.html" , allForms = allForm)
#     # return "Form object created successfully!"
#     # form = Form(email="asad@123", pword="4321", age="19",add="madni", city="lhr", zip="5400")
#     # db.session.add(form)
#     # db.session.commit()
#     # # return "<p>Hello, World!</p>"

# @app.route("/show")
# def home():
#     allForm = Form.query.all()
#     print(allForm)
#     return "this is home page"

# if __name__ ==  "__main__":
#     app.run(debug=True)