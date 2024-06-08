# wait_for_django_mysql.py

import time
from django.core.management.base import BaseCommand
from django.db import connections
from django.db.utils import OperationalError

class Command(BaseCommand):
    help = 'Waits for the MySQL database to be available'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('Waiting for MySQL...'))
        db_conn = None
        while not db_conn:
            try:
                db_conn = connections['default']
            except OperationalError:
                self.stdout.write(self.style.WARNING('MySQL is not available yet. Retrying in 1 second...'))
                time.sleep(1)

        self.stdout.write(self.style.SUCCESS('MySQL is now available!'))
