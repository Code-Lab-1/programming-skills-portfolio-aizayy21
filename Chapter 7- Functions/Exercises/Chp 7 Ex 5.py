def describe_city(city, country='United Arab Emirates'):
    """Describe your city Where you live"""
    msg = city.title() + " is in " + country.title() + "."
    print(msg)
#the default country is United arab emirates
#however you can also edit/add as per your choice
describe_city('Sharjah')
describe_city('Ras Al Khaimah')
describe_city('Paris','France')
#I have written all of my favourite places
#my most favourite is United kingdom
describe_city('Bharmigham', 'United kingdom')