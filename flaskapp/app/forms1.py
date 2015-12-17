from wtforms import Form, TextField, TextAreaField, SubmitField, validators, ValidationError , 	IntegerField
 
 
class ContactForm1(Form):
  empname = TextField("Employer name")
  city1 = TextField("City")
  state1 = TextField("State")
  country1 = TextField("Country")
  postitle = TextField("Position title")
  startdate = TextField("Start date")
  enddate = TextField("End date")
  submit = SubmitField("Next")
