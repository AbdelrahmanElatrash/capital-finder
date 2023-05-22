import os
import requests
from urllib.parse import urlencode , urlsplit , parse_qsl
from http.server import BaseHTTPRequestHandler


API_URL = "https://restcountries.com/v3.1/"

class handler(BaseHTTPRequestHandler):
 
    def do_GET(self):

        path=self.path
        url=urlsplit(path)    #  give 2 parts  url and query
        query_params=parse_qsl(url.query)  # take query part

        dic=dict(query_params)

        country=dic.get('country')
        capital=dic.get('capital')



        if country:
            capital=get_capital(country)

            if capital:
                result="The capital of {} is {}".format(country, capital)
            else:
                result= "Unable to find the capital of {}".format(country)
            
        elif capital :
            country=get_country(capital)

            if country:
                result= "{} is the capital of {}".format(capital, country)
            else:
                result= "Unable to find the country for capital {}".format(capital)

        else :
            result= "Invalid query parameters"

        


        self.send_response(200)
        self.send_header('Content-type','text/plain')
        self.end_headers()
        self.wfile.write(result.encode('utf-8'))
        return
    




def get_capital(country_name):
    
    query_params = {"name": country_name}  #to dict
    # Encode the query parameters
    query_string = urlencode(query_params) # name=country_name to str
    print(query_string)
    #  GET request to the REST Countries API
    response = requests.get(API_URL + "name/{}?{}".format(country_name, query_string))

    
    if response.status_code == 200:
        data = response.json()
        capital = data[0]["capital"]["name"]
        return capital
    else:
        return None



def get_country(capital_name):

    query_params = {"capital": capital_name}

    query_string = urlencode(query_params)

    response = requests.get(API_URL + "capital/{}?{}".format(capital_name, query_string))


    if response.status_code == 200:
        data = response.json()
        country_name = data[0]["name"]["common"]
        return country_name
    else:
        return None



