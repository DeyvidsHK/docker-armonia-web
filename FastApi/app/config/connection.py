from sqlalchemy import create_engine, MetaData
from sqlalchemy.exc import SQLAlchemyError


metadata = MetaData()

class DBConnectionResult:
    def __init__(self, success, connection=None, metadata=None, error_message=None):
        self.success = success
        self.connection = connection
        self.metadata = metadata
        self.error_message = error_message

def create_db_connection():
    USER = "root"
    PASSWORD = "test"
    HOST = "db"
    PORT = "3306"
    DATABASE = "armonia"

    URL_DATABASE = f"mysql+mysqlconnector://{USER}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}"

    try:
        engine = create_engine(URL_DATABASE)
        conn = engine.connect()

        return DBConnectionResult(success=True, connection=conn)

    except SQLAlchemyError as e:
        # Manejar el error aquí
        error_message = f"Error al conectarse a la base de datos: {str(e)}"
        print(error_message)
        return DBConnectionResult(success=False, error_message=error_message)
