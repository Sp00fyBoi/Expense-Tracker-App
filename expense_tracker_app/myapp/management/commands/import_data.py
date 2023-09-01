import csv
from datetime import datetime
from django.core.management.base import BaseCommand
from myapp.models import Book, BookCategory

class Command(BaseCommand):
    help = 'Import data from CSV file'

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str, help='Path to CSV file')

    def handle(self, *args, **kwargs):
        csv_file = kwargs['csv_file']

        # Open and read the CSV file
        with open(csv_file, 'r') as file:
            csv_reader = csv.reader(file)
            header = next(csv_reader)  # Get the header row

            # Check if the header contains the expected columns
            expected_columns = [
                'title', 'subtitle', 'authors', 'publisher', 'published_date', 'category_name', 'distribution_expense'
            ]
            if header != expected_columns:
                self.stdout.write(self.style.ERROR(f"Invalid CSV format. Expected columns: {', '.join(expected_columns)}"))
                return

            for row in csv_reader:
                # Check if the row has the correct number of columns
                if len(row) != len(expected_columns):
                    self.stdout.write(self.style.ERROR(f"Invalid row format: {', '.join(row)}. Skipping this record."))
                    continue

                # Extract data from the CSV row
                title, subtitle, authors, publisher, published_date, category_name, distribution_expense = row

                # Parse the date string into a DateField
                try:
                    published_date = datetime.strptime(published_date, '%m/%d/%Y').date()
                except ValueError:
                    self.stdout.write(self.style.ERROR(f"Invalid date format: {published_date}. Skipping this record."))
                    continue

                # Create or get the BookCategory
                category, created = BookCategory.objects.get_or_create(name=category_name)

                # Create the Book instance
                book = Book(
                    title=title,
                    subtitle=subtitle,
                    authors=authors,
                    publisher=publisher,
                    published_date=published_date,
                    distribution_expense=distribution_expense,
                    category=category
                )
                book.save()

        self.stdout.write(self.style.SUCCESS("Data import completed."))
