import psycopg2

db = psycopg2.connect(host='localhost', dbname='testdb',user='postgres',password='password',port=5432)

