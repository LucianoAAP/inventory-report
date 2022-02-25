import xmltodict

from inventory_report.importer.importer import Importer


class XmlImporter(Importer):
    def import_data(import_file):
        if import_file.split(".")[-1] != "xml":
            raise ValueError('Arquivo inválido')

        with open(import_file) as file:
            parsed_file = xmltodict.parse(file.read())['dataset']['record']
            list = [dict(row) for row in parsed_file]
            return list
