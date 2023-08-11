FROM python:latest

# # Install dependencies
# RUN apt-get update && \
#  apt-get -y install python3

ADD main.py in_stock_notifier.py

# Install python3 dependencies
RUN pip3 install requests \
 && pip3 install BeautifulSoup4 \
 && pip3 install twilio \
 && pip3 install python-dotenv

EXPOSE 80

CMD [ "*/5 * * * *" "python3", "./in_stock_notifier.py" ]