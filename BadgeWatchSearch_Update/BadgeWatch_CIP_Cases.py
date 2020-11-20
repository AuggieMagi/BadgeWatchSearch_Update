import sqlite3
conn = sqlite3.connect("BadgeWatch_DB.db")
cur = conn.cursor()

num = 3

sql_Pol = """
CREATE TABLE PoliceCases(
    ID INT,
    cip_No VARCHAR(6),
    Category CHAR(50), 
    badge_ID VARCHAR(15),
    first_Name CHAR(25),
    Last_name CHAR(25),
    Classification CHAR(40), 
    Allegation CHAR(40), 
    Finding CHAR(40)
) """

cur.execute(sql_Pol)
print('Police Case table has been created.')

conn.commit()
conn.close()