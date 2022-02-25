import sys

from inventory_report.inventory.inventory_refactor import InventoryRefactor
from inventory_report.importer.csv_importer import CsvImporter
from inventory_report.importer.json_importer import JsonImporter
from inventory_report.importer.xml_importer import XmlImporter


def main():
    if len(sys.argv) < 3:
        return sys.stderr.write("Verifique os argumentos\n")

    inventory = {}

    if sys.argv[1].split(".")[-1] == "csv":
        inventory = InventoryRefactor(CsvImporter)
    elif sys.argv[1].split(".")[-1] == "json":
        inventory = InventoryRefactor(JsonImporter)
    elif sys.argv[1].split(".")[-1] == "xml":
        inventory = InventoryRefactor(XmlImporter)
    else:
        return sys.stderr.write("Verifique os argumentos\n")

    inventory.import_data(sys.argv[1], sys.argv[2])

    report = inventory.report

    print(report, end="")
