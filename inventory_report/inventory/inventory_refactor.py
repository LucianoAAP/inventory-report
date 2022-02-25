from collections.abc import Iterable
from inventory_report.reports.complete_report import CompleteReport
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.inventory.inventory_iterator import InventoryIterator


def generate_report(report, type):
    if type == 'completo':
        return CompleteReport.generate(report)
    else:
        return SimpleReport.generate(report)


class InventoryRefactor(Iterable):
    def __init__(self, importer):
        self.importer = importer
        self.data = []
        self.report = ''

    def import_data(self, path, type):
        imported_data = self.importer.import_data(path)
        for imported_datum in imported_data:
            self.data.append(imported_datum)
        # print(self.data)
        self.report = generate_report(self.data, type)
        return self.data

    def __iter__(self):
        return InventoryIterator(self.data)
