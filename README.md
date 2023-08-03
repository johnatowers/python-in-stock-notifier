# Python Out of Stock Notifier
This is a simple little python script to send a text message when an item you are looking for comes back into stock.

## Dependencies

### Beautiful Soup 4
Install with `pip install bs4`

### Twilio
Install with `pip install twilio`

You will need an account ID and token to make a call their api with your own account. You can sign up [here](https://www.twilio.com/en-us).

## Usage
This script is designed to be run on a cron job as often as you want. In my case I did every 5min.

There are a few variables that will need to be changed to fit your situation. You can find them in the main.py wrapped in <>

When it comes to selecting the element you are checking please refer to their documentation [here](https://www.crummy.com/software/BeautifulSoup/bs4/doc/). The expression will differ on every site.
