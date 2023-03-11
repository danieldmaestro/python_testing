import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'PlayProject.settings')

import django
django.setup()

# fake population script
# from random import choice
from play_app.models import User
from faker import Faker

fake = Faker()

def populate(N=10):
    for en in range(N):
        name = fake.name()
        fname = name.split(" ")[0]
        lname = name.split(" ")[1]
        email = fake.email()

        # create new User entry
        user = User.objects.get_or_create(first_name = fname, last_name = lname, email = email)[0]

        # user.save()

if __name__ == '__main__':
    print('populating script!')
    populate(20)
    print('populating complete!')