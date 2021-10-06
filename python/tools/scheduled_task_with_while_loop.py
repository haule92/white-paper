import sys
import time
import datetime as dt


def ___working___():
    index = None
    for index, char in enumerate("> > > W O R K I N G > > >"):
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(1.0 / 4)
    index += 1
    sys.stdout.write("\b" * index + " " * index + "\b" * index)
    sys.stdout.flush()


if __name__ == "__main__":

    # in this case this logic execute the desired script from Monday to Friday at 705am.

    selected_hour = 7
    selected_minute = 5
    sent = False

    while True:
        ___working___()
        current_time = dt.datetime.today()
        if (current_time.hour == selected_hour) & (current_time.minute == selected_minute) & (current_time.weekday() in [0, 1, 2, 3, 4]) & (sent is False):

            print('------------------------------ GENERATING CFD TRADE RECAP -------------------------------------')
            print(current_time)
            # CODE TO EXECUTE AT A CERTAIN TIME HERE !
            print('-----------------------------------------------------------------------------------------------')
            print('')
            sent = True

        elif (current_time.hour == (selected_hour + 1)) & (sent is True):
            sent = False

        else:
            pass
