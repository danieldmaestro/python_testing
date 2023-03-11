import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'first_project.settings')

import django
django.setup()

# FAKE POP SCRIPT
import random
from first_app.models import AccessRecord, Webpage, Topic
from faker import Faker

fake = Faker()
topics = ['Search','Social', 'Marketplace', 'News', 'Games']

def add_topic():
    s = Topic.objects.get_or_create(top_name=random.choice(topics))
    print(s)
    t = s[0]
    t.save()
    
    print(t)
    return t

def populate(N=5):
    for entry in range(N):
        # get topic for entry
        top = add_topic()

        # create fake data for the entry
        fake_url = fake.url()
        fake_date = fake.date()
        fake_name = fake.company()

        # create new webpage entry
        webpg = Webpage.objects.get_or_create(topic = top, url = fake_url, name = fake_name)[0]

        # create fake access record
        acc_rec = AccessRecord.objects.get_or_create(name=webpg, date = fake_date)[0]

if __name__ == '__main__':
    print('populating script!')
    populate(20)
    print('populating complete!')

