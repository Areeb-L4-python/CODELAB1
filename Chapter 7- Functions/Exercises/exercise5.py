def describe_city(city, country='Pakistan'):
    """Describe a city."""
    msg = f"{city.title()} is in {country.title()}."
    print(msg)

describe_city('Karachi','Pakistan')
describe_city('Abu Dhabi', 'UAE')
describe_city('London', 'UK')

