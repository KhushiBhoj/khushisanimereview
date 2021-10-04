from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/ps5'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(app)
class contactus(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    email = db.Column(db.String(40), nullable=False)
    feedback = db.Column(db.String(500), nullable=False)

@app.route("/")
def home():
    return render_template('Home.html')

@app.route("/features")
def features():
    return render_template('Features.html')

@app.route("/reviews")
def reviews():
    return render_template('Reviews.html')

@app.route("/updates")
def updates():
    return render_template('404.html')

@app.route("/contact", methods = ['GET', 'POST'])
def contact():
    if(request.method=='POST'):
        name = request.form.get('name')
        email = request.form.get('email')
        feedback = request.form.get('feedback')
        # print(name, email, feedback)
        entry = contactus(name=name, email = email, feedback = feedback)
        db.session.add(entry)
        db.session.commit()
    return render_template('home.html')

if __name__=="__main__":
    app.run(debug=True)