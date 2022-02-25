from typing import Counter
from datetime import date


def format_result(fabrication_date, expiration_date, company):
    return (
          f"Data de fabricação mais antiga: {fabrication_date}\n"
          f"Data de validade mais próxima: {expiration_date}\n"
          "Empresa com maior quantidade de produtos "
          f"estocados: {company}\n\n"
        )


class CompleteReport:
    @classmethod
    def generate(self, list):
        fabrication_dates = []
        expiration_dates = []
        companies = []

        for product in list:
            fabrication_dates.append(
              date.fromisoformat(product["data_de_fabricacao"])
            )

            expiration_date = date.fromisoformat(product["data_de_validade"])
            if expiration_date > date.today():
                expiration_dates.append(
                  date.fromisoformat(product["data_de_validade"])
                )

            companies.append(product["nome_da_empresa"])

        oldest_fabrication_date = min(fabrication_dates)
        closest_expiration_date = min(expiration_dates)
        most_products_company = Counter(companies).most_common()[0][0]
        counted_stock = dict(Counter(companies))
        counted_companies = dict(Counter(companies)).keys()
        stocked_products = "Produtos estocados por empresa: "

        for company in counted_companies:
            stocked_products = (
              f"{stocked_products}\n"
              f"- {company}: {counted_stock[company]}"
            )

        simple_report = format_result(
          oldest_fabrication_date,
          closest_expiration_date,
          most_products_company
        )

        return (
          f"{simple_report}"
          f"{stocked_products}\n"
        )
