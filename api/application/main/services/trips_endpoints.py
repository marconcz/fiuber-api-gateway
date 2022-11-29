import requests
import json
from pydantic import BaseModel
from application.initializer import LoggerInstance
URL = "https://trips-fiuber.herokuapp.com/"
#URL = "http://localhost:7777/"

class Passenger(BaseModel):
    email: str
    password: str
    passwordConfirmation: str
    name: str
    lastname: str
    birthday: str
    rol: str

class PassengerUpdateSchema(BaseModel):
    id: str
    rol: str
    name: str
    lastname: str

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

def trips_put(url, parameters):
    r = requests.put(url, params = parameters)
    logger.info('Request URL: {0} , status code = {1}'.format(r.url, r.status_code))
    return r.json()

def trips_trip_price(endpoint, parameters):
    PARAMS = {'distance' : parameters}
    return trips_get(URL + endpoint, PARAMS)

def trips_register_trip(endpoint, client, price, user_lat,user_long,dest_lat, dest_long):
    PARAMS = {'client_id' : client,\
                'price' : price,\
                'user_lat' : user_lat,\
                'user_long': user_long,\
                'dest_lat' : dest_lat,\
                'dest_long' : dest_long }
    return trips_post(URL + endpoint, PARAMS)

def trips_search_trip(endpoint):
    return trips_get(URL + endpoint, None)

def trips_register_driver(endpoint, trip, driver, driver_lat, driver_long):
    PARAMS = {'trip_id' : trip,\
                'driver_id' : driver,\
                'driver_lat' : driver_lat,\
                'driver_long' : driver_long }
    return trips_post(URL + endpoint, PARAMS)

def trips_get_driver(endpoint, trip):
    PARAMS = {'trip_id' : trip}
    return trips_post(URL + endpoint, PARAMS)

def update_pos(endpoint, trip_id, driver_lat, driver_long):
    PARAMS = {'trip_id' : trip_id,\
                'driver_lat' : driver_lat,\
                'driver_long' : driver_long }
    return trips_put(URL + endpoint, PARAMS)

def get_driver_pos(endpoint, trip_id):
   PARAMS = {'trip_id' : trip_id}
   return trips_get(URL + endpoint, PARAMS)

def get_trip_status(endpoint, trip_id):
    PARAMS = {'trip_id' : trip_id}
    return trips_get(URL + endpoint, PARAMS)

def init_trip(endpoint, trip_id):
    PARAMS = {'trip_id' : trip_id}
    return trips_put(URL + endpoint, PARAMS)

URL_USERS = "https://test-app-fiuber.herokuapp.com/api/v1/users/"

def validate_user_registered(endpoint, email):
    PARAMS = {'email' : email}
    r = requests.post(URL_USERS + endpoint, data = PARAMS)
    return r.json()

def register_a_passenger(endpoint, passenger: Passenger):
    wallet = requests.post('http://localhost:3000/wallet')
    passenger_with_wallet = passenger.dict()
    passenger_with_wallet['waddress'] = wallet.json()["address"]
    passenger_with_wallet['key'] = wallet.json()["privateKey"]
    print(passenger_with_wallet)
    r = requests.post(URL_USERS + endpoint, data = passenger_with_wallet)
    return r.json()

def update_a_passenger(endpoint, passenger: PassengerUpdateSchema):
    print("pasajero:", passenger.dict())
    r = requests.put(URL_USERS + endpoint, data = passenger.dict())
    return r.json()