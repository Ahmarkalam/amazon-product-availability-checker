import time
from time import sleep
from lxml import html
import requests
import schedule
import smtplib
import random



def check (url):
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.90 Safari/537.36'}
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        doc = html.fromstring(response.content)
        availability = doc.xpath('//*[@id="availability"]/span/text()')
        return ''.join(availability).strip()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching the URL: {e}")
        return None
    
def monitor_product ():
    asin = "B0DGJJM5HZ"
    url = f"https://www.amazon.in/dp/{asin}"

    print(f"Checking availability for{url}")

    availability = check(url)

    if availability:
        print(f"status: {availability}")
        if 'In Stock' in availability or 'Available' in availability:
            print("product is available")
    else:
        print("Could not retrieve product availability.")
schedule.every(1).minutes.do(monitor_product)

while True:
    schedule.run_pending()
    sleep(random.uniform(5, 10))
   



    



                                        
    