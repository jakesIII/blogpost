from .models import Quote
import urllib.request, json

base_url='http://quotes.stormconsultancy.co.uk/random.json'

def get_quotes():

    with urllib.request.urlopen(base_url) as url:
        base_url_data=url.read()
        quote_data=json.loads(base_url_data)
    return quote_data
