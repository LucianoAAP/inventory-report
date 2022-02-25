import csv
import json
import xmltodict

from inventory_report.reports.complete_report import CompleteReport
from inventory_report.reports.simple_report import SimpleReport


def generate_report(report, type):
    if type == 'completo':
        return CompleteReport.generate(report)
    else:
        return SimpleReport.generate(report)


class Inventory:
    def import_data(path, type):

        if path.split(".")[-1] == "csv":
            with open(path) as file:
                report = csv.DictReader(file)
                return generate_report(report, type)

        if path.split(".")[-1] == "json":
            with open(path) as file:
                report = json.load(file)
                return generate_report(report, type)

        if path.split(".")[-1] == "xml":
            with open(path) as file:
                parsed_file = xmltodict.parse(file.read())['dataset']['record']
                report = [dict(row) for row in parsed_file]
                return generate_report(report, type)
