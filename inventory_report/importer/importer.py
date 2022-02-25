from abc import ABC, abstractmethod
from inventory_report.reports.complete_report import CompleteReport
from inventory_report.reports.simple_report import SimpleReport


def generate_report(report, type):
    if type == 'completo':
        return CompleteReport.generate(report)
    else:
        return SimpleReport.generate(report)


class Importer(ABC):
    @abstractmethod
    def import_data(self):
        raise NotImplementedError
