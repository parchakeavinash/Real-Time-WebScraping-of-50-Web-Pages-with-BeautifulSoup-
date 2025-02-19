from bs4 import BeautifulSoup
import requests
import pandas as pd

data = []
current_page = 1
proceed = True

while(proceed):
    print("Scraping Current page is "+str(current_page))

    url = "https://books.toscrape.com/catalogue/page-"+str(current_page)+".html"

    page = requests.get(url)

    soap = BeautifulSoup(page.text, 'html.parser')
    
    if soap.title.text == "404 Not Found":
        proceed = False
    else:
        all_books = soap.find_all('li', class_="col-xs-6 col-sm-4 col-md-3 col-lg-3")
        
        for book in all_books:
            item = {}

            item['Title'] = book.find("img").attrs['alt']

            item['Link'] = book.find('a').attrs['href']

            item['Price'] = book.find('p',class_= "price_color").text[2:]

            item['Stock'] = book.find('p', class_="instock availability").text.strip()
            
            data.append(item)

    current_page +=1
        
df = pd.DataFrame(data)
df.to_csv("books.csv")
df.to_excel("books.xlsx")






