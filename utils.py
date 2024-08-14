from datetime import datetime


def calculate_values_for_months(months, income_outcome_data):
    return_values = []
    current_cash = 0
    for month in months:
        income_for_month = calculate_income_for_month(month, income_outcome_data)
        current_cash += income_for_month
        cash_for_month = current_cash + income_for_month
        return_values.append(cash_for_month)
    return return_values

def calculate_income_for_month(
        month, income_outcome_data):
    incomes = get_income_sources_for_month(month, income_outcome_data)
    outcomes = get_outcome_sources_for_month(month, income_outcome_data)
    return incomes - outcomes

def get_income_sources_for_month(month, income_outcome_data):
    income_sources = income_outcome_data["income_sources"]
    values = []
    for income_source in income_sources:
        if datetime.strptime(income_source["start_date"], "%Y-%m-%d") <= month:
            values.append(float(income_source["amount"]))
    return sum(values)

def get_outcome_sources_for_month(month, income_outcome_data):
    outcome_sources = income_outcome_data["outcome_sources"]
    values = []
    for outcome_source in outcome_sources:
        if datetime.strptime(outcome_source["start_date"], "%Y-%m-%d") <= month:
            values.append(float(outcome_source["amount"]))
    return sum(values)