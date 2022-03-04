from get_info import GetInfo
from datetime import datetime
import time


class CheckInfoWebsite:

    def __init__(self):
        self.var = 0
        self.www = "https://sklep.pgg.pl"
        now = datetime.now()

    def run_check(self):
        while True:
            time.sleep(1)

            now = datetime.now()
            current_time = now.strftime("%H:%M:%S")

            get_info = GetInfo(self.www)

            if get_info.check_connection():
                if get_info.get_status():
                    print("The product is available")
                    print("Current Time =", current_time)
            else:
                print("Connection lost", current_time)


if __name__ == '__main__':
    check = CheckInfoWebsite()
    check.run_check()
