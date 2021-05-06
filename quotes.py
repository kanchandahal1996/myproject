from flask import Flask ,render_template,request,redirect,url_for
from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)

#app.config['SQLALCHEMY_DATABASE_URI'] ='postgresql+psycopg2://postgres:12345@localhost/quotes'
#app.config['SQLALCHEMY_DATABASE_URI'] ='postgres://vgobpiolhluwzp:4741d08c5dec5186a5b23307bb29d6dc8774a3d4c81fe968feab514622ae1ffe@ec2-54-152-185-191.compute-1.amazonaws.com:5432/d9aio8c9mfrl1u'
app.config['SQLALCHENY_DATABASE_URL']='postgres://vgobpiolhluwzp:4741d08c5dec5186a5b23307bb29d6dc8774a3d4c81fe968feab514622ae1ffe@ec2-54-152-185-191.compute-1.amazonaws.com:5432/d9aio8c9mfrl1u'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS']= False





db=SQLAlchemy(app)

class Favquotes(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    author=db.Column(db.String(30))
    quote=db.Column(db.String(2000))




@app.route('/')
def index():
    result=Favquotes.query.all()
    return render_template('index.html',result=result)



@app.route('/quotes')
def quotes():
    return render_template('quotes.html')

@app.route('/process',methods=['POST'])
def process():
    author=request.form['author']
    quote=request.form['quote']
    quotedata=Favquotes(author=author,quote=quote)
    db.session.add(quotedata)
    db.session.commit()
    
    return redirect(url_for('index'))




if __name__ == '__main__':
    app.run()