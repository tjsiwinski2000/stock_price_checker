#  Day36 of 100 Days of Code™: The Complete Python Pro Bootcamp [UDEMY]
#
# Course Requirement was to compare opening and closing stock prices for 1day
# -- and alert if > %5 change
#
# Code below does it daily for 120 days.
#
# determine [% stock price change]
# output date, price, date2, price2, [pct change] [MSG if greater 5% change]
import os
import requests
from datetime import datetime, timedelta
STOCK_URL="https://www.alphavantage.co/query"

STOCK_API_KEY=os.environ.get('STOCK_API_KEY')


parameters = {
    "function" : "TIME_SERIES_DAILY",
    "symbol" : "TSLA",
    #"symbol" : "RXT",
    "apikey" : STOCK_API_KEY
}

response = requests.get(url=STOCK_URL, params=parameters)
response.raise_for_status()
data = response.json()
price_dict =data['Time Series (Daily)']
price_dict_len = len(price_dict)



format_string = "%Y-%m-%d"
loop_count=0

for date,date_info in price_dict.items():
    loop_count += 1
   
    current_close_price = date_info['4. close']
    
    datetime_object = datetime.strptime(date, format_string)
    date_object = datetime_object.date()
    
    previous_day_str= str(date_object - timedelta(days=1))
    if previous_day_str in price_dict:
        previous_close_price=price_dict[previous_day_str]['4. close']
    else:
        count = 1
        while previous_day_str not in price_dict and loop_count < price_dict_len:
            count +=1
            previous_day_str= str(date_object - timedelta(days=count))
        if loop_count < price_dict_len:
            previous_close_price=price_dict[previous_day_str]['4. close']  
        else:
            previous_close_price=0
    percentage_change = abs((float(current_close_price) - float(previous_close_price)) /float(current_close_price)) 
    percentage_change = round(percentage_change * 100,2)
    if percentage_change >= 5.0:
        blurb = "GREATER 5% CHANGE"
    else:
        blurb = ""
    print(f"{date} close price: {current_close_price} previous_date {previous_day_str} previous close:{previous_close_price} pct change:{percentage_change} {blurb}")
    #previous_close_price = 0
    
    
   





