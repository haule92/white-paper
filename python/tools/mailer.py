import re
import os
import email
import random
import smtplib
import imaplib
import pandas as pd
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication

from credentials import Credentials


class Mailer(Credentials):

    def __init__(self, account):
        """
        Mailer class to send and download attachments.

        - account (str): Email account selected to use the Mailer class. The credentials for this mail have to be
                        defined previously in the Credentials class. If not the code will raise and exception.
        """

        Credentials.__init__(self)

        self.subject = ""
        self.message = ""
        self.direct_recepients = [None]
        self.indirect_recepients = [None]
        self.attachment = None
        self.attachment_header = None

        self.outlook_folder = 'INBOX'
        self.directory = None
        self.file_extension = 'csv'
        self.subject_pattern = None
        self.date_selected = None

        # something2@outlook.com
        if re.search('something2', account, re.I):
            self.credentials_email_something2()
            self._email_account = getattr(self, 'EMAIL_SOMETHING2_CREDENTIALS')['email']
            self._password_account = getattr(self, 'EMAIL_SOMETHING2_CREDENTIALS')['password']

        # this elif as an example mode if we have more than one mail to run automatically
        # something4@outlook.com
        # elif re.search('something4', account, re.I):
        #     self.credentials_email_something4()
        #     self._email_account = getattr(self, 'EMAIL_SOMETHING4_CREDENTIALS')['email']
        #     self._password_account = getattr(self, 'EMAIL_SOMETHING4_CREDENTIALS')['password']

        else:
            raise Exception('Credentials for this sender not found!')

    def add_subject_text(self, subject):
        """
        Adding subject for the email
            - subject (str)
        """
        self.subject += subject

    def add_message_text(self, message):
        """
        Adding text the email
            - message (str)
        """
        self.message += message

    def send_message(self, **kwargs):
        """
        Method to send the message, here have to include the kwargs:

        Kwargs:
            - direct_recipient (list): MANDATORY argument, write the emails where to send the message.

            - indirect_recipient (list): OPTIONAL argument, write the emails where to send the message.

            - attachment (str): OPTIONAL argument, path where is located the file we want to attach.

            - content_header (str): OPTIONAL argument, title of the attached file.
        """

        for kwarg, arg in kwargs.items():

            if re.search('.*(^direct).*(recipient|receiver)', kwarg, re.I):
                self.direct_recepients = arg
                if not isinstance(self.direct_recepients, list):
                    self.direct_recepients = [self.direct_recepients]

            elif re.search('.*(cc|indirect|forward).*(recipient|receiver)', kwarg, re.I):
                self.indirect_recepients = arg
                if not isinstance(self.indirect_recepients, list):
                    self.indirect_recepients = [self.indirect_recepients]

            elif re.search('^content$|^attachment$', kwarg, re.I):
                self.attachment = arg

            elif re.search('.*(content|attachment ).*(header)', kwarg, re.I):
                self.attachment_header = arg

            else:
                pass

        multipart = MIMEMultipart()
        multipart['Subject'] = self.subject
        multipart['To'] = ",".join(self.direct_recepients)
        if self.indirect_recepients[0] is not None:
            multipart['Cc'] = ",".join(self.indirect_recepients)
        else:
            pass
        multipart.attach(MIMEText(self.message, 'plain'))
        if self.attachment is None:
            pass
        else:
            file = MIMEApplication(open(self.attachment, 'rb').read())
            if getattr(self, '_attachment_header', None) is not None:
                file.add_header("Content-Disposition", f"attachment; filename={self.attachment_header}")
            else:
                file.add_header("Content-Disposition", f"attachment; filename={self.attachment}")
            multipart.attach(file)
        mail_server = smtplib.SMTP('smtp.office365.com', '587')
        text = multipart.as_string()
        try:
            mail_server.ehlo()
            mail_server.starttls()
            mail_server.login(self._email_account, self._password_account)
            if self.indirect_recepients[0] is not None:
                mail_server.sendmail(self._email_account, self.direct_recepients + self.indirect_recepients, text)
            else:
                mail_server.sendmail(self._email_account, self.direct_recepients, text)

        except Exception as e:
            print(e)
        finally:
            mail_server.quit()

    @staticmethod
    def create_dir(directory):
        """
        Method to create the specified directory if it does not exist already.
        After that is up to you if you want to delete the directory or not.

            - directory (str)
        """

        if not os.path.exists(str(directory)):
            return os.makedirs(directory)
        else:
            pass

    @staticmethod
    def check_msg_subject_same_subject_pattern(folder, msg, subject_pattern):
        """
        Although the mail is inside the folder this if statement serve the purpose to double check the subject
        is the one we want, to avoid cases where a mail is found in the folder without correct subject.
        To add an if statement for each folder in the selected email.

            - folder (str): exactly the same name in the Fasanara Quant Email Outlook

            - msg: Each of the message in the iteration, this variable is coming from inside the code not user input.

            - subject_pattern (str): the same subject that the emails use
        """

        # example1
        if re.search(r'^FOLDER_ONE$', folder):
            if not re.search(rf'{subject_pattern}', msg['Subject']):
                raise ValueError('Subject pattern does not match with the subject of the mail!')
            else:
                pass

        # example2
        elif re.search(r'^FOLDER_TWO$', folder):
            if not re.search(rf'^{subject_pattern}$|^justanexample$', msg['Subject']):
                raise ValueError('Subject pattern does not match with the subject of the mail!')
            else:
                pass

        # example3
        elif re.search(r'^FOLDER_THREE$', folder):
            if not re.search(rf'{subject_pattern}', msg['Subject']):
                raise ValueError('Subject pattern does not match with the subject of the mail!')
            else:
                pass

        else:
            pass

    @staticmethod
    def generating_binary_format(directory, _file_name, part):
        """
        To save the downloaded attachments in the directory specified with the name of the file.
        Using binary file to saved, 'wb' states for write byte.

            - directory (str): Specific directory

            - _file_name (str): Name of the file to save with

            - part: Part of the mail, which is the attached file ending with the format specified.
                    This variable is coming from inside the code not user input.
        """

        _file_path = os.path.join(str(directory), _file_name)
        fp = open(_file_path, 'wb')
        fp.write(part.get_payload(decode=True))
        fp.close()

    def saving_attachment(self, folder, directory, _file_name, part):
        """
        In every if statement we can alter the file, name or filter for files of same name.
        Alterations needed for each folder before saving the file in the directory.

            - folder (str): exactly the same name in the Fasanara Quant Email Outlook

            - directory (os.path): Specific directory

            - _file_name (str): Name of the file to save with

            - part: Part of the mail, which is the attached file ending with the format specified
        """

        if re.search(r'^FOLDER_ONE$', folder):
            # save if the trade files match with the name stated below.
            # here can be added different filters or if statements
            if re.search(r'filewithspecificname', _file_name, re.I):
                self.generating_binary_format(directory=directory, _file_name=_file_name, part=part)

        elif re.search(r'^FOLDER_TWO$', folder):
            self.generating_binary_format(directory=directory, _file_name=_file_name, part=part)

        elif re.search(r'^FOLDER_THREE$', folder):
            # in this case this is happening because the file names are always the same, so a random int is added
            # at the end of the file to make it unique. This is not robust enough because there is the small prob
            # that if the random number is repeated then the file would be not saved because will exists one file
            # with exactly the same name.
            _file_name = _file_name[:-4] + str(random.randint(1, 999_999_999_999)) + _file_name[-4:]
            self.generating_binary_format(directory=directory, _file_name=_file_name, part=part)

        elif re.search(r'^FOLDER_FOUR$', folder):
            self.generating_binary_format(directory=directory, _file_name=_file_name, part=part)

        elif re.search(r'^FOLDER_FIVE$', folder):
            self.generating_binary_format(directory=directory, _file_name=_file_name, part=part)

        else:
            raise Exception('nothing has been saved, consider to fill this case inside saving_attachment method')

    def download_attached_files_from_folder(self, **kwargs):
        """
        Method to download the attachments files from the folder selected in the Outlook account. Previously the folder
        has to be created in the Outlook Email, here have to include the kwargs:

        Kwargs:
            - outlook_folder (str): MANDATORY argument, name of the folder which we want to download the attachments.

            - directory (str): MANDATORY argument, path where we want to save the downladed files after that is up to us
                                if we want to remove the path using "shutil.rmtree(directory)". The code takes care to
                                create the directory if it does not exist.

            - file_extension (str): MANDATORY argument, here we write whatever is the extension of the file or files we
                                want to download. For instance: "csv" "xlsx" "pdf"

            - subject_pattern (str): OPTIONAL argument, if we want to include the subject pattern to make sure that the
                                email is in the folder and have the same subject pattern we want. Recommend to add it.

            - date_selected (dt.date): OPTIONAL argument, if we want to download attached files from specific date we
                                add this argument. For example for today would be "dt.date.today()". Otherwise if we do
                                not add this argument the code will download all the attached files without considering
                                the dates.


        """

        for kwarg, arg in kwargs.items():

            if re.search(r'^outlook_folder$', kwarg, re.I):
                self.outlook_folder = arg
            elif re.search(r'^directory$', kwarg, re.I):
                self.directory = arg
            elif re.search(r'^file_extension$', kwarg, re.I):
                self.file_extension = arg
            elif re.search(r'^subject_pattern$', kwarg, re.I):
                self.subject_pattern = arg
            elif re.search(r'^date_selected$', kwarg, re.I):
                self.date_selected = arg
            else:
                pass

        imap_server = imaplib.IMAP4_SSL(host='smtp.office365.com')
        imap_server.login(self._email_account, self._password_account)
        imap_server.select(self.outlook_folder)

        _, message_numbers_raw = imap_server.search(None, 'ALL')

        for message_number in message_numbers_raw[0].split():
            _, raw_msg_coded = imap_server.fetch(message_number, '(RFC822)')
            raw_msg_decoded_str = raw_msg_coded[0][1].decode('utf-8')
            msg = email.message_from_string(raw_msg_decoded_str)

            for part in msg.walk():
                if self.date_selected is not None:
                    message_sent_date = pd.to_datetime(msg['Date']).date()
                    if message_sent_date == self.date_selected:
                        self.check_msg_subject_same_subject_pattern(folder=self.outlook_folder,
                                                                    msg=msg,
                                                                    subject_pattern=self.subject_pattern)
                        # Get the name of the file attached
                        _file_name = part.get_filename()
                        # If _file_name exists proceed, otherwise jump to next iteration
                        if bool(_file_name):
                            if re.search(rf'\.{self.file_extension}', _file_name, re.I):
                                self.create_dir(self.directory)
                                self.saving_attachment(folder=self.outlook_folder,
                                                       directory=self.directory,
                                                       _file_name=_file_name,
                                                       part=part)
                else:
                    # Get the name of the file attached
                    _file_name = part.get_filename()
                    # If _file_name exists proceed, otherwise jump to next iteration
                    if bool(_file_name):
                        if re.search(rf'\.{self.file_extension}', _file_name, re.I):
                            self.create_dir(self.directory)
                            self.saving_attachment(folder=self.outlook_folder,
                                                   directory=self.directory,
                                                   _file_name=_file_name,
                                                   part=part)
