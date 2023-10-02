from bs4 import BeautifulSoup
import requests
import csv

page_to_scrap = requests.get("https://quotes.toscrape.com/")
soup = BeautifulSoup(page_to_scrap.text, "html.parser")

quotes = soup.find_all("span", attrs={"class": "text"})
authors = soup.find_all("small", attrs={"class": "author"})

file = open("scapped_quotes.csv", "w")
writer = csv.writer(file)

writer.writerow(["QUOTES", "AUTHOR"])

for quote, author in zip(quotes, authors):
    print(quote.text + " " + author.text)
    writer.writerow([quote.text, author.text])
file.close()
