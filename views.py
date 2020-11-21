# from flaskext.mysql import MySQL

# class views:
#     def get_view1(self, team_id):
#         # SELECT borrower.name as borrower_name, borrower.ID, library_branch.branchID, books.author_name
#         # FROM library_system.books
#         # INNER JOIN library_system.library_branch ON books.BranchID = library_branch.branchID
#         # INNER JOIN library_system.borrower ON books.borrowerID = borrower.ID
#     def get_view2(self, team_id):
#         # SELECT ALL avg(employee.hourly_wages), employee.branchID
#         # FROM library_system.employee
#         # WHERE hourly_wages > 16
#         # GROUP BY employee.branchID
#     def get_view3(self, team_id):
#         # SELECT * FROM library_system.employee
#         # WHERE hourly_wages > (SELECT AVG(employee.hourly_wages) 
#         # FROM library_system.employee
#         # WHERE employee.title = 'Manager');
#     def get_view4(self, team_id):
#         # SELECT books.title, borrower.name FROM library_system.books
#         # LEFT JOIN library_system.borrower ON books.ISBNnumber = borrower.borrower_book_ISBN 
#         # UNION 
#         # SELECT books.title, borrower.name FROM library_system.books 
#         # RIGHT JOIN library_system.borrower ON books.ISBNnumber = borrower.borrower_book_ISBN 
#     def get_view5(self, team_id):
#         # SELECT * FROM LIBRARY_BRANCH WHERE capacity > 300
#         # UNION
#         # SELECT * FROM LIBRARY_BRANCH WHERE employees_total > 20
#     def get_view6(self, team_id):
#         # SELECT employee.name, employee.ID, (employee.hourly_wages*employee.work_hours) AS Salary
#         # FROM library_system.employee
#         # WHERE employee.hourly_wages*employee.work_hours = 
#         # (SELECT MIN(employee.hourly_wages*employee.work_hours) FROM library_system.employee) OR 
#         # employee.hourly_wages*employee.work_hours = 
#         # (SELECT MAX(employee.hourly_wages*employee.work_hours) FROM library_system.employee);  
#     def get_view7(self, team_id):
#         # SELECT books.author_name, COUNT(DISTINCT books.ISBNnumber)
#         # FROM library_system.books 
#         # GROUP BY books.author_name;
#     def get_view8(self, team_id):
#         # SELECT employee.name, employee.ID, (employee.hourly_wages*employee.work_hours) AS Salary  
#         # FROM library_system.employee
#         # ORDER BY employee.hourly_wages*employee.work_hours;
#     def get_view9(self, team_id):
#         # SELECT COUNT(DISTINCT borrower_book_ISBN) AS Books_borrowed_in_November
#         # FROM library_system.borrower
#         # WHERE date_borrowed LIKE '%11%';
#     def get_view10(self, team_id):
#         # SELECT * FROM library_system.employee 
#         # WHERE (hourly_wages*work_hours) BETWEEN 500 AND 1000;

        