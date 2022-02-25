import json

from inventory_report.importer.importer import Importer


class JsonImporter(Importer):
    def import_data(import_file):
        if import_file.split(".")[-1] != "json":
            raise ValueError('Arquivo inválido')

        with open(import_file) as file:
            list = json.load(file)
            return list
