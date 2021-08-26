import pandas as pd
from sqlalchemy_connector import SQLalchemyConn


class NameOfDatabase(SQLalchemyConn):

    def __init__(self):
        super().__init__()

    def read_from_sql(self, table_name):
        query = f"""
                SELECT * FROM {table_name}
        """
        return pd.read_sql(sql=query, con=self.setting_connection())

    def write_to_sql(self, df, table_name):
        return df.to_sql(name=table_name, con=self.setting_connection(), if_exists='replace')
