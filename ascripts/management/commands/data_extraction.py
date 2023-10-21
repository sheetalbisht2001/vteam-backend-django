import os
from decimal import Decimal
from os.path import expanduser, join
import uuid
import pandas as pd
from django.conf import settings
from django.core.management import BaseCommand
import requests
from django.http import HttpResponse
from bs4 import BeautifulSoup

from stractor.common.models.models import Distributor


PARENT_UPLINE_ID = '56a03a85-801d-4785-9099-4d3a1524f003'
COOKIE = 'ASP.NET_SessionId=hzfk5ke4ooinql0wmcsfjlao; _gid=GA1.2.492615491.1697886267; _gat_gtag_UA_209062538_1=1; _ga=GA1.1.1541421837.1690730274; _clck=1z0yy8y|2|fg1|0|1306; _clsk=1rwgznj|1697886269673|1|1|w.clarity.ms/collect; _ga_DFQYN30LLV=GS1.1.1697886267.11.0.1697886279.0.0.0; AWSALB=Hq94HBNWkOZLJrq/k+1OCGxIWWspwaltarB9VuYiJhP+MiWzudMw0DpPYdhLxHyGX68N5N4WgMdvwnxVXO6RugjzY56/2gidksw4RdAANly7Z2Uu430l+r2ifB/h; AWSALBCORS=Hq94HBNWkOZLJrq/k+1OCGxIWWspwaltarB9VuYiJhP+MiWzudMw0DpPYdhLxHyGX68N5N4WgMdvwnxVXO6RugjzY56/2gidksw4RdAANly7Z2Uu430l+r2ifB/h'

def fetch_downline_data(payload):
    # Define the URL
    url = 'https://www.myvestige.com/loggedin/downline.aspx'
    response_content = None
    # Define headers
    headers = {
        'authority': 'www.myvestige.com',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8,hi;q=0.7',
        'cache-control': 'max-age=0',
        'content-type': 'application/x-www-form-urlencoded',
        'cookie': COOKIE,
        'origin': 'https://www.myvestige.com',
        'referer': 'https://www.myvestige.com/loggedin/downline.aspx',
        'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"macOS"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36'
    }

    # Define the data
    data = {
        **payload,
       }

    # Make the POST request
    response = requests.post(url, headers=headers, data=data)

    # Check the response status code
    if response.status_code == 200:
        # Request was successful, you can access the response content like this:
        response_content = response.text
        
    else:
        # Request failed
        print(f"Request failed with status code: {response.status_code}")
    return response_content

def parse_html(downlines_html_data):
    # Sample HTML data (replace this with your HTML content)
    html_data = f"""
        {downlines_html_data}
    """
    # Parse the HTML using BeautifulSoup
    soup = BeautifulSoup(html_data, 'html.parser')

    # Find the <table> element
    tables = soup.find_all('table')
    data_list = []

    for table in tables:
        # Find all <tr> elements within the <tbody>
        tbodys = table.find_all('tbody')
        for tbody in tbodys:
            rows = tbody.find_all('tr')

            # Initialize an empty list to store the data
            

            # Iterate through the rows and extract data into dictionaries
            for row in rows:
                columns = row.find_all('td')
                if len(columns) == 14:  # Assuming each row has 14 columns
                    data_dict = {
                        'sno': columns[0].get_text(strip=True),
                        'distributor_id': columns[1].get_text(strip=True),
                        'reg_date': columns[2].get_text(strip=True),
                        'designation': columns[3].get_text(strip=True),
                        'name': columns[4].get_text(strip=True),
                        'percent': columns[5].get_text(strip=True),
                        'prev_cum_pv': columns[6].get_text(strip=True),
                        'exclusive_pv': columns[7].get_text(strip=True),
                        'self_pv': columns[8].get_text(strip=True),
                        'group_pv': columns[9].get_text(strip=True),
                        'total_pv': columns[10].get_text(strip=True),
                        'short_points': columns[11].get_text(strip=True),
                        'next_level_percent': columns[12].get_text(strip=True),
                        'view': columns[13].find('a').get('href') if columns[13].find('a') else None,
                    }
                    data_list.append(data_dict)
    return data_list

def get_event_target(input_string):
    import re
    result = None
    # Define the regular expression pattern
    pattern = r"'(rptDestributor\$ctl\d+\$lb_Downline)'"

    # Use re.search() to find the pattern in the input string
    match = re.search(pattern, input_string)

    # Check if a match is found
    if match:
        result = match.group(1)
    else:
        print("Pattern not found in the input string.")
    return result

def get_view_state(downlines_html_data):
    html_data = f"""
        {downlines_html_data}
    """
    viewstate_value = None
    # Create a BeautifulSoup object from the HTML
    soup = BeautifulSoup(html_data, 'html.parser')

    # Find the input element with id="__VIEWSTATE"
    viewstate_input = soup.find('input', {'id': '__VIEWSTATE'})

    # Check if the input element was found
    if viewstate_input:
        viewstate_value = viewstate_input.get('value')
    else:
        print("Input element with id=__VIEWSTATE not found.")

    return viewstate_value


def create_downline_data(downline_obj_arr, upline_id, event_target, view_state):
    print("START")
    payload = {
        '__EVENTTARGET': event_target,
        '__VIEWSTATE': view_state
    } if event_target and view_state else {}
    downline_html = fetch_downline_data(payload)
    downline_list = parse_html(downline_html) if downline_html else []
    new_view_state = get_view_state(downline_html) if downline_html else []
    if len(downline_list)==0:
        return;
    for downline_item in downline_list:
        downline_id = uuid.uuid4()
        downline_obj = Distributor(
            id=downline_id,
            name=downline_item.get('name', None),
            vid=downline_item.get('distributor_id', None),
            upline_id=upline_id,
            address=downline_item.get('address', None),
            phone_number=downline_item.get('phone_number', None),
        )
        downline_obj_arr.append(downline_obj)
        new_event_target = get_event_target(downline_item.get('view', None))
        create_downline_data(downline_obj_arr, downline_id, new_event_target, new_view_state)

    print(downline_list)  
    print("END")
    pass


class Command(BaseCommand):
    help = 'Creates the initial data entries'

    def handle(self, *args, **options):
        downline_obj_arr = []
        create_downline_data(downline_obj_arr, PARENT_UPLINE_ID, None, None)
        Distributor.objects.bulk_create(downline_obj_arr)
        print("SUCCESSFULLY DONE.")