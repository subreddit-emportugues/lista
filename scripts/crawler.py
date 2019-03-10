from time import sleep
from datetime import datetime
import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
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

        session = requests.Session()
        retry = Retry(connect=3, backoff_factor=0.5)
        adapter = HTTPAdapter(max_retries=retry)
        session.mount('http://', adapter)
        session.mount('https://', adapter)
        
        response = session.get('https://www.reddit.com/{}/about.json'.format(subreddit), headers={'User-agent': 'ept-crawler'})
        json_obj = response.json()
        data = json_obj['data']

        subreddit = []

        subreddit.append(format_icon_name(data['community_icon'], data['display_name_prefixed'], data['over18']))
        subreddit.append(format_description(data['public_description']))
        subreddit.append(format_subscribers(data['subscribers']))
        subreddit.append(format_age(data['created']))
        subreddit.append(format_nsfw(data['over18']))

        subreddits.append(subreddit)

        sleep(1)

    return pandas.DataFrame(subreddits, columns=['Subreddit', 'Descrição','Inscrições', 'Criação', 'NSFW'])


def convert_unix_timestamp(unixTimestamp):
    return datetime.utcfromtimestamp(unixTimestamp).strftime('%d/%m/%Y')


def get_date():
    return datetime.today().strftime('%d/%m/%Y')


def format_icon_name(icon, name, nsfw):
    if nsfw:
        return '<img src="../docs/assets/img/subreddit-nsfw.png" width="20px" height="20px" style="border-radius: 50%;">&nbsp;&nbsp;<a class="link-style-3" target="_blank" href="https://www.reddit.com/{0}">{0}</a>'.format(name)
    else:
        if not icon:
            return '<img src="../docs/assets/img/subreddit.png" width="20px" height="20px" style="border-radius: 50%;">&nbsp;&nbsp;<a class="link-style-3" target="_blank" href="https://www.reddit.com/{0}">{0}</a>'.format(name)
        else:
            return '<img src="{0}" width="20px" height="20px" style="border-radius: 50%;">&nbsp;&nbsp;<a class="link-style-3" target="_blank" href="https://www.reddit.com/{1}">{1}</a>'.format(icon, name)


def format_description(description):
    if description:
        return '<div style="width: 400px; word-wrap: break-word;">{}</div>'.format(description)
    else:
        return ' <div align="center">- - -</div>'


def format_age(age):
    return convert_unix_timestamp(age)


def format_nsfw(nsfw):
    return 'Sim' if nsfw else 'Não'


def format_subscribers(subscribers):
    return locale.format("%d", subscribers, grouping=True)
