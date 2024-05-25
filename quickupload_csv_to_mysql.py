"""
SUPPOSE WE WILL UPLOAD ALL DATA FROM markspb2.csv TO scorespb TABLE
"""

import os
os.chdir("PATHTOCSVFILE")
import mysql.connector
spcdatabase=mysql.connector.connect(
    user="root",
    host="localhost",
    password="YOURPASSWORD",
    database="DATABASENAME",
    allow_local_infile=True
    )
sql_command = """LOAD DATA LOCAL INFILE 'markspb2.csv' INTO TABLE scorespb FIELDS TERMINATED BY ',' IGNORE 1 LINES; """
spccur=spcdatabase.cursor()
spccur.execute(sql_command)
spcdatabase.commit()
