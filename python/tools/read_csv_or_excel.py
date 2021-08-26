import os
import re
import pandas as pd


class ReadGenericFileCSVEXCEL:
    """
    Te purpose of this class is to read generic CSV or EXCEL files, which you don't need to state the exactly name of
    the file, only the directory where is saved the file.
    """

    def __init__(self, **kwargs):
        """
        Mailer class to send and download attachments.

        - relative_path (str): MANDATORY argument, write the path where is stored the file, usually the absolut.

        - encoding_file (str): OPTIONAL argument, depends on if required for the file.

        - delimiter_file (str): OPTIONAL argument, depends on if required for the file.

        - sheet_name_file (str): OPTIONAL argument, this is used only for the excel format types.
        """

        for k, v in kwargs.items():
            if re.search('^relative_path$', k):
                self.relative_path = v
            elif re.search('^encoding_file$', k):
                self.encoding_file = v
            elif re.search('^delimiter_file$', k):
                self.delimiter_file = v
            elif re.search('^sheet_name_file$', k):
                self.sheet_name_file = v
            else:
                raise ValueError('kwargs not found')

    def csv(self):
        """
        Method to read csv files taking care if they have encodings or delimiters added before read it.
        :return: pd.DataFrame()
        """
        os.chdir(self.relative_path)
        directory = os.listdir(self.relative_path)
        if len(directory) == 0:
            print('Directory is empty')
            return pd.DataFrame()
        else:
            for file in directory:
                if hasattr(self, 'encoding_file') and hasattr(self, 'delimiter_file'):
                    return pd.read_csv(filepath_or_buffer=file,
                                       encoding=self.encoding_file,
                                       delimiter=self.delimiter_file)
                elif hasattr(self, 'encoding_file') and not hasattr(self, 'delimiter'):
                    return pd.read_csv(filepath_or_buffer=file, encoding=self.encoding_file)
                elif not hasattr(self, 'encoding_file') and hasattr(self, 'delimiter'):
                    return pd.read_csv(filepath_or_buffer=file, delimiter=self.delimiter_file)
                else:
                    return pd.read_csv(filepath_or_buffer=file)

    def excel(self):
        """
        Method to read excel files with or without sheet_name_file.
        :return: pd.DataFrame()
        """
        os.chdir(self.relative_path)
        directory = os.listdir(self.relative_path)
        if len(directory) == 0:
            print('Directory is empty')
            return pd.DataFrame()
        else:
            for file in directory:
                if hasattr(self, 'sheet_name_file'):
                    return pd.read_excel(io=file, sheet_name=self.sheet_name_file, engine='openpyxl')
                else:
                    return pd.read_excel(io=file)