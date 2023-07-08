from databases.postgresdb import PostgresDB

class Repositorio:
    
    def select(self, db_connection: any) -> None:
        connection = db_connection.conectar()
        print(f"Conectei ao banco {connection}")
        print(f"Fazendo um SELECT * FROM ...")
        db_connection.desconectar()
        
    def insert(self, db_connection: any) -> None:
        connection = db_connection.conectar()
        print(f"Conectei ao banco {connection}")
        print(f"Fazendo um INSERT VALUES...")
        db_connection.desconectar()