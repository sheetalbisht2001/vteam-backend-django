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
import influxdb_client, os, time
from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS
from stractor.common.models.models import Distributor




class Command(BaseCommand):
    help = 'Creates the initial data entries'

    def handle(self, *args, **options):
        # this should be an all-access-token
        #  export INFLUXDB_TOKEN=8aHj2FpAZMcF7CtWDl63PpYPJJKkiGlJfb399rY-OIQ-_uWiIKldPxwnEd3x_vAFglLZZaSR2kkyk6vaOqmI5A==
        token = os.environ.get("INFLUXDB_TOKEN")
        org = "vteam"
        url = "http://localhost:8086"

        client = influxdb_client.InfluxDBClient(url=url, token=token, org=org)


        ## write data
        bucket="vteam"
        write_api = client.write_api(write_options=SYNCHRONOUS)
        
        for value in range(5):
            point = (
                Point("measurement1")
                .tag("tagname1", "tagvalue1")
                .field("field1", value)
            )
            write_api.write(bucket=bucket, org="vteam", record=point)
            time.sleep(1) # separate points by 1 second

        # execute simple query
        query_api = client.query_api()
        query = """from(bucket: "vteam")
        |> range(start: -10m)
        |> filter(fn: (r) => r._measurement == "measurement1")"""
        tables = query_api.query(query, org="vteam")

        for table in tables:
            for record in table.records:
                print(record)

        ## execute an aggregate query
        query_api = client.query_api()

        query = """from(bucket: "vteam")
        |> range(start: -10m)
        |> filter(fn: (r) => r._measurement == "measurement1")
        |> mean()"""
        tables = query_api.query(query, org="vteam")

        for table in tables:
            for record in table.records:
                print(record)
                


