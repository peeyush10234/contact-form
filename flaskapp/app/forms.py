from wtforms import Form, TextField, TextAreaField, SubmitField,IntegerField
 
 
class ContactForm(Form):
  firstname = TextField("First name")
  lastname = TextField("Last name")
  country = TextField("Country")
  address1 = TextField("Address1")
  address2 = TextField("Address2")
  city = TextField("City")
  state = TextField("State")
  zipcode = IntegerField("Zip code")
  phone = IntegerField("Phone")
  email = TextField("Email")
  submit = SubmitField("Next")
