from django.core.management.base import BaseCommand, CommandError

from caesar_cipher.helpers import decipher
from caesar_cipher.models import Article


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('article_id', type=int)
        parser.add_argument('--shift', type=int, required=True)

    def handle(self, *args, **options):
        print("DAMIAN JAHN\n\n")
        article_id = options['article_id']
        shift = options['shift']
        if not shift in range(27):
            raise Exception('Shift must be in range 0-26')

        article = Article.objects.get(pk=article_id)
        all_words = decipher(article.body, shift).split(" ")
        capital_words = 0

        for element in all_words :
            if ord(element[:1]) > 64 and ord(element[:1]) < 91:
                capital_words += 1

        print(f'Capital words: {capital_words}, all words: {len(all_words)}')
        print(
            "{:.2f} % of capital words".format(capital_words / len(all_words) * 100)
        )

