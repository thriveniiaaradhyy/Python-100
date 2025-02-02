import sqlite3
import pandas

conn = sqlite3.connect("database\database.db")
cur = conn.cursor()
cur.execute("SELECT country FROM countries WHERE area >= 2000000")
rows = cur.fetchall()
conn.close()

df = pandas.DataFrame.from_records(rows)
df.columns = ["Rank", "Country", "Area", "Population"]
df.to_csv("countries_big_area.csv", index = False)
