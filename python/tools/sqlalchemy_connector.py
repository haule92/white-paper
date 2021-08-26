from sqlalchemy import create_engine
from credentials import Credentials


class SQLalchemyConn(Credentials):

    def __init__(self):
        Credentials.__init__(self)
        self.credentials_database_something()

    def setting_connection(self):
        driver = "mysql+pymysql:"
        conn = \
            f"{driver}//" \
            f"{getattr(self, 'SERVER_DATABASE_CREDENTIALS')['user']}:" \
            f"{getattr(self, 'SERVER_DATABASE_CREDENTIALS')['password']}@" \
            f"{getattr(self, 'SERVER_DATABASE_CREDENTIALS')['host']}/" \
            f"{getattr(self, 'SERVER_DATABASE_CREDENTIALS')['db']}"
        return create_engine(conn)
