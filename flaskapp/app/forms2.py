from wtforms import Form, TextField, TextAreaField, SubmitField, validators, ValidationError , 	IntegerField
 
 
class ContactForm2(Form):
  colname = TextField("Employer name")
  city2 = TextField("City")
  state2 = TextField("State")
  country2 = TextField("Country")
  degree = TextField("Degree/Programme")
  submit = SubmitField("Next")
