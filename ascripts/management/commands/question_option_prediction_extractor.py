import os
from decimal import Decimal
from os.path import expanduser, join
import pandas as pd
from django.conf import settings
from django.core.management import BaseCommand
import requests
from django.http import HttpResponse
from stractor.common.models import Symptom, SearchWord, SearchWordToSymptom


def create_session():
    url = 'https://ubiehealth.com/api/createSession'
    headers = {'Content-Type': 'application/json'}
    data = {}
    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 200:
        data = response.json()
        data = data['sessionKey']
    else:
        data = None
    return data

def main_complaint():
    url = 'https://ubiehealth.com/api/answerMonshinQuestion'
    headers = {'Content-Type': 'application/json'}
    data = {}
    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 200:
        data = response.json()
        data = data['sessionKey']
    else:
        data = None
    return data

def create_question_option_prediction_data():
    print("START")
    search_word_list = SearchWord.objects.all()
    count = 1
    if search_word_list:
        for item in search_word_list:
            session_key = create_session()

            print('Data Inserted: ', count)
            count+=1

    print("END")
    pass



class Command(BaseCommand):
    help = 'Creates the initial data entries'

    def handle(self, *args, **options):
        create_question_option_prediction_data()
        print("SUCCESSFULLY DONE.")
