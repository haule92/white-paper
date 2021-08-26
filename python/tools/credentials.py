import configparser
from pathlib import Path


class Credentials:
    """
    Credentials class to read the credentials for different of accounts, emails, apis or databases
    This information is usually stored locally and gitignored in the repo under the name 'config.ini'
    """
    # the parents of the ROOT DIR depend on the class Credentials is defined.
    ROOT_DIR = Path(__file__).parents[1]
    # the same for the .joinpath(), depending on where the 'config.ini' is placed.
    CONFIG_FILENAME = ROOT_DIR.joinpath('configs', 'config.ini')

    def __init__(self):
        self.config = configparser.ConfigParser()
        self.config.read(self.CONFIG_FILENAME)

    def credentials_database_something(self):
        definition = 'DATABASE_SOMETHING_CREDENTIALS'
        credential_dict = {
            'user': self.config[definition]['username'],
            'password': self.config[definition]['password'],
            'host': self.config[definition]['hostname'],
            'port': self.config[definition]['port'],
            'db': self.config[definition]['database']
        }
        setattr(self, definition, credential_dict)

    def credentials_email_something2(self):
        definition = 'EMAIL_SOMETHING2_CREDENTIALS'
        credential_dict = {
            'email': self.config[definition]['email'],
            'password': self.config[definition]['password'],
        }
        setattr(self, definition, credential_dict)

    def credentials_api_something3(self):
        definition = 'API_SOMETHING3_CREDENTIALS'
        credential_dict = {
            'email': self.config[definition]['email'],
            'api_key': self.config[definition]['api_key'],
        }
        setattr(self, definition, credential_dict)
