import psycopg2
con = psycopg2.connect(
   database="bankmanagementsystem", user='postgres', password='123456', host='127.0.0.1', port= '5432'
)
cur = con.cursor()
