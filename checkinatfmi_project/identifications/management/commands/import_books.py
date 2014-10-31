import csv

from django.core.management.base import BaseCommand
from django.contrib.contenttypes.models import ContentType

from identifications.models import Book, BookCategory, BookLanguage
from activities.models import Carrier


class Command(BaseCommand):
    args = '<path_to_csv_file>'
    help = '''
        I will import books from the csv file.
        The format of the CSV file must be:
            title, author, publisher, language, category, copies, year
        We use the comma for value separation!

        May the force be with you!
    '''

    def handle(self, *args, **options):

        with open(args[0], 'r') as csvfile:
            csv_line = csv.reader(csvfile, delimiter=',', quotechar='|')
            for row in csv_line:
                title = row[0].strip()
                author = row[1].strip()
                publisher = row[2].strip()
                language_title = row[3].strip()
                category_title = row[4].strip()
                copies = row[5].strip()
                year = row[6]
                if year == '""':
                    year = None

                language, created = BookLanguage.objects.get_or_create(title=language_title)
                category, created = BookCategory.objects.get_or_create(title=category_title)
                language.save()
                category.save()


                book_type = ContentType.objects.get_for_model(Book)

                book = Book.objects.create(
                    title=title,
                    author=author,
                    publisher=publisher,
                    language=language,
                    category=category,
                    copies=copies,
                    year=year
                )
                # Create a carier
                carier = Carrier.objects.create()
                carier.status = Carrier.REGISTERED
                carier.data = book.id
                carier.content_type = book_type
                carier.object_id = book.id

                carier.save()
                book.save()
                print(book.title)
