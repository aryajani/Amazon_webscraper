import requests
import subprocess
from bs4 import BeautifulSoup
from time import sleep

# This function collects prices from amazon about a few products and puts it in the form of a 
# csv file.
def plaid(URL):

    File = open("results.csv", "a")
    
    HEADERS = ({'User-Agent':
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',
                            'Accept-Language': 'en-US, en;q=0.5'})
    
    webpage = requests.get(URL, headers=HEADERS)
    soup = BeautifulSoup(webpage.content, "lxml")

    # find product title
    try:
            title = soup.find("span",
                            attrs={"id": 'productTitle'})
            title_value = title.string

            title_string = title_value.strip().replace(',', '')
                    
    except AttributeError:

            title_string = "NA"

            print("product Title = ", title_string)


    File.write(f"{title_string},")

    try:
        price = soup.find("span", attrs={"id": "priceblock_ourprice"}).string.strip().replace(",", "")

    except AttributeError:
        price = "NA"

    File.write(f"{price},\n")
    

    File.close()


def openFile(filename):
    
    subprocess.call(['open', filename])


if __name__ == '__main__':
  # openning our url file to access URLs
    file = open("URLs.txt", "r")
    open("results.csv", "w")

  
    # iterating over the urls
    for links in file.readlines():
        plaid(links)
    openFile("/Users/checkoutuser/Desktop/amazonwebscraper/results.csv")
        
