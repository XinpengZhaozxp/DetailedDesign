import sqlite3

coon = sqlite3.connect("E473.db")
c = coon.cursor()
c.execute("""
    DROP TABLE  RENUMBER
""")

coon.commit()
coon.close()