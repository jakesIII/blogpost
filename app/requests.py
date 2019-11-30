from . import models
import urllib.request, json

base_url=app.config['QUOTES_BASE_URL']

def get_quotes():

    quotes_url=base_url

    with urllib.request.urlopen(quotes_url) as url:
        data_quote=url.read()
        response_quote=json.loads(data_quote)

        
