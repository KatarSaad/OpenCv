from requests import get
from pprint import  PrettyPrinter

BASE_URL="https://free.currconv.com/"
API=" 9d40bae82984efdc1356"

printer=PrettyPrinter()

def get_currencies():
    endpoint = f"api/v7/currencies?apiKey={API}"
    url=BASE_URL+endpoint
    data=get(url).json()
    printer.pprint(data)
get_currencies()
