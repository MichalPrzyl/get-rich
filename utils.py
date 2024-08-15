from datetime import datetime
import random


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
        print(50*'-')
        return_values.append(current_cash)
    return return_values

def calculate_income_for_month(
        month, income_outcome_data):
    incomes = get_income_sources_for_month(month, income_outcome_data)
    print(f"incomes: {incomes}")
    outcomes = get_outcome_sources_for_month(month, income_outcome_data)
    random_outcomes = get_random_sources_for_month(month, income_outcome_data)
    print(f"random_outcomes: {random_outcomes}")
    print(f"outcomes: {outcomes}")
    return incomes - outcomes - random_outcomes

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

def get_random_sources_for_month(month, income_outcome_data):
    random_outcome_sources = income_outcome_data["random_outcome_sources"]
    values = []
    for random_outcome_source in random_outcome_sources:
        if datetime.strptime(random_outcome_source["start_date"], "%Y-%m-%d") <= month \
                and datetime.strptime(random_outcome_source["end_date"], "%Y-%m-%d") >= month:
            # Get random value between min and max
            random_value = get_random_from_range(float(random_outcome_source["min_amount"]), float(random_outcome_source["max_amount"]))
            values.append(random_value)
    return sum(values)

def get_random_from_range(range_from, range_to):
    return random.randint(range_from, range_to)
