from get_info import GetInfo
import time


class CheckInfoWebsite:

    def __init__(self):
        self.var = 0
        self.www = "https://sklep.pgg.pl"

    def run_check(self):
        while True:
            time.sleep(10)
            get_info = GetInfo(self.www)

            if get_info.check_connection():
                if get_info.get_status():
                    print("The product is available")
            else:
                print("Connection lost")
            self.var += 1
            print(self.var)


if __name__ == '__main__':
    check = CheckInfoWebsite()
    check.run_check()
