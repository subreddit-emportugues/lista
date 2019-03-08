from time import sleep
from datetime import datetime
import requests
import pandas
import locale


locale.setlocale(locale.LC_ALL, 'pt_BR')


def get_data():
    subreddit_list = []
    subreddits = []

    with open('../res/data/subreddits_mini.txt', 'r') as file:
        for line in file:
            subreddit_list.append(line.rstrip())

    for subreddit in subreddit_list:
        
        response = requests.get('https://www.reddit.com/{}/about.json'.format(subreddit), headers={'User-agent': 'ept-crawler'})
        json_obj = response.json()
        data = json_obj['data']

        subreddit = []

        subreddit.append(format_icon_name(data['community_icon'], data['display_name_prefixed']))
        subreddit.append(data['public_description'])
        subreddit.append(format_subscribers(data['subscribers']))
        subreddit.append(format_age(data['created']))
        subreddit.append(format_nsfw(data['over18']))

        subreddits.append(subreddit)

        sleep(1)

    return pandas.DataFrame(subreddits, columns=['Subreddit', 'Descrição','Subscrições', 'Criação', 'NSFW'])


def convert_unix_timestamp(unixTimestamp):
    return datetime.utcfromtimestamp(unixTimestamp).strftime('%d/%m/%Y')


def get_date():
    return datetime.today().strftime('%d/%m/%Y')


def format_icon_name(icon, name):
    return '<img src="{}" width="20px" height="20px">&nbsp;&nbsp;{}'.format(icon, name)


def format_age(age):
    return '<span style="display: none">{}</span>{}'.format(age, convert_unix_timestamp(age))


def format_nsfw(nsfw):
    return 'Sim' if nsfw else 'Não'


def format_subscribers(subscribers):
    return subscribers
    # '<span style="display: none">{}</span>{}'.format(subscribers, locale.format("%d", subscribers, grouping=True))
