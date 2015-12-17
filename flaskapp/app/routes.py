from flask import Flask, render_template, request, flash,redirect,url_for
from forms import ContactForm
from forms1 import ContactForm1
from forms2 import ContactForm2
from forms3 import ContactForm3

from flask.ext.mail import Message, Mail
app = Flask(__name__) 
 
app.secret_key = 'development key'


@app.route('/')
def home():
  return render_template('home.html')
  
@app.route('/about')
def about():
  return render_template('about.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
  form = ContactForm()
 
  if request.method == 'POST':
    return redirect(url_for('contact1'))

  elif request.method == 'GET':
    return render_template('contact.html', form=form)

@app.route('/contact1', methods=['GET', 'POST'])
def contact1():
  form = ContactForm1()
 
  if request.method == 'POST':
     return redirect(url_for('contact2'))

  elif request.method == 'GET':
    return render_template('contact1.html', form=form)

@app.route('/contact2', methods=['GET', 'POST'])
def contact2():
  form = ContactForm2()
 
  if request.method == 'POST':
     return redirect(url_for('contact3'))


  elif request.method == 'GET':
    return render_template('contact2.html', form=form)

@app.route('/contact3', methods=['GET', 'POST'])
def contact3():
  form = ContactForm3()
 
  if request.method == 'POST':
     return "form posted"


  elif request.method == 'GET':
    return render_template('contact3.html', form=form)    

      
if __name__ == '__main__':
  app.run(debug=True)
