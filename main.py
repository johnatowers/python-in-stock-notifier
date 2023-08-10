from pip._vendor import requests
from bs4 import BeautifulSoup
from twilio.rest import Client



account_sid = "<twilio account id>"
auth_token = "<twilio account token>"
client = Client(account_sid, auth_token)

headers = {
    "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"
}

url = "<url of website you want to check stock on>"
page = requests.get(url, headers=headers)

soup = BeautifulSoup(page.content, 'html.parser')

# expression on parsed to find the buy button, this will differ on every webpage
parsed = soup.find('span', attrs={"data-default-text": True}).text
inStock = parsed.strip()

print(inStock)

# Simple expression checking if the button from stock != Sold out
if inStock != "Sold Out":
    message = client.messages.create(
        body="<message i.e Your item is back in stock.>",
        from_="<your twilio number>",
        to="<your phone number>"
    )
else:
    exit(0)