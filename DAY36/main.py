import requests
from math import fabs

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
API_KEY_STOCK_ENDPOINT = '6PBA3V4DTQQGW9UC'
API_KEY_NEWS_ENDPOINT = 'c693312239ce4f2e8a4bed19a2cb68be'
TWILIO_SID = 'AC3e38fc8efcfd2736707615630aa5509a'
TWILIO_AUTH_TOKEN = '21b05d1b27c6993e81a1b1acbff95adf'
## STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

# TODO 1. - Get yesterday's closing stock price. Hint: You can perform list comprehensions on Python dictionaries. e.g. [new_value for (key, value) in dictionary.items()]
stock_param = {
    'function': 'TIME_SERIES_DAILY',
    'symbol': STOCK_NAME,
    'apikey': API_KEY_NEWS_ENDPOINT
}
response = requests.get(STOCK_ENDPOINT, params=stock_param)
print(response.json())
data = response.json()['Time Series (Daily)']
data_list = [value for (key, value) in data.items()]
yesterday_closing_price = data_list[0]['4. close']

# TODO 2. - Get the day before yesterday's closing stock price
before_yesterday_closing_price = data_list[1]['4. close']
# TODO 3. - Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20.
#  Hint: https://www.w3schools.com/python/ref_func_abs.asp
pos_difference = float(yesterday_closing_price) - float(before_yesterday_closing_price)
up_down = None
if pos_difference > 0:
    up_down = '🔺'
else:
    up_down = '🔻'
# TODO 4. - Work out the percentage difference in price between closing price yesterday and closing price the day
#  before yesterday.
percentage = (fabs(pos_difference) / float(yesterday_closing_price)) * 100
print(percentage)

# TODO 5. - If TODO4 percentage is greater than 5 then print("Get News").
if percentage > 1:
    print('get news')

## STEP 2: https://newsapi.org/
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.

# TODO 6. - Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME.
if percentage > 5:
    news_param = {
        'qInTitle': COMPANY_NAME,
        'apiKey': API_KEY_NEWS_ENDPOINT
    }
    response_news = requests.get(NEWS_ENDPOINT, params=news_param)
    data = response_news.json()['articles']
    print(data)
    # TODO 7. - Use Python slice operator to create a list that contains the first 3 articles. Hint: https://stackoverflow.com/questions/509211/understanding-slice-notation
    first_three_from_data = data[:3]
    print(first_three_from_data)
    ## STEP 3: Use twilio.com/docs/sms/quickstart/python
    # to send a separate message with each article's title and description to your phone number.

    # TODO 8. - Create a new list of the first 3 article's headline and description using list comprehension.
    fromatted_articles = [f'{STOCK_NAME}: {up_down}{pos_difference}%\nHeandline: {article["title"]}. \nBrief: {article["description"]}' for article in
                          first_three_from_data]
    from twilio.rest import Client

    client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)
    # TODO 9. - Send each article as a separate message via Twilio.
    for article in fromatted_articles:
        message = client.messages.create(
            body=article,
            from_='+18787688918',
            to='+213797873139'
        )
        print(message.status)
# Optional TODO: Format the message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""
