from bs4 import BeautifulSoup
import requests

def euro_course():
    page = requests.get("https://www.cbr.ru/eng/currency_base/daily/")
    soup = BeautifulSoup(page.content,'html.parser')
    print(soup.find_all('title')[0].get_text())
    euro = (soup.find_all("tr")[12].get_text())
    current_euro = print(euro.split()[4])
    return current_euro

def gatchina_weather():
    page = requests.get("https://yandex.ru/pogoda/gatchina")
    soup = BeautifulSoup(page.content,'html.parser')
    title = (soup.find_all('title')[0].get_text())
    right_now_in = (soup.find_all("span",class_ = 'temp__value')[0])
    return str(title+'\n'+'сейчас'+right_now_in.get_text())

if __name__ == "__main__":
    gatchina_weather()
    euro_course()
