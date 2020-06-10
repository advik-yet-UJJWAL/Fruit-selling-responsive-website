from flask import Flask,render_template,request
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root@localhost/Tiwari_fruit'
db = SQLAlchemy(app)

class Contact(db.Model):

    '''
    Sno,Name,Email,Msg,Phone,Date
    '''
    Sno = db.Column(db.Integer, primary_key=True)
    Name= db.Column(db.String(50), unique=False, nullable=False)
    Email =db.Column(db.String(120), unique=False, nullable=False)
    Msg = db.Column(db.String(220), unique=False, nullable=False)
    Phone = db.Column(db.String(120), unique=False, nullable=False)
    Date = db.Column(db.String(120), unique=False, nullable=False)



@app.route("/")
def home():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/gallery")
def gallery():
    return render_template("gallery.html")

@app.route("/distributers")
def distributers():
    return render_template("distributers.html")

@app.route("/codes")
def codes():
    return render_template("codes.html")

@app.route("/order")
def order():
    return render_template("order.html")

@app.route("/contact", methods = ['GET','POST'])
def contact():

    if(request.method=="POST"):
        '''
        Sno,Name,Email,Msg,Phone,Date
        '''
        '''
        variable = request.form.get("name_of_element_html_page")
        '''
        name_form = request.form.get("name") 
        email_form = request.form.get("email")
        msg_form = request.form.get("msg")
        phone_form = request.form.get("phn")


        #entry to database having table contact table_name(db_variable=variable upar wala)
        entry = Contact(Name=name_form, Email=email_form, Msg=msg_form, Phone=phone_form)

        db.session.add(entry)
        db.session.commit()
        
    return render_template("contact.html")

app.run(debug=True)