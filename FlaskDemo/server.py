import pyodbc

cnxn = pyodbc.connect('Driver={SQL Server};Server=.\Mayank;Database=Payroll;')
cursor = cnxn.cursor()
cursor.execute("SELECT Name FROM dbo.Employees_details")
while 1:
    row = cursor.fetchone()
 
    if not row:
        break
 
    print(row.Name)



cursor.execute("SELECT * from dbo.Employees_details")
for row in cursor:
 print('row =%r' %(row,))
 
cursor.execute("UPDATE CommaDelimeter SET Name = 'Mayank' WHERE NAME = 'Michel'")
cnxn.commit() 
 
cnxn.close()