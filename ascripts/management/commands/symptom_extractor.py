import os
from decimal import Decimal
from os.path import expanduser, join
import pandas as pd
from django.conf import settings
from django.core.management import BaseCommand
import requests
from django.http import HttpResponse
from stractor.common.models import Symptom, SearchWord, SearchWordToSymptom


def get_symptom_list():
    url = 'https://ubiehealth.com/_next/data/M6F9OuSUg-FdFe9P1JFQO/symptoms.json'
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        data = data['pageProps']['lps']
        data = [
            {
                'id':item['symptomUuid'],
                'title':item['seoName'],
                'path': item['path'],
                'speciality_id': None if not item['specialty'] or len(item['specialty'])==0 else item['specialty'],
                'disease_id': None if not item['diseaseUuid'] or len(item['diseaseUuid'])==0 else item['diseaseUuid']
            } for item in data]
    else:
        data = None
    return data

def get_search_words_for_symptom(symptom):
    url = 'https://ubiehealth.com/_next/data/M6F9OuSUg-FdFe9P1JFQO/symptoms/{}.json?name={}'.format(symptom, symptom)
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        data = data['pageProps']['searchWordOptions']
        data = [
            {
                'id':item['uuid'],
                'title':item['text'],
                'type': item['type'],
                'uid': None if not item['uid'] else item['uid']
            } for item in data]
    else:
        data = None
    return data

def create_symtom_data():
    print("START")
    symptom_objs = []
    search_word_objs = []
    symptom_to_search_word_objs = []
    symptom_list = get_symptom_list()
    count = 1
    if symptom_list:
        for item in symptom_list:
            symptomObj = Symptom(
                id=item['id'],
                title = item['title'],
                path = item['path'],
                speciality_id = item['speciality_id'],
                disease_id = item['disease_id']
            )
            symptom_objs.append(symptomObj)
            search_word_list = get_search_words_for_symptom(item['path'])
            if search_word_list:
                for search_word_item in search_word_list:
                    search_word_obj = SearchWord(
                        id=search_word_item['id'],
                        title=search_word_item['title'],
                        type=search_word_item['type'],
                        uid=search_word_item['uid'],
                    )
                    search_word_objs.append(search_word_obj)
                    symptom_to_search_word_obj = SearchWordToSymptom(
                        search_word_id=search_word_item['id'],
                        symptom_id=item['id']
                    )
                    symptom_to_search_word_objs.append(symptom_to_search_word_obj)
            print('Symptoms Inserted: ', count)
            count+=1

        Symptom.objects.bulk_create(symptom_objs, ignore_conflicts=True)
        SearchWord.objects.bulk_create(search_word_objs, ignore_conflicts=True)
        SearchWordToSymptom.objects.bulk_create(symptom_to_search_word_objs, ignore_conflicts=True)
    print("END")
    pass


class Command(BaseCommand):
    help = 'Creates the initial data entries'

    def handle(self, *args, **options):
        create_symtom_data()
        print("SUCCESSFULLY DONE.")
