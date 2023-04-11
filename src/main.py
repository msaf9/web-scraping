# Web scraping

# Libraries
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as req

# URL - eCommerce website
url = "https://www.flipkart.com/search?q=ipad&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off"

client = req(url)
page = client.read()
client.close()
html = soup(page, "html.parser")

containers = html.findAll("div", {"class": "_1YokD2 _3Mn1Gg"})
# print(len(containers))

container = containers[0]
# print(container.div.img["alt"])

price = container.findAll("div", {"class": "col col-5-12 _2o7WAb"})
# print(price[0].text)

ratings = container.findAll("div", {"class": "niH0FQ"})
# print(ratings[0].text)

# Files
filename = "../resources/products.csv"
f = open(filename, "w")
headers = "Product_name,Price,Ratings\n"
f.write(headers)

for container in containers:
    product_name = container.div.img["alt"]

    price_container = container.findAll("div", {"class": "_1vC4OE _2rQ-NK"})
    price = price_container[0].text.strip()

    ratings_container = container.findAll("div", {"class": "hGSR34"})
    rating = ratings_container[0].text.strip()

    # print("product_name:" + product_name)
    # print("price:" + price)
    # print("Ratings:" + rating)

    # String parsing
    trim_price = ''.join(price.split(','))
    rm_rupee = trim_price.split("₹")
    add_rs_price = "Rs." + rm_rupee[1]
    split_price = add_rs_price.split('N')
    split_price = add_rs_price.split('E')
    split_price = add_rs_price.split('U')
    final_price = split_price[0]
    # print(final_price)

    split_rating = rating.split(" ")
    split_rating = rating.split(",")
    split_price = add_rs_price.split("1")
    final_rating = split_rating[0]

    print(product_name.replace(",", "|") + "," + final_price + "," + final_rating + "\n")
    f.write(product_name.replace(",", "|") + "," + final_price + "," + final_rating + "\n")

f.close()
