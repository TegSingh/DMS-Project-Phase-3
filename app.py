from flask import Flask, json, render_template, request, redirect
from flaskext.mysql import MySQL
import yaml

app = Flask(__name__)

db = yaml.load(open('dbconfig.yaml'))
app.config['MYSQL_DATABASE_HOST'] = db['mysql_host']
app.config['MYSQL_DATABASE_USER'] = db['mysql_user']
app.config['MYSQL_DATABASE_PASSWORD'] = db['mysql_password']
app.config['MYSQL_DATABASE_DB'] = db['mysql_db']
mysql = MySQL(app)

@app.route('/', methods = ['GET', 'POST'])
def index():
    if request.method == 'POST':
        userDetails = request.form
        name = userDetails['name']
        id = userDetails['ID']
        connection = mysql.connect()
        cursor = connection.cursor()
        cursor.execute("INSERT INTO student(name, ID) VALUES (%s, %s)", (name, id))
        connection.commit()
        cursor.close()
        return redirect('/users')
    return render_template('index.html')

# @app.route('/users')
# def userDetails():
#     connection = mysql.connect()
#     cursor = connection.cursor()
#     result = cursor.execute("SELECT * FROM student")
#     if result > 0: 
#         userDetails = cursor.fetchall()
#         return render_template('users.html', userValues = userDetails)
#     cursor.close()
    
@app.route('/library_branch')
def branchDetails():
    connection = mysql.connect()
    cursor = connection.cursor()
    result = cursor.execute("SELECT * FROM library_branch")
    if result > 0: 
        branchDetails = cursor.fetchall()
        return render_template('library_branch.html', branchDetails = branchDetails)
    cursor.close()

@app.route('/books')
def bookDetails():
    connection = mysql.connect()
    cursor = connection.cursor()
    result = cursor.execute("SELECT * FROM books")
    if result > 0: 
        bookDetails = cursor.fetchall()
        return render_template('books.html', bookDetails = bookDetails)
    cursor.close()

@app.route('/employee')
def employeeDetails():
    connection = mysql.connect()
    cursor = connection.cursor()
    result = cursor.execute("SELECT * FROM employee")
    if result > 0: 
        employeeDetails = cursor.fetchall()
        return render_template('employee.html', employeeDetails = employeeDetails)
    cursor.close()

@app.route('/borrower')
def borrowerDetails():
    connection = mysql.connect()
    cursor = connection.cursor()
    result = cursor.execute("SELECT * FROM borrower")
    if result > 0: 
        borrowerDetails = cursor.fetchall()
        return render_template('borrower.html', borrowerDetails = borrowerDetails)
    cursor.close()
        
if __name__ == '__main__':
    app.run(debug = True)
