from django.core.management.base import BaseCommand

from Fixtures.fakedata import generate_data


class Command(BaseCommand):
    help = 'Displays current time'

    def handle(self, *args, **options):
        generate_data()
        print('Database Seeded')
