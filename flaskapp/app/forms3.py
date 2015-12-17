from wtforms import Form, TextField, TextAreaField, SubmitField, validators, ValidationError , 	IntegerField
 
 
class ContactForm3(Form):
  message = TextAreaField("Info")
  submit = SubmitField("Send")
