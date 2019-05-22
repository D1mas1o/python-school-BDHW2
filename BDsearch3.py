
import sqlite3 as lite

data = None
query_string = '''
select G.Name as Genre,group_concat(T.Name) as Track,group_concat(A.Title) as Title,group_concat(Art.Name) as Artist, sum(IL.UnitPrice) as Price
from InvoiceLine as IL
left join Track as T on IL.TrackId = T.TrackId 
left join Genre as G on T.GenreId = G.GenreId
left join Album as A on T.AlbumId = A.AlbumId
left join Artist as Art on A.ArtistId = Art.ArtistId
where IL.UnitPrice not null
group by G.Name
order by sum(IL.UnitPrice) desc
limit 1
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