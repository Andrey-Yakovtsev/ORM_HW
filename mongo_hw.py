import csv
import re
from pprint import pprint
from datetime import datetime, date
from pymongo import MongoClient


client = MongoClient()

def import_data_from_file_to_db(filename):
    with open(filename, encoding='utf8') as csvfile:
        reader = csv.DictReader(csvfile)
        events = list(reader)
        for item in events:
            item['Дата'] = datetime.strptime(
                f'{item["Дата"]}.{datetime.now().year}', '%d.%m.%Y')
            item['Цена'] = int(item['Цена'])
        return events

def sort_by_price(price_direction=1):
    '''1 = ascending, -1 =  descending'''
    return list(events_collection.find().sort([('Цена', price_direction)]))

def sort_by_date(date_direction=1):
    '''1 = ascending, -1 =  descending'''
    return list(events_collection.find().sort([('Дата', -1)]))

events_db = client['events_list']
events_collection = events_db['events']

events_collection.delete_many({})
single_event = events_collection.insert_many(import_data_from_file_to_db('artists.csv'))

# pprint(sort_by_price(-1))
pprint(sort_by_date(-1))



# print(single_event.items())
# print(events_db.list_collection_names())