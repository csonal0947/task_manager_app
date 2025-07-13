from flask import Flask, render_template, request, redirect, url_for
from models import db, Task
from config import config       


app = Flask(__name__)
app.config.from_object(config)
db.init_app(app)

with app.app_context():
    print("Creating database tables...")
    db.create_all()
    print("Database tables created successfully.")

@app.route('/')
def index():
    tasks = Task.query.order_by(Task.created_at.desc()).all()
    return render_template('index.html', tasks=tasks)    

@app.route('/add', methods=['POST'])
def add_task():
    title = request.form.get('title')
    description = request.form.get('description')
    new_task = Task(title=title, description=description)
    db.session.add(new_task)
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/delete/<int:id>')
def delete_task (id):
    task = Task.query.get_or_404(id)
    db.session.delete(task)
    db.session.commit()
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)
