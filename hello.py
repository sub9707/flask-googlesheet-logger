import psycopg2

# DB 연결
connection = psycopg2.connect("host=192.168.0.1 dbname=postgres user=postgres password=1234 port=5432")

cur = connection.cursor()