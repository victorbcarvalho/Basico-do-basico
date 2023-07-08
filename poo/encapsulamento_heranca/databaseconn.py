class DatabaseConn:
    
    def __init__(self) -> None:
        self.__database = "Postgres"
        self._conn = "//connection_string"
        self.user = "Victor"
    
    def __get_database(self) -> str:
        return self.__database
    
    def _testing_connection(self) -> None:
        print(f"Connection {self.__get_database()} Ok!")

class Repository(DatabaseConn):
    
    def __init__(self) -> None:
        super().__init__()
    
    def teste_connection(self):
        self._testing_connection()

db = DatabaseConn()
print(db.user)

repo = Repository()
repo.teste_connection()