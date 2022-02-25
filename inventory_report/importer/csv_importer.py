import csv

from inventory_report.importer.importer import Importer


class CsvImporter(Importer):
    def import_data(import_file):
        if import_file.split(".")[-1] != "csv":
            raise ValueError('Arquivo inválido')

        with open(import_file) as file:
            parsed_file = csv.DictReader(file)
            list = [dict(row) for row in parsed_file]
            return list
