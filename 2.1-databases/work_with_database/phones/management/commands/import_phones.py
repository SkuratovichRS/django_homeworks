import csv

from django.core.management.base import BaseCommand
from phones.models import Phone
from django.utils.text import slugify


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open('phones.csv', 'r') as file:
            phones = list(csv.DictReader(file, delimiter=';'))

        for phone in phones:
            Phone.objects.create(
                id=int(phone.get("id")),
                name=phone.get("name"),
                price=phone.get("price"),
                image=phone.get("image"),
                release_date=phone.get("release_date"),
                lte_exists=bool(phone.get("lte_exists")),
                slug=slugify(phone.get("name"))
            )
