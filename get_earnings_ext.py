from bs4 import BeautifulSoup
import requests
import datetime


class GetEarnings:
    def __init__(self, ticker):
        self.lst_earnings_dt = []
        self.ticker = ticker

    def get_earnings(self):
        current = 0
        while True:
            url = f"https://finance.yahoo.com/calendar/earnings?symbol={self.ticker}&offset={current}&size=100"
            response = requests.get(url)
            try:
                response.raise_for_status()
            except:
                try:
                    response = requests.get(url)
                    response.raise_for_status()
                except:
                    return
            soup = BeautifulSoup(response.text, 'html.parser')

            earnings_date = soup.select(
                r'''div.Ovx\(a\).Ovx\(h\)--print.Ovy\(h\) > table > tbody > tr >
                td[aria-label="Earnings Date"]''')

            earnings_price = soup.select(
                r'''div.Ovx\(a\).Ovx\(h\)--print.Ovy\(h\) > table > tbody > tr >
                td[aria-label="Reported EPS"]''')

            if not len(earnings_date):
                return self.lst_earnings_dt
                break

            for date, price in zip(earnings_date, earnings_price):
                raw_date = date.getText()[:12]

                date_object = datetime.datetime.strptime(raw_date, "%b %d, %Y")
                string_date = datetime.date.strftime(date_object, "%Y-%m-%d")
                self.lst_earnings_dt.append(string_date)

            current += 100
