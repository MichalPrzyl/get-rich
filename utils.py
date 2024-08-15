from datetime import datetime


def calculate_values_for_months(months, income_outcome_data, initial_cash):
    return_values = []
    current_cash = initial_cash
    for month in months:
        income_for_month = calculate_income_for_month(month, income_outcome_data)
        print(f"current_cash before: {current_cash}")
        print(f"month: {month}")
        print(f"income_for_month: {income_for_month}")
        current_cash += income_for_month
        print(f"current_cash after: {current_cash}")
        # cash_for_month = current_cash + income_for_month
        # print(f"cash_for_month: {cash_for_month}")
        print(50*'-')
        return_values.append(current_cash)
    return return_values

def calculate_income_for_month(
        month, income_outcome_data):
    incomes = get_income_sources_for_month(month, income_outcome_data)
    print(f"incomes: {incomes}")
    outcomes = get_outcome_sources_for_month(month, income_outcome_data)
    print(f"outcomes: {outcomes}")
    return incomes - outcomes

def get_income_sources_for_month(month, income_outcome_data):
    income_sources = income_outcome_data["income_sources"]
    values = []
    for income_source in income_sources:
        if datetime.strptime(income_source["start_date"], "%Y-%m-%d") <= month \
                and datetime.strptime(income_source["end_date"], "%Y-%m-%d") >= month:
            values.append(float(income_source["amount"]))
    return sum(values)

def get_outcome_sources_for_month(month, income_outcome_data):
    outcome_sources = income_outcome_data["outcome_sources"]
    values = []
    for outcome_source in outcome_sources:
        if datetime.strptime(outcome_source["start_date"], "%Y-%m-%d") <= month \
                and datetime.strptime(outcome_source["end_date"], "%Y-%m-%d") >= month:
            values.append(float(outcome_source["amount"]))
    return sum(values)