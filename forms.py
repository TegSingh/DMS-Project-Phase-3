from flask_wtf import Form
from wtforms import TextField, IntegerField, TextAreaField, SubmitField, RadioField, SelectField, DateField, BooleanField
from wtforms import validators, ValidationError

# ID, name location, capacity, total employees, number of books 
class branchForm(Form):
    ID = IntegerField("Branch ID: ",[validators.Required("Please enter a branch ID")])
    name = TextField("Branch name: ", [validators.Required("Please enter the branch name")])
    location = TextField("Branch location: ", [validators.Required("Please enter a valid branch location")])
    capacity = IntegerField("Branch Capacity: ", [validators.Required("Please enter the branch capacity")])
    numberOfEmployees = IntegerField("Number of Employees: ", [validators.Required("Please enter the number of employees")])
    numberOfBooks= IntegerField("Number of Books:  ", [validators.Required("Please enter the number of books")])
    branchSubmit = SubmitField("Submit")

class booksForm(Form):
    ISBN = TextField("ISBN Number: ",[validators.Required("Please enter ISBN")])
    title = TextField("Title: ", [validators.Required("Please enter a book title")])
    genre = TextField("Genre: ", [validators.Required("Please enter genre")])
    publisher = TextField("Publisher Name: ", [validators.Required("Please enter the publisher name")])
    author = TextField("Author Name: ", [validators.Required("Please enter Author name")])
    availability = BooleanField("Availability:  ", [validators.Required("Please enter book availability")])
    numberOfCopies = IntegerField("Number of Copies:  ", [validators.Required("Please enter the number of copies")])
    borrowerID = TextField("Number of Books: ")
    branchID = IntegerField("Number of Books: ", [validators.Required("Please enter a valid branch number")])
    bookDateReturn = DateField("Date to be returned: ", format = '%Y-%m-%d')
    bookateBorrowed = DateField("Date when borrowed: ", format = '%Y-%m-%d')
    bookSubmit = SubmitField("Submit")

class employeeForm(Form):
    employeeID = IntegerField("Employee ID: ",[validators.Required("Please enter a employee ID")])
    employeeName = TextField("Employee name: ", [validators.Required("Please enter the employee name")])
    employeeTitle = TextField("Employee title: ", [validators.Required("Please enter a valid employee title")])
    employeeBranchID = IntegerField("Employee Branch ID: ", [validators.Required("Please enter the branch ID")])
    workHours = IntegerField("Weekly number of hours: ", [validators.Required("Please enter the number of hours")])
    hourlyWages= IntegerField("Hourly wage:  ", [validators.Required("Please enter the hourly wage")])
    employeeSubmit = SubmitField("Submit")

class borrowerForm(Form):
    borrowerID = TextField("Borrower ID: ",[validators.Required("Please enter ID")])
    BorrowerName = TextField("Borrower name: ", [validators.Required("Please enter the name")])
    email = TextField("Branch location: ", [validators.Required("Please enter a valid email")])
    phoneNumber = IntegerField("Branch Capacity: ", [validators.Required("Please enter the phone number")])
    borrowerBookISBN = TextField("Number of Employees: ")
    borrowerDateReturn = DateField("Date to be returned: ", format = '%Y-%m-%d')
    borrowerDateBorrowed = DateField("Date when borrowed: ", format = '%Y-%m-%d')
    borrowerSubmit = SubmitField("Submit")


