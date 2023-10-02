#things i used for this project: SQL, datetime and time modules and an IDE or python's IDLE
#table is to be created in mySql with the attributes of your choice:  for me it will be "Expenses" "Spent_on"  "Day" "Date".
#expenses is an integer value of upto five digits and spent_on, Day, Date are string value of upto thirty characters (depending)

import mysql.connector as sqlt;
from datetime import date;
import time;

hello=('monday','tuesday','wednesday','thursday','friday','saturday')

years=('2023', '2024', '2025', '2026', '2027', '2028', '2029', '2030', '2031', '2032', '2033', '2034', '2035', '2036', '2037', '2038', '2039', '2040', '2041', '2042', '2043', '2044', '2045', '2046', '2047', '2048', '2049', '2050', '2051', '2052', '2053', '2054', '2055', '2056', '2057', '2058', '2059', '2060', '2061', '2062', '2063', '2064', '2065', '2066', '2067', '2068', '2069', '2070', '2071', '2072', '2073', '2074', '2075', '2076', '2077', '2078', '2079', '2080', '2081', '2082', '2083', '2084', '2085', '2086', '2087', '2088', '2089', '2090', '2091', '2092', '2093', '2094', '2095', '2096', '2097', '2098', '2099', '2100', '2101', '2102', '2103', '2104', '2105', '2106', '2107', '2108', '2109', '2110', '2111', '2112', '2113', '2114', '2115', '2116', '2117', '2118', '2119', '2120', '2121', '2122', '2123')
#UPDATE THIS TUPLE EVERY 100 YEARS lol

def sqlConnect():#sends data to the sql object
    return sqlt.connect(host="",user="",passwd="",database="") #modify this according to your SQL

def checkInteger():#checks if the amount entered is integer or not
    while True:
        a=input("Enter Amount spend: ")
        if a.isdigit():
            a=int(a)
            break
        else:
            print("Enter a valid amount");print('\n')
    return a

def checkString():#checks for a valid day
    while True:
        a=input("Please Enter a valid day: ")
        if (a.isalpha()) and (a.lower() in hello):
            break
        else:
            print("Check your Spellings and/or the input values");print('\n')
    return a

def getDate():#sends a date in yyyy-dd-mm format to be entered in the relation
    a=date.today()
    return str(a)

def insert_into_table(ex,spentOn,day,date): #inserts data into the table
    z=sqlConnect()
    if z.is_connected():
        try:
            insertCursor=z.cursor()
            query="insert into daily_expenses values({},'{}','{}','{}')".format(ex,spentOn,day,date)
            insertCursor.execute(query)
            z.commit()
            print("insert success");print('\n')
        except EOFError:
            print(EOFError)
    else:
        print("Unable to connect");print('\n')
    return

"""
*****************only Applies to the function below***********************
these function are connected to checkMonth to get the correct values.
DO NOT RUN DIRECTLY UNLESS MONTH VARIABLE IS NOT 
CHANGED INTO A STRING MATCHING THE SAME AS IN THE TUPLE IN 
checkMonth() FUNCTION   
"""

def specifiedMonth(month):
    z=sqlConnect()
    if z.is_connected():
        cursorMonth=z.cursor()
        query="select * from daily_expenses where date like '_____{}%'".format(month)
        cursorMonth.execute(query)
        data=cursorMonth.fetchall()
        if data == []:
            print("No Records to show");print('\n')
        for row in data:
            print(row)
    j=input("Would You like to delete for the specified month? (Y/N): ");print('\n')
    if j.lower()=='y':
        delRecordsMonth(month)
    return

def delRecordsMonth(month):
    z=sqlConnect()
    print("NOTE: THIS WILL DELETE ALL THE RECORDS OF THE MONTH REGARDLESS OF THE YEAR, THIS IS NOT REVERSIBLE")
    if z.is_connected():
        j=input("Would You Like to delete records? (Y/N): ")
        if (j.isalpha() and j.lower()=='y'):
            cursorDel=z.cursor()
            query="delete from daily_expenses where date like '_____{}%'".format(month)
            cursorDel.execute(query)
            z.commit()
            print("Deletion success");print('\n')
        else:
            print("Deletion Cancelled");print('\n')
    return

def checkMonth():#checks for the month entered
    while True:
        a=input("Enter a Month in (mm) format: ")
        if a.isdigit() and a in ('01','02','03','04','05','06','07','08','09','10','11','12'):
            break
        else:
            print("Enter a valid Month")
    
    print("View Records For a Specified Month or Delete records for a specified month")
    k=input("Enter (REC) to view records or (DEL) to delete records: ");print('\n')
    if k.lower()=='rec':
        specifiedMonth(a)
    elif k.lower()=='del':
        delRecordsMonth(a)
    else:
        print("Cancelled");print('\n')
    return

"""END OF CONDITION"""

#saved for later (working function)
'''
def viewRecords():#used for viewing all the contents of the table 
    z=sqlConnect()
    if z.is_connected():
        print("initiating records to view...");time.sleep(3) #this is just for wait lol
        showCursor=z.cursor()
        query="select * from daily_expenses"
        showCursor.execute(query)
        g=showCursor.fetchall()
        for data in g:
            print(data)
    return
'''

"""
*******Applies to the functions below*******
all the functions below depends on the checkYear()
DO NOT MODIFY the functions' formal parameters
"""
def specifiedYear(year):
    z=sqlConnect()
    if z.is_connected():
        cursorYear=z.cursor()
        query="select * from daily_expenses where date like '{}%'".format(year)
        cursorYear.execute(query)
        data=cursorYear.fetchall()
        if data==[]:
            print("No records found");print('\n')
        for row in data:
            print(row)
    return

def delRecordsYear(year):
    z=sqlConnect()
    print("NOTE: THIS WILL DELETE ALL THE RECORDS OF THE YEAR PROVIDED, THIS IS NOT REVERSIBLE")
    j=input("Would You like to proceed? (Y/N): ")
    if (j.isalpha()  and j.lower()=='y'):  
        if z.is_connected():
            cursorDelYear=z.cursor()
            query="delete from daily_expenses where date like '{}%'".format(year)
            cursorDelYear.execute(query)
            z.commit()
            print("Deletion success");print('\n')
    else:
        print("Deletion Cancelled");print('\n')
    return

def checkYear():
    while True:
        j=input("Enter a Year to search the records of (2023-2123): ")
        if j.isdigit() and j in years:
            break
        else:
            print("Enter a valid year")
    
    print("View Records For a Specified Year or Delete records for a specified Year")
    k=input("Enter (REC) to view records or (DEL) to delete records: ")
    if k.lower()=='rec':
        specifiedYear(j)
    elif k.lower()=='del':
        delRecordsYear(j)
    return

"""End Of Condition"""

def delAccDate(date):
    z=sqlConnect()
    print("This will delete according to the date provided, THIS IS NOT REVERSIBLE")
    j=input("Would you like to proceed? (Y/N): ")
    if (j.isalpha and j.lower()=='y'):
        if z.is_connected():
            dateDelCursor=z.cursor()
            query="delete from daily_expenses where date like '{}%'".format(date)
            dateDelCursor.execute(query)
            z.commit()
            print("Deletion success");print('\n')
    else:
        print("Deletion Cancelled");print('\n')
    return

def check_int_validity():
    while True:
        j=input("Enter The Serial Number According to above: ")
        if j.isdigit():
            z=int(j)
            break
        else:
            print("Enter a Valid Number");print('\n')
    return z

def main():
    print('''
__________________________________________________________        
          What Would You like to do?      
          1. Insert Values Into The Database   
          2. View/Delete Records For a Particular Year
          3. View/Delete Records for Particular Month
          4. View/Delete Records According To Date
          5. Delete Entire Data From The Relation
__________________________________________________________          
          ''')
    
# if __name__=='__main__':
#     main()
