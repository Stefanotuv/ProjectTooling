import os
# Configure settings for project
# Need to run this before calling models from application!
os.environ.setdefault('DJANGO_SETTINGS_MODULE','DTS.settings')

import django
# Import settings
django.setup()

import random
from masterdata.models import Application, AppType, Region
from faker import Faker

fakegen = Faker()
regions = {'UK':'United Kingdom',
            'US':'United States',
            'HK':'Hong Kong',
            'CN':'China',
            'PL':'Poland'}

def populate_region_start():
    for key, value in regions.items():
        t = Region.objects.get_or_create(region_ID=key, region_name=value)[0]
        print (key)
        print(value)
        t.save()
    return t

def add_region(new_region_ID, new_region_name):
    t = Region.objects.get_or_create(region_ID=new_region_ID, region_name=new_region_name)[0]
    t.save()
    return t


if __name__ == '__main__':
    print("Populating the databases Region...Please Wait")
    add_topic()
    print('Populating Region Complete')
