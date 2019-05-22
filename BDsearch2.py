import sqlite3 as lite

data = None
query_string = '''
    select C.City, sum(I.Total)
    from Invoice as I
    left join Customer as C on C.CustomerId = I.CustomerId where I.total > 0
    group by C.City
    order by sum(I.Total) desc
    limit 3
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