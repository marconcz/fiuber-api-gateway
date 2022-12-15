import requests
import json
from pydantic import BaseModel
from application.initializer import LoggerInstance
URL = "https://trip-fiuber.herokuapp.com/"

class Driver(BaseModel):
    email: str
    password: str
    passwordConfirmation: str
    name: str
    lastname: str
    birthday: str
    rol: str

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
    idProfile: int

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

def trip_completed(endpoint, trip_id):
    PARAMS = {'trip_id' : trip_id}
    return trips_post(URL + endpoint, PARAMS)

def trip_qualify(endpoint, trip_id, user_id, score):
    PARAMS = {'trip_id' : trip_id, 'user_id' : user_id, 'score' : score}
    return trips_post(URL + endpoint, PARAMS)

def get_score_average(endpoint, user_id):
    PARAMS = {'user_id' : user_id}
    return trips_get(URL + endpoint, PARAMS)

def get_trip_history(endpoint, user_id):
    PARAMS = {'user_id' : user_id}
    return trips_get(URL + endpoint, PARAMS)

def cancel_a_trip(endpoint, trip_id):
    PARAMS = {'trip_id' : trip_id}
    return trips_post(URL + endpoint, PARAMS)

# USERS ENDPOINTS

URL_USERS = "https://users-fiuber.herokuapp.com/api/v1/users/"
URL_WALLET = "https://wallet-api-fiuber.herokuapp.com/"

def validate_user_registered(endpoint, email):
    PARAMS = {'email' : email}
    r = requests.post(URL_USERS + endpoint, data = PARAMS)
    print(r)
    return r.json()

def register_a_passenger(endpoint, passenger: Passenger):
    wallet = requests.post(URL_WALLET + 'wallet')
    passenger_with_wallet = passenger.dict()
    passenger_with_wallet['address'] = wallet.json()["address"]
    passenger_with_wallet['key'] = wallet.json()["privateKey"]
    print(passenger_with_wallet)
    r = requests.post(URL_USERS + endpoint, data = passenger_with_wallet)
    return r.json()

def update_a_passenger(endpoint, passenger: PassengerUpdateSchema):
    print("pasajero:", passenger.dict())
    r = requests.put(URL_USERS + endpoint, data = passenger.dict())
    return r.json()

def get_a_passenger(endpoint, email):
    PARAMS = {'email' : email}
    r = requests.post(URL_USERS + endpoint, data = PARAMS)
    return r.json()

def register_a_driver(endpoint, driver):
    wallet = requests.post(URL_WALLET + 'wallet')
    driver_with_wallet = driver.dict()
    driver_with_wallet['address'] = wallet.json()["address"]
    driver_with_wallet['key'] = wallet.json()["privateKey"]
    print(driver_with_wallet)
    r = requests.post(URL_USERS + endpoint, data = driver_with_wallet)
    return r.json()

def update_a_driver(endpoint, driver: PassengerUpdateSchema):
    print("driver:", driver.dict())
    r = requests.put(URL_USERS + endpoint, data = driver.dict())
    return r.json()

# Pays Endpoints 

def get_a_driver(endpoint, email):
    PARAMS = {'email' : email}
    r = requests.post(URL_USERS + endpoint, data = PARAMS)
    return r.json()

def get_balance(endpoint):
    r = requests.get(URL_WALLET + endpoint)
    print(URL_WALLET + endpoint)
    return r.json()

def deposit(endpoint, privateKey, amountInEthers):
    PARAMS = {"privateKey" : privateKey, "amountInEthers" : amountInEthers}
    PARAMS = json.dumps(PARAMS)
    headers = {'content-type': "application/json"}
    r = requests.post(URL_WALLET + endpoint, data = PARAMS, headers = headers)
    return r.json()

def pay(endpoint, privateKey, amountInEthers):
    return deposit(endpoint, privateKey, amountInEthers)
