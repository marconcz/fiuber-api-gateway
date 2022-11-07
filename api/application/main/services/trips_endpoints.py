import requests
from application.initializer import LoggerInstance
#URL = "https://trips-fiuber.herokuapp.com/"
URL = "http://localhost:7777/"

logger = LoggerInstance().get_logger(__name__)

def trips_get(url, parameters):
    if parameters is not None:
        r = requests.get(url, parameters)
    else:
        r = requests.get(url)
    logger.info('Request URL: {0} , status code = {1}'.format(r.url, r.status_code))
    return r.json()

def trips_post(url, parameters):
    r = requests.post(url, params = parameters)
    logger.info('Request URL: {0} , status code = {1}'.format(r.url, r.status_code))
    return r.json()

def trips_trip_price(endpoint, parameters):
    PARAMS = {'distance' : parameters}
    return trips_get(URL + endpoint, PARAMS)

def trips_register_trip(endpoint, client, price):
    PARAMS = {'client_id' : client, 'price' : price}
    return trips_post(URL + endpoint, PARAMS)

def trips_search_trip(endpoint):
    return trips_get(URL + endpoint, None)

def trips_register_driver(endpoint, trip, driver):
    PARAMS = {'trip_id' : trip, 'driver_id' : driver}
    return trips_post(URL + endpoint, PARAMS)

def trips_get_driver(endpoint, trip):
    PARAMS = {'trip_id' : trip}
    return trips_post(URL + endpoint, PARAMS)