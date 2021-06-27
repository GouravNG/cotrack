import requests  # for the url request


def data_fetcher(pincode, date):
    url = f'https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByPin?pincode={pincode}&date={date}'
    print(url)  # remove this
    data = requests.get(url)
    print(data)


pincode = 574201
date = '27-06-21'
data_fetcher(pincode, date)
