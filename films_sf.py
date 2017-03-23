import requests
from csv import DictReader
from sys import argv
from dateutil import parser as dateparser
from datetime import datetime
from urllib.parse import urljoin
from os.path import exists, join
import csv
from time import sleep

MAP_SIZE = '500x500'
BASE_MAP_URL = 'https://maps.googleapis.com/maps/api/streetview'
DIR_NAME = 'tempdata'
DATA_FNAME = join(DIR_NAME, 'Film_Locations_in_San_Francisco.csv')

def parse_data():
    #fname = fetch_data()
    thefile = open(DATA_FNAME, 'r', encoding = 'utf-8', errors = 'ignore')
    rawtxt = thefile.read()
    thefile.close()
    csv_raw = rawtxt.splitlines()
    csv_data = list(csv.DictReader(csv_raw))
    return csv_data


def make_map_url(location):
    my_request = requests.PreparedRequest()
    my_params = {'location': location, 'size' : MAP_SIZE, 'sensor':'false'}
    my_request.prepare_url(BASE_MAP_URL, my_params)
    the_url = my_request.url
    return the_url



def streetview_link(film_name):
    csv_data = parse_data()
    for entry in csv_data:
        title = entry['Title']
        if title == film_name:
            location = entry['Locations']
            url = make_map_url(location)
            return (url)

def msg_for_movie(film_name):
    csv_data = parse_data()
    for entry in csv_data:
        title = entry['Title']
        if title == film_name:
            location = entry['Locations']
            director = entry['Director']
            release_date = entry['Release Year']
            actor = entry['Actor 1']
            actor2 = entry['Actor 2']
            if actor2 == '':
                if actor == '':
                    msg_template = '{title}, a film by {director} released in {release_date} was filmed at {location}.'
                    msg =  msg_template.format(title = title, director = director, release_date = release_date, location = location)
                else:
                    msg_template = '{title}, a film by {director} released in {release_date} was filmed at {location}. It starred {actor}.'
                    msg =  msg_template.format(title = title, director = director, release_date = release_date, location = location, actor = actor)
            else:
                msg_template = '{title}, a film by {director} released in {release_date} was filmed at {location}. It starred {actor} and {actor2}.'
                msg =  msg_template.format(title = title, director = director, release_date = release_date, location = location, actor = actor, actor2 = actor2)
            return (msg)
            #sleep(2)

def get_film_list():
    csv_data = parse_data()
    #return csv_data
    film_list = []
    for entry in csv_data:
        title = entry['Title']
        film_list.append(title)
    return film_list


def main():
    print ("hello")
