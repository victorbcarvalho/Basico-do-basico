from repositorio import Repositorio
from databases import PostgresDB
from databases import MysqlDB

db_conn = PostgresDB()
repo = Repositorio()

repo.insert(db_conn)
repo.select(db_conn)

db_conn_mysql = MysqlDB()
repo.insert(db_conn_mysql)
repo.select(db_conn_mysql)