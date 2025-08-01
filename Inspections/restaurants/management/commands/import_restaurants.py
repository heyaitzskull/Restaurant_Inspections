# app/management/commands/import_restaurants.py

import csv
from django.core.management.base import BaseCommand
from django.db import transaction
from restaurants.models import Restaurant


class Command(BaseCommand):
    help = "Import restaurants from a CSV file."

    def add_arguments(self, parser):
        parser.add_argument("csv_path", type=str)
        parser.add_argument("--batch-size", type=int, default=5000)

    def handle(self, *args, **opts):
        path = opts["csv_path"]
        batch_size = opts["batch_size"]

        objs = []
        total = 0

        with open(path, newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                try:
                    obj = Restaurant(
                        inspection_id=int(row["Inspection ID"]) if row["Inspection ID"] else None,
                        dba_name=row["DBA Name"],
                        aka_name=row["AKA Name"],
                        license=int(row["License #"]) if row["License #"] else None,
                        facility_type=row["Facility Type"],
                        risk=row["Risk"],
                        address=row["Address"],
                        city=row["City"],
                        state=row["State"],
                        zip=row["Zip"],
                        inspection_date=row["Inspection Date"],  # Could parse if needed
                        inspection_type=row["Inspection Type"],
                        results=row["Results"],
                        violations=row["Violations"],
                        lattitude=float(row["Latitude"]) if row["Latitude"] else None,
                        longitude=float(row["Longitude"]) if row["Longitude"] else None,
                        location=row["Location"],
                    )
                    objs.append(obj)
                except Exception as e:
                    self.stdout.write(self.style.WARNING(f"Skipping row due to error: {e}"))

                if len(objs) >= batch_size:
                    with transaction.atomic():
                        Restaurant.objects.bulk_create(objs, batch_size=batch_size)
                    total += len(objs)
                    self.stdout.write(f"Imported {total} rows...")
                    objs.clear()

        if objs:
            with transaction.atomic():
                Restaurant.objects.bulk_create(objs, batch_size=batch_size)
            total += len(objs)

        self.stdout.write(self.style.SUCCESS(f"Done. Imported {total} rows."))
