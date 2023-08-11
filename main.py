import requests
import os
from bs4 import BeautifulSoup
from twilio.rest import Client
from dotenv import load_dotenv

load_dotenv()

account_sid = os.getenv('TWILIO_ACCOUNT_SID')
auth_token = os.getenv('TWILIO_AUTH_TOKEN')
client = Client(account_sid, auth_token)

url = "https://www.lego.com/en-us/product/lego-star-wars-darth-vader-keyring-850996"
page = requests.get(url)

soup = BeautifulSoup(page.content, 'html.parser')

# expression on parsed to find the buy button, this will differ on every webpage
parsed = soup.find('p', attrs={"class": "Text__BaseText-sc-13i1y3k-0 bAqfGh ProductOverviewstyles__AvailabilityStatus-sc-1a1az6h-11 jRMAfF"}).text
inStock = parsed.strip()

print(inStock)

# Simple expression checking if the button from stock != Sold out
if inStock != "Sold out":
    message = client.messages.create(
        body="The LEGO® Star Wars™ Darth Vader™ Key Chain is back in stock",
        from_= os.getenv('TWILIO_PHONE_NUMBER'),
        to= os.getenv('YOUR_PHONE_NUMBER')
    )
else:
    print("The LEGO® Star Wars™ Darth Vader™ Key Chain is out of stock"),
    exit(0)
