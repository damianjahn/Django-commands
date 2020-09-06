from django.core.management.base import BaseCommand, CommandError

from caesar_cipher.models import CapitalWord


class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

    def add_arguments(self, parser):
        parser.add_argument('amount', type=int)

    def handle(self, *args, **options):
        print("DAMIAN JAHN\n\n")
        amount = options['amount']

        for element in CapitalWord.objects.order_by('-count')[:amount]:
            print(element.word)

