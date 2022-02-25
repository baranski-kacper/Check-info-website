from urllib.request import urlopen


class GetInfo:

    def __init__(self, www):
        self.html_dic = None
        self.html = None
        self.html_bytes = None
        self.page = None
        self.url = www

    def check_connection(self):
        try:
            self.page = urlopen(self.url)
            self.html_bytes = self.page.read()
            self.html = self.html_bytes.decode("utf-8")
            self.html_dic = self.html.split()
            return True
        except:
            return False

    def get_status(self):
        for var, var2 in enumerate(self.html_dic):
             if 'czy_dostepny&quot;:true' in var2:
                return True
        # for var, var2 in enumerate(self.html_dic):
        #     if var2 == ':akcyza_insert':
        #         # print(var, var2, self.html_dic[var + 2])
        #         if self.html_dic[var + 2] != '"0"':
        #             return True
        #     if var2 == ':pojedynczy_produkt':
        #         # print(var, var2, self.html_dic[var + 2])
        #         if self.html_dic[var + 2] != '"0"':
        #             return True
        #     if var2 == ':sprzedaz_akcyza':
        #         # print(var, var2, self.html_dic[var + 2])
        #         if self.html_dic[var + 2] != '"0"':
        #             return True
        #     if var2 == ':sprzedaz_ppw':
        #         # print(var, var2, self.html_dic[var + 2])
        #         if self.html_dic[var + 2] != '"0"':
        #             return True


getinfo = GetInfo('https://sklep.pgg.pl')
getinfo.check_connection()
getinfo.get_status()
