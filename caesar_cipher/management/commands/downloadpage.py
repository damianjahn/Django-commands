from django.core.management.base import BaseCommand, CommandError
from bs4 import BeautifulSoup
import requests
from django.db import models

from caesar_cipher.helpers import cipher
from caesar_cipher.models import Article, Statistic, CapitalWord


class Command(BaseCommand):
    """
    parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('integers', metavar='N', type=int, nargs='+',
                    help='an integer for the accumulator')
parser.add_argument('--sum', dest='accumulate', action='store_const',
                    const=sum, default=max,
                    help='sum the integers (default: find the max)')

args = parser.parse_args()
print(args.accumulate(args.integers))
    """
    help = 'Closes the specified poll for voting'

    def add_arguments(self, parser):
        parser.add_argument('uri', type=str)
        parser.add_argument('--shift', type=int, required=True)



    def handle(self, *args, **options):
        print("DAMIAN JAHN")

        uri = options['uri']
        shift = options['shift']
        if not shift in range(27):
            raise Exception('Shift must be in range 0-26')
        if not uri:
            raise Exception('No URI provided')
        if not '://' in uri:
            raise Exception('No valid URI schema')

        response = requests.get(uri)
        soup = BeautifulSoup(response.text, 'html.parser')
        body = soup.body.get_text()

        article, created = Article.objects.get_or_create(
            uri=uri
        )
        article.body = cipher(body, shift),
        article.save()
        stat, stat_created = Statistic.objects.get_or_create(uri=uri)
        word_counter = {}
        for word in body.split(" "):
            if not(ord(word[:1]) >64 and ord(word[:1]) < 91):
                continue
            try:
                word_counter[word] = word_counter[word] + 1
            except KeyError:
                word_counter[word] = 1

        for k, v in word_counter.items():
            try:
                c_w = CapitalWord.objects.get(word=k)
                c_w.count = c_w.count + v
                c_w.save()
            except CapitalWord.DoesNotExist:
                c_w = CapitalWord.objects.create(
                    word=k, count=v
                )
                c_w.save()

        print(f"PageID: {article.pk}")
        if created:
            print('Article created')
        else:
            print('Article updated')