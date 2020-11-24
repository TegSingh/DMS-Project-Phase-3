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

# Execute the following function when the app route is at localhost
@app.route('/')
def homePage():
    return render_template('home.html') 

@app.route('/login', methods = ['POST'])
def employeeLogin():
    if request.method == 'POST':    
        connection = mysql.connect()
        cursor = connection.cursor()
        employeeLoginName = request.form['employeeLoginName']
        employeeLoginID = request.form['employeeLoginID']
        result = cursor.execute("SELECT * FROM employee WHERE name = %s AND ID = %s", (employeeLoginName, employeeLoginID))
        if result > 0: 
            return redirect('\employeeHome')
        cursor.close()

@app.route('/employeeHome')
def employeeHome():
    return render_template("index.html")

@app.route('/titleSearch', methods = ['POST'])
def searchBookByTitle():
    if request.method == 'POST':    
        connection = mysql.connect()
        cursor = connection.cursor()
        searchTitle = request.form['searchTitle']
        result = cursor.execute("SELECT * FROM books WHERE title = %s", searchTitle)
        if result > 0: 
            searchTitleDetails = cursor.fetchall()
            return render_template('bookSearch.html', searchDetails = searchTitleDetails)
        cursor.close()

    
@app.route('/authorSearch', methods = ['POST'])
def searchBookByAuthor():
    if request.method == 'POST':    
        connection = mysql.connect()
        cursor = connection.cursor()
        searchAuthor = request.form['searchAuthor']
        result = cursor.execute("SELECT * FROM books WHERE author_name = %s", searchAuthor)
        if result > 0: 
            searchAuthorDetails = cursor.fetchall()
            return render_template('bookSearch.html', searchDetails = searchAuthorDetails)
        cursor.close()
    
@app.route('/genreSearch', methods = ['POST'])
def searchBookByGenre():
    if request.method == 'POST':    
        connection = mysql.connect()
        cursor = connection.cursor()
        searchGenre = request.form['searchGenre']
        result = cursor.execute("SELECT * FROM books WHERE genre = %s", searchGenre)
        if result > 0: 
            searchGenreDetails = cursor.fetchall()
            return render_template('bookSearch.html', searchDetails = searchGenreDetails)
        cursor.close()    

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

# EDIT
@app.route('/library_branch/edit/<id>', methods = ['GET', 'POST'])
def editBranch(id):
    connection = mysql.connect()
    cursor = connection.cursor()
    result = cursor.execute("SELECT * FROM library_branch WHERE branchID = %s", id)
    if result > 0: 
        branchDetailsEdit = cursor.fetchall()
        return render_template('library_branchEdit.html', branchEdit = branchDetailsEdit[0])
    cursor.close()

# UPDATE
@app.route('/library_branch/update/<id>', methods = ['POST'])
def updateBranch(id):
    if request.method == 'POST':
        # Create the cursor
        connection = mysql.connect()
        cursor = connection.cursor()
        # Initialize the entered values
        branchNameEdit = request.form['branchNameEdit']
        branchLocationEdit = request.form['branchLocationEdit']
        capacityEdit = request.form['capacityEdit']
        numberOfEmployeeEdit = request.form['numberOfEmployeeEdit']
        numberOfBooksEdit = request.form['numberOfBooksEdit']
        cursor.execute(
            "UPDATE library_branch SET name = %s, location = %s, capacity = %s, employees_total = %s, number_of_books = %s WHERE branchID = %s", 
            (branchNameEdit, branchLocationEdit, capacityEdit, numberOfEmployeeEdit, numberOfBooksEdit, id)
        )
        connection.commit()
        flash("Branch added successfully")
        return redirect('/library_branch')
        cursor.close()

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

# EDIT 
@app.route('/books/edit/<id>', methods = ['GET','POST'])
def editBooks(id):
    connection = mysql.connect()
    cursor = connection.cursor()
    result = cursor.execute("SELECT * FROM books WHERE ISBNnumber = %s", id)
    connection.commit()
    if result > 0:
        bookDetailsEdit = cursor.fetchall()
    return render_template('booksEdit.html', bookEdit = bookDetailsEdit[0])
    cursor.close()

# UPDATE
@app.route('/books/update/<id>', methods = ['POST'])
def updateBooks(id):
    if request.method == 'POST':
        # Create the cursor
        connection = mysql.connect()
        cursor = connection.cursor()
        # Initialize the entered values
        titleEdit = request.form['titleEdit']
        genreEdit = request.form['genreEdit']
        publisherEdit = request.form['publisherEdit']
        authorEdit = request.form['author_nameEdit']
        availabilityEdit = request.form['availabilityEdit']
        numberOfCopiesEdit = request.form['numberOfCopiesEdit']
        borrowerIDbooksEdit = request.form['borrowerIDbooksEdit']
        branchIDbooksEdit = request.form['branchIDbooksEdit']
        dateReturnEdit = request.form['dateReturnBooksEdit']
        dateBorrowedBooksEdit = request.form['dateBorrowedBookEdit']
        cursor.execute(
            "UPDATE books SET title = %s, genre = %s, publisher = %s, author_name = %s, availability = %s, number_of_copies = %s, borrowerID = %s, branchID = %s, date_to_be_returned = %s, date_borrowed = %s WHERE ISBNnumber = %s", 
            (titleEdit, genreEdit, publisherEdit, authorEdit, availabilityEdit, numberOfCopiesEdit, borrowerIDbooksEdit, branchIDbooksEdit, dateReturnEdit, dateBorrowedBooksEdit, id)
        )
        connection.commit()
        flash("Book updated successfully")
        return redirect('/books')
        cursor.close()
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

# EDIT
@app.route('/employee/edit/<id>', methods = ['GET', 'POST'])
def editEmployee(id):
    connection = mysql.connect()
    cursor = connection.cursor()
    result = cursor.execute("SELECT * FROM employee WHERE ID = %s", id)
    connection.commit()
    if result > 0:
        employeeDetailsEdit = cursor.fetchall()
    return render_template('employeeEdit.html', employeeEdit = employeeDetailsEdit[0])
    cursor.close()

# UPDATE
@app.route('/employee/update/<id>', methods = ['POST'])
def updateEmployee(id):
    if request.method == 'POST':
        # Create the cursor
        connection = mysql.connect()
        cursor = connection.cursor()
        # Initialize the entered values
        employeeNameEdit = request.form['employeeNameEdit']
        employeeTitleEdit = request.form['employeeTitleEdit']
        branchIDemployeeEdit = request.form['branchIDemployeeEdit']
        weeklyHoursEdit = request.form['weeklyHoursEdit']
        hourlyWagesEdit = request.form['hourlyWagesEdit']
        cursor.execute(
            "UPDATE employee SET name = %s, title = %s, branchID = %s, work_hours = %s, hourly_wages = %s WHERE ID = %s", 
            (employeeNameEdit, employeeTitleEdit, branchIDemployeeEdit, weeklyHoursEdit, hourlyWagesEdit, id)
        )
        connection.commit()
        return redirect('/employee')
        flash("Record updated succesfully")
        cursor.close()

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

# EDIT FORM
@app.route('/borrower/edit/<id>', methods = ['GET', 'POST'])
def borrowerEdit(id):
    connection = mysql.connect()
    cursor = connection.cursor()
    result = cursor.execute("SELECT * FROM borrower WHERE ID = %s", id)
    if result > 0: 
        borrowerDetailsEdit = cursor.fetchall()
        return render_template('borrowerEdit.html', bid = borrowerDetailsEdit[0])
    cursor.close()

# UPDATE
@app.route('/borrower/update/<id>', methods = ['POST'])
def borrowerUpdate(id):
    connection = mysql.connect()
    cursor = connection.cursor()
    borrowerNameEdit = request.form['borrowerNameEdit']
    emailEdit = request.form['emailEdit']
    phoneNumberEdit = request.form['phoneNumberEdit']    
    cursor.execute("UPDATE borrower SET name = %s, email = %s, phone_number = %s WHERE id = %s", (borrowerNameEdit, emailEdit, phoneNumberEdit, id))
    connection.commit()
    cursor.close()
    return redirect('/borrower')

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

# VIEWS
@app.route('/views/1')
def view1():
    connection = mysql.connect()
    cursor = connection.cursor() 
    result = cursor.execute("SELECT borrower.name as borrower_name, borrower.ID, library_branch.branchID, books.author_name FROM library_system.books INNER JOIN library_system.library_branch ON books.BranchID = library_branch.branchID INNER JOIN library_system.borrower ON books.borrowerID = borrower.ID")
    if result > 0:
        view1 = cursor.fetchall()
    return render_template('/views/view1.html', view1 = view1)
    
@app.route('/views/2')
def view2():
    connection = mysql.connect()
    cursor = connection.cursor() 
    result = cursor.execute(" SELECT ALL avg(employee.hourly_wages), employee.branchID FROM library_system.employee WHERE hourly_wages > 16 GROUP BY employee.branchID")
    if result > 0:
        view2 = cursor.fetchall()
    return render_template('/views/view2.html', view2 = view2)

@app.route('/views/3')
def view3():
    connection = mysql.connect()
    cursor = connection.cursor() 
    result = cursor.execute("SELECT * FROM library_system.employee WHERE hourly_wages > (SELECT AVG(employee.hourly_wages) FROM library_system.employee WHERE employee.title = 'Manager');")
    if result > 0:
        view3 = cursor.fetchall()
    return render_template('/views/view3.html', view3 = view3)

@app.route('/views/4')
def view4():
    connection = mysql.connect()
    cursor = connection.cursor() 
    result = cursor.execute("SELECT borrower.name, books.title FROM library_System.books LEFT JOIN library_system.borrower ON borrower.ID = books.borrowerID UNION SELECT borrower.name, books.title FROM library_System.books RIGHT JOIN library_system.borrower ON borrower.ID = books.borrowerID")
    if result > 0:
        view4 = cursor.fetchall()
    return render_template('/views/view4.html', view4 = view4)

@app.route('/views/5')
def view5():
    connection = mysql.connect()
    cursor = connection.cursor() 
    result = cursor.execute("SELECT * FROM LIBRARY_BRANCH WHERE capacity > 300 UNION SELECT * FROM LIBRARY_BRANCH WHERE employees_total > 20")
    if result > 0:
        view5 = cursor.fetchall()
    return render_template('/views/view5.html', view5 = view5)

@app.route('/views/6')
def view6():
    connection = mysql.connect()
    cursor = connection.cursor() 
    result = cursor.execute("SELECT employee.name, employee.ID, (employee.hourly_wages*employee.work_hours) AS Salary FROM library_system.employee WHERE employee.hourly_wages*employee.work_hours = (SELECT MIN(employee.hourly_wages*employee.work_hours) FROM library_system.employee) OR employee.hourly_wages*employee.work_hours = (SELECT MAX(employee.hourly_wages*employee.work_hours) FROM library_system.employee);  ")
    if result > 0:
        view6 = cursor.fetchall()
    return render_template('/views/view6.html', view6 = view6)

@app.route('/views/7')
def view7():
    connection = mysql.connect()
    cursor = connection.cursor() 
    result = cursor.execute("SELECT books.author_name, COUNT(DISTINCT books.ISBNnumber) FROM library_system.books GROUP BY books.author_name;")
    if result > 0:
        view7 = cursor.fetchall()
    return render_template('/views/view7.html', view7 = view7)

@app.route('/views/8')
def view8():
    connection = mysql.connect()
    cursor = connection.cursor() 
    result = cursor.execute("SELECT employee.name, employee.ID, (employee.hourly_wages*employee.work_hours) AS Salary FROM library_system.employee ORDER BY employee.hourly_wages*employee.work_hours;")
    if result > 0:
        view8 = cursor.fetchall()
    return render_template('/views/view8.html', view8 = view8)

@app.route('/views/9')
def view9():
    connection = mysql.connect()
    cursor = connection.cursor() 
    result = cursor.execute("SELECT COUNT(DISTINCT ISBNnumber) AS Books_borrowed_in_November FROM library_system.books WHERE date_borrowed LIKE '%11%'")
    if result > 0:
        view9 = cursor.fetchall()
    return render_template('/views/view9.html', view9 = view9)

@app.route('/views/10')
def view10():
    connection = mysql.connect()
    cursor = connection.cursor() 
    result = cursor.execute("SELECT * FROM library_system.employee WHERE (hourly_wages*work_hours) BETWEEN 500 AND 1000")
    if result > 0:
        view10 = cursor.fetchall()
    return render_template('/views/view10.html', view10 = view10)

    
if __name__ == '__main__':
    app.run(debug = True)
