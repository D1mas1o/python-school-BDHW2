import sqlite3 as lite

data = None
query_string = '''
    select C.FirstName ||' '|| C.LastName,C.Phone,C.City
    from Invoice as I
    left join Customer as C on C.CustomerId = I.CustomerId where total > 0
    group by C.FirstName ||' '|| C.LastName
    having count(C.City)>1
    order by City
'''
try:
    con = lite.connect('Chinook_Sqlite.sqlite')
    cur = con.cursor()
    cur.execute(query_string)
    data = cur.fetchall()
    for item in data:
        print(item)
except Exception as e:
    print(e)
finally:
    if con is not None:
        con.close()