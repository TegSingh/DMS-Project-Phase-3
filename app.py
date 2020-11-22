from flask import Flask, json, render_template, request, redirect, flash
from flaskext.mysql import MySQL
from forms import booksForm, branchForm, borrowerForm, employeeForm
import yaml

app = Flask(__name__)

db = yaml.load(open('dbconfig.yaml'))
app.config['MYSQL_DATABASE_HOST'] = db['mysql_host']
app.config['MYSQL_DATABASE_USER'] = db['mysql_user']
app.config['MYSQL_DATABASE_PASSWORD'] = db['mysql_password']
app.config['MYSQL_DATABASE_DB'] = db['mysql_db']
mysql = MySQL(app)

# add secret key for encryption operations
app.secret_key = "phase3"

@app.route('/')
def index():
    return render_template('index.html')

# DISPLAY     
@app.route('/library_branch')
def branchDetails():
    connection = mysql.connect()
    cursor = connection.cursor()
    result = cursor.execute("SELECT * FROM library_branch")
    if result > 0: 
        branchDetails = cursor.fetchall()
        return render_template('library_branch.html', branchDetails = branchDetails)
    cursor.close()

# # EDIT
# @app.route('/library_branch/edit/<id>')
# def branchDetails():
#     connection = mysql.connect()
#     cursor = connection.cursor()
#     result = cursor.execute("SELECT * FROM library_branch")
#     if result > 0: 
#         branchDetails = cursor.fetchall()
#         return render_template('library_branch.html', branchDetails = branchDetails)
#     cursor.close()

# DELETE
@app.route('/library_branch/delete/<id>')
def deleteBranch(id):
    connection = mysql.connect()
    cursor = connection.cursor()
    cursor.execute("DELETE FROM library_branch WHERE branchID = %s", id)
    connection.commit()
    return redirect('/library_branch')
    flash("Branch removed successfully")
    cursor.close()

# INSERT
@app.route('/library_branch/insert', methods = ['POST'])
def insertBranch():
    if request.method == 'POST':
        # Create the cursor
        connection = mysql.connect()
        cursor = connection.cursor()
        # Initialize the entered values
        branchID = request.form['branchID']
        branchName = request.form['branchName']
        branchLocation = request.form['branchLocation']
        capacity = request.form['capacity']
        numberOfEmployee = request.form['numberOfEmployee']
        numberOfBooks = request.form['numberOfBooks']
        cursor.execute(
            "INSERT INTO library_branch VALUES (%s, %s, %s, %s, %s, %s)", 
            (branchID, branchName, branchLocation, capacity, numberOfEmployee, numberOfBooks)
        )
        connection.commit()
        flash("Branch added successfully")
        return redirect('/library_branch')
        cursor.close()

# DISPLAY
@app.route('/books')
def bookDetails():
    connection = mysql.connect()
    cursor = connection.cursor()
    result = cursor.execute("SELECT * FROM books")
    if result > 0: 
        bookDetails = cursor.fetchall()
        return render_template('books.html', bookDetails = bookDetails)
    cursor.close()

# # EDIT 
# @app.route('/books/edit/<id>')
# def branchDetails():
#     connection = mysql.connect()
#     cursor = connection.cursor()
#     result = cursor.execute("SELECT * FROM library_branch")
#     if result > 0: 
#         branchDetails = cursor.fetchall()
#         return render_template('library_branch.html', branchDetails = branchDetails)
#     cursor.close()

# DELETE
@app.route('/books/delete/<id>')
def deleteBook(id):
    connection = mysql.connect()
    cursor = connection.cursor()
    cursor.execute("DELETE FROM books WHERE ISBNnumber = %s", id)
    connection.commit()
    flash("book removed succesfully")
    return redirect('/books')
    cursor.close()

# INSERT
@app.route('/books/insert', methods = ['POST'])
def insertBooks():
    if request.method == 'POST':
        # Create the cursor
        connection = mysql.connect()
        cursor = connection.cursor()
        # Initialize the entered values
        ISBNbook = request.form['ISBNbooks']
        title = request.form['title']
        genre = request.form['genre']
        publisher = request.form['publisher']
        author = request.form['author_name']
        availability = request.form['availability']
        numberOfCopies = request.form['numberOfCopies']
        borrowerIDbooks = request.form['borrowerIDbooks']
        branchIDbooks = request.form['branchIDbooks']
        dateReturn = request.form['dateReturnBooks']
        dateBorrowedBooks = request.form['dateBorrowedBook']
        cursor.execute(
            "INSERT INTO books VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", 
            (ISBNbook, title, genre, publisher, author, availability, numberOfCopies, borrowerIDbooks, branchIDbooks, dateReturn, dateBorrowedBooks)
        )
        connection.commit()
        flash("Book added successfully")
        return redirect('/books')
        cursor.close()

# DISPLAY
@app.route('/employee')
def employeeDetails():
    connection = mysql.connect()
    cursor = connection.cursor()
    result = cursor.execute("SELECT * FROM employee")
    if result > 0: 
        employeeDetails = cursor.fetchall()
        return render_template('employee.html', employeeDetails = employeeDetails)
    cursor.close()

# # EDIT
# @app.route('/employee/edit/<id>')
# def branchDetails():
#     connection = mysql.connect()
#     cursor = connection.cursor()
#     result = cursor.execute("SELECT * FROM library_branch")
#     if result > 0: 
#         branchDetails = cursor.fetchall()
#         return render_template('library_branch.html', branchDetails = branchDetails)
#     cursor.close()

# DELETE
@app.route('/employee/delete/<id>')
def deleteEmployee(id):
    connection = mysql.connect()
    cursor = connection.cursor()
    cursor.execute("DELETE FROM employee WHERE ID = %s", id)
    connection.commit()
    return redirect("/employee")
    flash("employee removed succesfully")
    cursor.close()

# INSERT
@app.route('/employee/insert', methods = ['POST'])
def insertEmployee():
    if request.method == 'POST':
        # Create the cursor
        connection = mysql.connect()
        cursor = connection.cursor()
        # Initialize the entered values
        employeeID = request.form['employeeID']
        employeeName = request.form['employeeName']
        employeeTitle = request.form['employeeTitle']
        branchIDemployee = request.form['branchIDemployee']
        weeklyHours = request.form['weeklyHours']
        hourlyWages = request.form['hourlyWages']
        cursor.execute(
            "INSERT INTO employee VALUES (%s, %s, %s, %s, %s, %s)", 
            (employeeID, employeeName, employeeTitle, branchIDemployee, weeklyHours, hourlyWages)
        )
        connection.commit()
        return redirect('/employee')
        flash("Record added succesfully")
        cursor.close()

# DISPLAY
@app.route('/borrower')
def borrowerDetails():
    connection = mysql.connect()
    cursor = connection.cursor()
    result = cursor.execute("SELECT * FROM borrower")
    if result > 0: 
        borrowerDetails = cursor.fetchall()
        return render_template('borrower.html', borrowerDetails = borrowerDetails)
    cursor.close()

# # EDIT
# @app.route('/borrower/edit/<id>')
# def branchDetails():
#     connection = mysql.connect()
#     cursor = connection.cursor()
#     result = cursor.execute("SELECT * FROM library_branch")
#     if result > 0: 
#         branchDetails = cursor.fetchall()
#         return render_template('library_branch.html', branchDetails = branchDetails)
#     cursor.close()

# DELETE
@app.route('/borrower/delete/<id>')
def deleteBorrower(id):
    connection = mysql.connect()
    cursor = connection.cursor()
    cursor.execute("DELETE FROM borrower WHERE id = %s", id)
    connection.commit()
    return redirect('/borrower')
    flash("borrower removed succesfully")
    cursor.close()

# INSERT
@app.route('/borrower/insert', methods = ['POST'])
def insertBorrower():
    if request.method == 'POST':
        # Create the cursor
        connection = mysql.connect()
        cursor = connection.cursor()
        # Initialize the entered values
        borrowerIDnew = request.form['borrowerIDnew']
        borrowerName = request.form['borrowerName']
        email = request.form['email']
        phoneNumber = request.form['phoneNumber']       
        cursor.execute(
            "INSERT INTO borrower VALUES (%s, %s, %s, %s)", 
            (borrowerIDnew, borrowerName, email, phoneNumber)
        )
        connection.commit()
        return redirect('/borrower')
        cursor.close()

if __name__ == '__main__':
    app.run(debug = True)
